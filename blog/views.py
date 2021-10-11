from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
#from math import ceil


def index(request):
    blog = Blogpost.objects.all()
    return render(request, 'blog\index.html', {'blog':blog})

def postblog(request, id):
    post = Blogpost.objects.filter(post_id=id)[0]
    return render(request, 'blog\postblog.html', {'post':post})

def search(request):
    query = request.GET.get('search')
    blog = Blogpost.objects.filter(title=query)
    param = {'blog':blog}
    return render(request, 'blog\search.html', param)


