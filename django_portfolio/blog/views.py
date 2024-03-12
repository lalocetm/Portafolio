from django.shortcuts import render, get_object_or_404

from blog.models import Post


# Create your views here.

def renderPosts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html',{'posts': posts})

def postDetail(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, "post_detail.html", {'post':post})
