from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import Group
from .forms import RegisterUserForm, LoginForm
from .models import CustomUser


def index_view(request):
    context = {'title': 'Home'}
    return render(request, 'home.html', context)


class NewUserRegistration(CreateView):
    form_class = RegisterUserForm
    template_name = 'user/register_user.html'

    def post(self, request, *args, **kwargs):
        form = RegisterUserForm(request.POST, request.FILES)
        user = form.save(commit=False)
        user.email = user.username
        user.slug = user.username.split('@')[0]
        user.save()
        group = Group.objects.get(name='groups_user')
        user.groups.add(group)
        login(self.request, user)
        return redirect('user:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        return context


class UserPageView(DetailView):
    model = CustomUser
    template_name = 'user/user_page.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'User Page'
        return context


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context

    def get_success_url(self):
        return reverse_lazy('user:index')
