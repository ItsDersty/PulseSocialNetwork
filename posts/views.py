from django.shortcuts import render
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