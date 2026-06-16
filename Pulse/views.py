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

import time


def index(request):
    alpha_time = time.perf_counter()
    # Gather IDs of posts the user has already liked to exclude them from the feed
    excluded_ids = Post.objects.filter(likes=request.user).values_list("id", flat=True)

    # Generate personalized recommendations directly via your Feed class
    feed_queryset = PostFeed.get_feed(
        user=request.user,
        queryset=Post.objects.all(),
        excluded_ids=excluded_ids,
        limit=20,
    )

    delta_time = time.perf_counter() - alpha_time
    return render(
        request, "Pulse/index.html", {"posts": feed_queryset, "delta_time": delta_time}
    )
