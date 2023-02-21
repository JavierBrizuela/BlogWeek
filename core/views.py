from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

def home(request):
    post_page = Paginator(Post.objects.filter(published=True), 3)
    page = request.GET.get('page')
    posts = post_page.get_page(page)
    return render(request, 'core/home.html', {'posts':posts})

def post(request, post_id):
    #post = Post.objects.get(id=post_id)
    try:
        post = get_object_or_404(Post, id=post_id)
        return render(request, 'core/detail.html', {'post':post})
    except:
        return render(request, 'core/404.html')

def author(request):
    return render(request, 'core/home.html')

def category(request):
    return render(request, 'core/home.html')

def date(request):
    return render(request, 'core/home.html')