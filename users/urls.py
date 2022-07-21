from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from .views import index_view, NewUserRegistration, UserPageView, LoginUser

app_name = 'user'

urlpatterns = [
    path('', index_view, name='index'),
    path('registration/', NewUserRegistration.as_view(), name='registration'),
    path('profile/<slug:slug>/', UserPageView.as_view(), name='profile'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('user:login')), name='logout')

]