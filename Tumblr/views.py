from django.shortcuts import render
from Blog.models import Post


def index(request):
    print("Loading Home Page...")
    posts = Post.objects.all()
    return render(request, "index.html", {'posts': posts})


def blogs(request):
    print("Loading Blogs...")
    posts = Post.objects.all()
    return render(request, "blogs.html", {'posts': posts})

def blogs(request):
    print("Loading Blogs...")
    posts = Post.objects.all()
    return render(request, "blogs.html", {'posts': posts})