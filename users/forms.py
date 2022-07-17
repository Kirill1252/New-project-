from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'avatar', 'instagram', 'mobile', 'facebook')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'avatar', 'instagram', 'mobile', 'facebook')


class RegisterUserForm(CustomUserCreationForm):
    username = forms.EmailField(label='Email address',)
    password1 = forms.CharField(label='Password ',)
    password2 = forms.CharField(label='Password confirmation ',)
    mobile = forms.IntegerField(label='Mobile',)
    first_name = forms.CharField(label='First Name',)
    last_name = forms.CharField(label='Last Name',)
    avatar = forms.CharField(label='Avatar',)
    instagram = forms.CharField(label='Instagram',)
    facebook = forms.CharField(label='Facebook',)

    class Meta:
        model = CustomUser
        fields = (
            'username', 'password1', 'password2',
            'mobile', 'first_name',
            'last_name', 'avatar', 'instagram',
            'facebook',
        )


class UpdateUserData(CustomUserChangeForm):
    mobile = forms.IntegerField(label='Mobile',)
    first_name = forms.CharField(label='First Name',)
    last_name = forms.CharField(label='Last Name',)
    avatar = forms.CharField(label='Avatar',)
    instagram = forms.CharField(label='Instagram',)
    facebook = forms.CharField(label='Facebook',)

    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'avatar',
            'instagram', 'facebook',
            'mobile',
        )


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email address',)
    password = forms.CharField(label='Password',)
