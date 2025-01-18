from django.urls import path
from . import views

urlpatterns = [
    path('submit-request/', views.submit_request, name='submit_request'),
]
