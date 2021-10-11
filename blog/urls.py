from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bloghome'),
    path('postblog/<int:id>', views.postblog, name='blogpost'),
    path('search', views.search, name='search'),
]
