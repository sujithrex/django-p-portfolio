from django.shortcuts import render, get_object_or_404
from .models import all_blog

def all_blogs (request):
    all_bs= all_blog.objects.all()
    return render (request , 'blog/all_blogs.html', {'all_blogs' : all_bs})

def detail(request, blog_id):
    blog = get_object_or_404(all_blog, pk = blog_id)
    return render(request, 'blog/detail.html', {'blog' : blog})