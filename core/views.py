from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category
from django.contrib.auth.models import User

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

def author(request, author_id):
    try:
        author = get_object_or_404(User, id=author_id)
        return render(request, 'core/author.html', {'author':author})
    except:
        return render(request, 'core/404.html')

def category(request, category_id):
    try:
        category = get_object_or_404(Category, id=category_id)
        
        return render(request, 'core/category.html', {'category':category})
    except:
        return render(request, 'core/404.html')

def date(request):
    return render(request, 'core/home.html')