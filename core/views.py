from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post, Category, About
from django.contrib.auth.models import User
import datetime
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView

class PostListView(ListView):
    model = Post
    paginate_by = 3
    template_name = 'core/home.html'
    queryset = Post.objects.filter(published=True)
    
class PostDetailViews(DetailView):
   model = Post
   template_name = 'core/detail.html'

class CategoryListView(ListView):
    model = Category
    template_name = 'core/category.html'
   
    def get_queryset(self):
        category_id = self.kwargs['pk']
        if category_id:
            return Post.objects.filter(category=category_id, published=True)
        return super().get_queryset()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(id=self.kwargs['pk'])
        return context
    
class AuthorListView(ListView):
    model = User
    template_name = 'core/author.html'

    def get_queryset(self):
        author_id = self.kwargs['pk']
        if author_id:
            return Post.objects.filter(author=author_id, published=True)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = User.objects.get(id=self.kwargs['pk'])
        return context
    
class DateListView(ListView):
    model = Post
    template_name = 'core/date.html'

    def get_queryset(self):
        return super(ProvinciaList,
        self).get_queryset().filter(comunidad_id=self.kwargs.get("comunidad_id"))
    def get_queryset(self):
        month_id = self.kwargs['month_id']
        year_id = self.kwargs['year_id']
        #month_id = self.request.GET['month']
        #year_id = self.request.GET['year']
        
        return Post.objects.filter(published=True, created__month=month_id, created__year=year_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.date(self.kwargs['year_id'],self.kwargs['month_id'], 1)
        return context 

class AboutTemplateView(TemplateView):
    template_name = 'core/abouts.html'

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
