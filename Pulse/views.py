from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from posts.models import Post

""" 
def index(request):
    posts = Post.objects.all()
    return render(request,"Pulse/index.html",{'posts': posts})
 """
from Pulse.feeds import PostFeed


def index(request):
    feed_queryset = PostFeed.get_feed(
        user=request.user, queryset=Post.objects.all(), excluded_ids=[], limit=20
    )
    return render(request, "Pulse/index.html", {"posts": feed_queryset})
