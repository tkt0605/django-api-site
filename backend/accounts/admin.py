from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, Account
from django.contrib.auth import get_user_model

class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'is_staff', 'is_active']
    list_filter = ('is_staff', 'is_active')

    fieldsets = (
        (None, {
            "fields": ("email", "password")
            }
        ),
        ('Permisstion Info', {
            "fields": ("username", )
            }
        ),
        ("Permisstions", {
            "fields": ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')
            }
        ),
        ("Importants Date", {
            "fields": ("last_login", "date_joined")
            }
        )
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide", ),
            "fields": ("email", "username", "password1", "password2", "is_staff", "is_active")
            }
        )
    )
    search_fields = ("email", "username")
    ordering = ("email", )
    filter_horizontal = ('groups', 'user_permissions',)
admin.site.register(CustomUser, CustomUserAdmin)


