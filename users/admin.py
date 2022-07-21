from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    search_fields = ('pk', 'username', 'email', 'mobile')
    prepopulated_fields = {'username': ('email',)}
    list_display = ('pk', 'username', 'email', 'mobile')
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        ('Custom fields', {
            'fields': (
                'slug',
                'instagram',
                'facebook',
                'avatar',
                'mobile',
                'email'
            )
        })
    )
    fieldsets = (
        *UserAdmin.fieldsets,
        ('Custom fields', {
            'fields': (
                'slug',
                'instagram',
                'facebook',
                'avatar',
                'mobile'
            )
        })
    )


admin.site.register(CustomUser, CustomUserAdmin)