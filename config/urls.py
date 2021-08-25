from django.contrib import admin
from django.urls import path, include

from config import views

urlpatterns = [
    path('shops/', include('shops.urls')),
    path('', views.index, name='index'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('admin/', admin.site.urls)
]