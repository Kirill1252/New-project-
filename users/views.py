from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.contrib.auth.models import Group
from .forms import RegisterUserForm


def index_view(request):
    context = {'title': 'Welcome'}
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
