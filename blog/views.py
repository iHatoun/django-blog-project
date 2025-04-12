from django.shortcuts import render, get_object_or_404
from .models import Blog, Comment, Category
from django.contrib.auth.models import User

def main(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/main.html', {'blogs': blogs})

def users(request):
    users = User.objects.all()
    return render(request, 'blog/users.html', {'users': users})

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blogs.html', {'blogs': blogs})

def comments(request):
    comments = Comment.objects.all()
    return render(request, 'blog/comments.html', {'comments': comments})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'blog/categories.html', {'categories': categories})


def blogdetails(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comments = blog.comment_set.all()
    return render(request, 'blog/blogdetails.html', {'blog': blog, 'comments': comments})