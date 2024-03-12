from django.urls import path

from blog.views import renderPosts, postDetail

app_name = 'blog'

urlpatterns = [
    path('', renderPosts, name = 'posts'),
    path('<int:id>', postDetail, name = 'postDetail'),
]