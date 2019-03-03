from .models import Blog

from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.


def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})


def sy(request):
    return render(request, 'blog/sy.html')

def ja(request):
    return render(request, 'blog/ja.html')

def taewan(request):
    return render(request, 'blog/taewan.html')

def minji(request):
    return render(request, 'blog/minji.html')


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})


def new(request):
    return render(request, 'blog/new.html')


def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.save()
    return redirect('/blog/' + str(blog.id))
