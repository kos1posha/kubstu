from django.contrib import admin
from django.contrib.auth import admin as djadmin
from django.utils.safestring import mark_safe


def _r(string):
    return mark_safe(''.join(f'&#{ord(c)};' for c in string))


class UserAdmin(djadmin.UserAdmin):
    fieldsets = [
        (_r('Аккаунт'), {'fields': ['email', 'password']}),
        (_r('Персональная информация'), {'fields': ['first_name', 'last_name']}),
        (_r('Статусы'), {'fields': ['is_active', 'is_superuser']}),
        (_r('Отслеживаемые даты'), {'fields': ['last_login', 'date_joined']}),
    ]
    add_fieldsets = [
        ('Обязательные поля', {
            'classes': ['wide'],
            'fields': ['first_name', 'last_name', 'email', 'password1', 'password2']
        })
    ]

    list_display = ['full_name', 'email', 'is_active', 'is_superuser']
    list_filter = ['is_active', 'is_superuser']
    readonly_fields = ['last_login', 'date_joined']
    search_fields = ['first_name', 'last_name', 'email']
    ordering = ['-is_superuser']

    @admin.display(description='Пользователь')
    def full_name(self, obj):
        return obj.full_name
