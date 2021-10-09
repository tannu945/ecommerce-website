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


'''def category_header(request):
    #allcategory = []
    cat_values = Blogpost.objects.filter(category='Technology')
    #allcategory.append(prod)
    #allcat = {'allcategory':allcategory}
    #print(allcat)
    #print(len(allcat))
    print(cat_values[0])
    return render(request, 'blog\category_blog.html', {'product':cat_values[0]})'''


