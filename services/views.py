from django.shortcuts import render
from .models import ServiceRequest

def submit_request(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        email = request.POST['email']
        request_type = request.POST['request_type']
        description = request.POST['description']
        ServiceRequest.objects.create(
            customer_name=customer_name,
            email=email,
            request_type=request_type,
            description=description
        )
        return render(request, 'success.html')

    return render(request, 'submit_request.html')

def home(request):
    return render(request, 'home.html')
