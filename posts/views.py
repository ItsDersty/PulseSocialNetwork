from django.shortcuts import render,redirect
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required
from .models import Post
from django.http import JsonResponse

@login_required
def newPost(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('postPage',id=post.id) 
    else:
        form = NewPostForm()
    return render(request, 'posts/newPost.html', {'form': form})

def viewPost(request,id):
    post = Post.objects.get(id=id)
    form=NewPostForm(request.POST or None)

    if request.method == "GET":
        return render(request,'posts/postPage.html', {'post': post,'form': form})
    elif request.method == "POST" and form.is_valid():
        reply = form.save(commit=False)
        reply.author = request.user
        reply.parent = post
        reply.save()
        return redirect(request,f'/post/{reply.id}')
    
def likePost(request,id):
    if request.method == "POST":
        post = Post.objects.get(id=id)
        liked = None
        
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True

        return JsonResponse({
            'liked': liked,
            'count': post.likes.count(),
        })
        

""" TODO:make newpost logic
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save() # Сохранение пользователя в базу данных
            return redirect('login') # Перенаправление на страницу входа
    else:
        form = RegisterForm()
    return render(request, 'pages/register.html', {'form': form})
 """