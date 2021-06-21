from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .forms import UsuarioForm
from .models import Perfil


class UsuarioCreate(CreateView):
    template_name = 'form.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')


    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Discente")

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url


    def get_context_data(self, *args ,**kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Criar Conta"
        context['botao'] = "Confirmar"
        context['cor'] = 'primary'

        return context


class Login(auth_views.LoginView):
    template_name = 'usuarios/login.html'


class Logout(auth_views.LogoutView):
    pass


class PerfilUpdate(UpdateView):
    template_name = "form.html"
    model = Perfil
    fields = ["nome_completo", "cpf", "telefone"]
    success_url = reverse_lazy("home")


    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)

        return self.object


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Meus Dados"
        context['botao'] = "Atualizar"
        context['cor'] = "yellow"

        return context


    def __str__(self):
        return self.object
