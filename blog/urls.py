from django.urls import include ,path
from .views import  PostDetailView , PostCreateView ,PostUpdateView ,PostDeleteView
from . import views

urlpatterns = [
    path('', views.about , name='blog-about'),
    path('home/', views.home , name='blog-home'),
    path('post/view/<int:pk>/',PostDetailView.as_view(),name='post-detail'),   
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/update/<int:pk>/',PostUpdateView.as_view(),name='post-update'),   
    path('post/delete/<int:pk>/',PostDeleteView.as_view(),name='post-delete'),   
]