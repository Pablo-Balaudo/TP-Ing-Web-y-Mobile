from django.urls import path
from .views import (
    PostListView,
    PostDetailedView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='Foro'),
    path('post/<int:pk>/', PostDetailedView.as_view(), name='post-detail'),
    # int:pk is integer primary key (of the post to see in detail)
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
