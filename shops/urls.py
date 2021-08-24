from django.urls import path

from shops import views

urlpatterns=[
    path('', views.index, name='index'),
    path('products/', views.products, name='products_list')
]