from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bloghome'),
    path('postblog/<int:id>', views.postblog, name='blogpost'),
    #path('category_header', views.category_header, name='b=category_header'),
]
