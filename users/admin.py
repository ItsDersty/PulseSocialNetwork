from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import PulseUser  # импортируем модели

@admin.register(PulseUser)
class CustomUserAdmin(UserAdmin):
    model = PulseUser
    # Какие поля показывать в списке
    list_display = ['username', 'email', 'is_staff', 'bio']
    # Какие поля редактировать в админке
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'pfp', 'followers')}),
    )

