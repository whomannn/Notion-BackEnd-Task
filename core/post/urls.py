from django.urls import path,include
from .views import *
urlpatterns = [
    path('create/', CreatePost.as_view(), name='post-list-create'),
    path('list/', ListPost.as_view(), name='post-list'),
    path('detail/<int:pk>', DetailPost.as_view(), name='post-detail'),
    path('update/<int:pk>', UpdatePost.as_view(), name='post-update'),
    path('delete/<int:pk>', DeletePost.as_view(), name='post-delete'),
]
