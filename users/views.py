from django.shortcuts import render, redirect
from .forms import RegisterForm,EditUserForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

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
    
@login_required
def editUser(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save() # Сохранение пользователя в базу данных
            return redirect(f'/users/{request.user.id}') # Перенаправление на страницу входа
    else:
        form = EditUserForm(instance=request.user)
    return render(request, 'users/editUser.html', {'form': form})