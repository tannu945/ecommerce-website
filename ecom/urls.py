from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='AboutUs'),
    path('contact/', views.contact, name='ContactUs'),
    path('tracker/', views.tracker, name='TrackingStatus'),
    path('products/<int:myid>', views.productview, name='ProductView'),
    path('search/',views.search, name='Search'),
    path('checkout/', views.checkout, name='CheckOut'),
    path('placeorder/', views.placeorder, name='PlaceOrder'),
    path('handlerequest/', views.handlerequest, name='HandleRequest'),

]
