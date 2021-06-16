from django.contrib.auth import views as auth_views


class Login(auth_views.LoginView):
    template_name = 'usuarios/login.html'


class Logout(auth_views.LogoutView):
    pass
