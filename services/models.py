from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    ]

    REQUEST_TYPE_CHOICES = [
        ('new_connection', 'New Connection'),
        ('modification', 'Service Modification'),
        ('maintenance', 'Maintenance and Repairs'),
        ('billing', 'Billing and Payment'),
        ('disconnection', 'Disconnection or Reconnection'),
        ('inspection', 'Safety Inspection'),
        ('upgrade', 'Service Upgrade'),
        ('emergency', 'Emergency Services'),
        ('general', 'General Inquiry'),
    ]
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPE_CHOICES)

    customer_name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.TextField(null=True, blank=True)

    def __str__(self):
         return f"Request by {self.customer_name} ({self.status})"
