from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import get_user_model

Users=get_user_model()

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save() # Сохранение пользователя в базу данных
            return redirect('login') # Перенаправление на страницу входа
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def viewUser(request,id):
    if request.method == "GET":
        profile = Users.objects.get(id=id)
        return render(request,'users/userPage.html', {'profile': profile})