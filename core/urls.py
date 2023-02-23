from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>', views.post, name='post'),
    path('author/<int:author_id>', views.author, name='author'),
    path('category/<int:category_id>', views.category, name='category'),
    path('date/', views.date, name='date'),
]