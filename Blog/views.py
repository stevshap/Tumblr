from django.shortcuts import render
from Blog.models import Post

# Create your views here.
def post_view(request, id):
    posts = Post.objects.get(id = id)
    return render(request, "posts.html", {'posts': posts})