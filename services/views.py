from django.shortcuts import render, get_object_or_404, redirect
from .models import ServiceRequest
from django.contrib import messages 
from .forms import ServiceRequestForm, ServiceRequestResponseForm
from django.http import Http404
from django.contrib.auth.decorators import login_required

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user  # Associate the request with the logged-in user
            service_request.save()
            messages.success(request, 'Your service request has been successfully submitted.')
            
            # Redirect to home page
            return redirect('home')
    else:
        form = ServiceRequestForm()
    
    return render(request, 'services/submit_request.html', {'form': form})

@login_required
def track_request(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'services/track_request.html', {'requests': requests})

def respond(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)

    # Check if the logged-in user is an admin or the owner of the request
    if not request.user.is_staff and request.user != service_request.user:
        raise Http404("You are not allowed to respond to this request.")
    
    if request.method == 'POST':
        form = ServiceRequestResponseForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            return redirect('services:track_request')  # Redirect to track request page
    else:
        form = ServiceRequestResponseForm(instance=service_request)
    
    return render(request, 'services/respond.html', {'form': form, 'service_request': service_request})