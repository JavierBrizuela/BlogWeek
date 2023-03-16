from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/<pk>', views.PostDetailViews.as_view(), name='post'),
    path('author/<pk>', views.AuthorListView.as_view(), name='author'),
    path('category/<pk>', views.CategoryListView.as_view(), name='category'),
    path('date/<int:month_id>/<int:year_id>/', views.DateListView.as_view(), name='date'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('update/<pk>', views.PostUpdateview.as_view(), name='update'),
    path('delete/<pk>', views.PostDeleteView.as_view(), name='delete'),
    path('abouts/', views.AboutTemplateView.as_view(),name='abouts'),
    path('accounts/', include('django.contrib.auth.urls')),
]