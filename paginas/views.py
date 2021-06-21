from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView, ListView, DetailView
from .models import Campo, Atividade
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


class HomeView(TemplateView):
    template_name = 'home.html'


class CampoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'form.html'
    success_url = reverse_lazy('listarcampos')

    group_required = u"Docente"


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Criar Matéria"
        context['botao'] = "Cadastrar"
        context['cor'] = 'primary'

        return context


class AtividadeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Atividade
    fields = ['campo', 'numero', 'descricao', 'detalhes', 'pontos']
    template_name = 'form.html'
    success_url = reverse_lazy('listaratividades')

    group_required = u"Docente"


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Criar Atividade"
        context['botao'] = "Cadastrar"
        context['cor'] = 'primary'

        return context


    def form_valid(self, form):
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        return url


class CampoList(ListView):
    model = Campo
    template_name = 'campos.html'


class AtividadeList(ListView):
    model = Atividade
    template_name = 'atividades.html'


class CampoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'form.html'
    success_url = reverse_lazy('listarcampos')

    group_required = u"Docente"


    def get_context_data(self, *args ,**kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Alterar Campo"
        context['botao'] = "Editar"
        context['cor'] = 'yellow'

        return context


class AtividadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Atividade
    fields = ['campo', 'numero', 'descricao', 'detalhes', 'pontos']
    template_name = 'form.html'
    success_url = reverse_lazy('listaratividades')

    group_required = u"Docente"


    def get_context_data(self, *args ,**kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Alterar Atividade"
        context['botao'] = "Editar"
        context['cor'] = 'yellow'

        return context


class CampoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Campo
    template_name = 'excluir.html'
    success_url = reverse_lazy('listarcampos')

    group_required = u"Docente"


class AtividadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Atividade
    template_name = 'excluir.html'
    success_url = reverse_lazy('listaratividades')

    group_required = u"Docente"


class VerAtividade(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    model = Atividade
    template_name = 'ver_atividade.html'

    group_required = [u'Discente', u'Docente']
