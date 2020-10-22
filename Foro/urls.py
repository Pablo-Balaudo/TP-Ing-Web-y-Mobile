from django.urls import path, include

from .views import (
    PostListView,
    post_detail,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='Foro'),

    # int:pk is integer primary key (of the post to see in detail)
    path('post/<int:pk>/', post_detail, name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/report/', PostDeleteView.as_view(), name='post-report'),

    path('user/<str:username>/', UserPostListView.as_view(), name='user-post'),

    path('post/<int:pk>/comment-update/', CommentUpdateView.as_view(), name='comment-update'),
    path('post/<int:pk>/comment-delete/', CommentDeleteView.as_view(), name='comment-delete'),

    path('search/', include('haystack.urls')),
]
