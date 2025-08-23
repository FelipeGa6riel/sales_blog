from django.urls import path
from blog.views import index_posts, post_detail

urlpatterns = [
    path('', index_posts, name='index'),
    path('post/<int:pk>/<str:title>', post_detail, name='post_detail')
]
