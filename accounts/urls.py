from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path('', views.SignUpView.as_view(), name='signup'),

    path('login/',
         auth_views.LoginView.as_view(template_name='login.html'),
         name='login'),

    path('logout/',
         auth_views.LogoutView.as_view(next_page=reverse_lazy('typingapp:index')),
         name='logout'),

]
