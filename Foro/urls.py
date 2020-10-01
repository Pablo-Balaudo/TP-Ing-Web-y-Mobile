from django.urls import path
from .views import (
    PostListView,
    PostDetailedView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='Foro'),
    path('post/<int:pk>/', PostDetailedView.as_view(), name='post-detail'),
    # int:pk is integer primary key (of the post to see in detail)
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('user/<str:username>/', UserPostListView.as_view(), name='user-post'),

    path('post/comment/new/', CommentCreateView.as_view(), name='comment-create'),
    path('post/<int:pk>/comment-update/', CommentUpdateView.as_view(), name='comment-update'),
    path('post/<int:pk>/comment-delete/', CommentDeleteView.as_view(), name='comment-delete'),


]
