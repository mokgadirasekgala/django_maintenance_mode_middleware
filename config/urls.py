from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('shops/', include('shops.urls')),
    path('admin/', admin.site.urls)
]