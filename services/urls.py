from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('respond/<int:request_id>/', views.respond, name='respond'),
    path('track/', views.track_request, name='track_request'),
]

