from django.contrib import admin
from django.urls import path, include

from config import views

urlpatterns = [
    path('shops/', include('shops.urls')),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('admin/', admin.site.urls)
]