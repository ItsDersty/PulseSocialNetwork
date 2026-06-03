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
from django_neural_feed.services import RecommendationService
from posts.models import Post


def index(request):
    # Get IDs of items to exclude (e.g., dislikes or hidden posts)
    excluded_ids = []

    # Get user's active likes to calculate interests
    user_likes = request.user.likedPosts.all()

    feed_queryset = RecommendationService.get_feed_for_user(
        user=request.user,
        model_class=Post,
        queryset=Post.objects.all(),
        likes_queryset=user_likes,
        excluded_ids=excluded_ids,
        limit=20,
    )

    return render(request, "Pulse/index.html", {"posts": feed_queryset})
