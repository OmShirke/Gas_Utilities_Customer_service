from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_home, name='home'),
    path('users/', include('users.urls')),
    path('services/', include('services.urls')),
]

