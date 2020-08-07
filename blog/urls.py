from django.urls import path,include
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from . import views

urlpatterns = [
	path('', PostListView.as_view(),name="blog-home"),
	path('user/<str:username>', UserPostListView.as_view(), name='userposts'),
	path('post/<int:pk>/', PostDetailView.as_view(),name="postdetail"),
	path('post/<int:pk>/update', PostUpdateView.as_view(),name="postupdate"),
	path('post/<int:pk>/delete', PostDeleteView.as_view(),name="postdelete"),
	path('post/new', PostCreateView.as_view(),name='postcreate'),
	path('about/', views.about,name='blog-about'),
]
