from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.user_home, name='home'),
    path('users/', include('users.urls')),
    path('services/', include('services.urls')),
]

