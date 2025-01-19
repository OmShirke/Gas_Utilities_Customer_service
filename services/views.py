from django.shortcuts import render
from .models import ServiceRequest

def services(request):
    services = ServiceRequest.objects.all()
    return render(request, 'services/services.html', {'services': services})

def track_request(request):
    if request.method == 'POST':
        request_title = request.POST.get('request_title')
        ServiceRequest.objects.create(title=request_title, status="Pending")
        return redirect('services')
    return render(request, 'services/track_request.html')
