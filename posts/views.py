from django.shortcuts import render,redirect
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required
from .models import Post

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
    if request.method == "GET":
        post = Post.objects.get(id=id)
        return render(request,'posts/postPage.html', {'post': post})

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