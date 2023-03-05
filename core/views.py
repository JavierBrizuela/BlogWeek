from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post, Category
from django.contrib.auth.models import User
import datetime
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

class PostListView(ListView):
    model = Post
    paginate_by = 3
    template_name = 'core/home.html'
    
    def get_queryset(self):
        return Post.objects.filter(published=True)
    

class PostDetailViews(DetailView):
   model = Post
   template_name = 'core/detail.html'

class CategoryListView(ListView):
    model = Category
    template_name = 'core/category.html'
   
    def get_queryset(self):
        category_id = self.request.GET['cat']
        if category_id:
            return Post.objects.filter(category=category_id, published=True)
        return super().get_queryset()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(id=self.request.GET['cat'])
        return context
    
class AuthorListView(ListView):
    model = User
    template_name = 'core/author.html'

    def get_queryset(self):
        author_id = self.request.GET['aut']
        if author_id:
            return Post.objects.filter(author=author_id, published=True)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = User.objects.get(id=self.request.GET['aut'])
        return context
    
class DateListView(ListView):
    model = Post
    template_name = 'core/date.html'

    def get_queryset(self):
        month_id = self.request.GET['month']
        year_id = self.request.GET['year']
        print(month_id, year_id)
        return Post.objects.filter(publised=True, created__month=month_id, created__year=year_id)

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('home')

class PostUpdateview(UpdateView):
    model = Post
    form_class = PostForm
    template_name_suffix = '_update_form'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('update', args=[self.object.id]) + '?ok'

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')

""" def author(request, author_id):
    try:
        author = get_object_or_404(User, id=author_id)
        return render(request, 'core/author.html', {'author':author})
    except:
        return render(request, 'core/404.html') 
    
def date(request, month_id, year_id):
        posts = Post.objects.filter(published=True, created__month=month_id, created__year=year_id)
        fecha = datetime.date(year_id, month_id, 1)
        return render(request, 'core/date.html', {'posts':posts,'fecha':fecha}) """