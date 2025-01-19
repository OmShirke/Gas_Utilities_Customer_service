from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('track-request/', views.track_request, name='track_request'),
]
