from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView, ListView, DetailView
from .models import Campo, Atividade, Progressao
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


class AtividadeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Atividade
    fields = ['campo', 'numero', 'descricao', 'detalhes', 'pontos']
    template_name = 'form.html'
    success_url = reverse_lazy('listaratividades')

    group_required = u"Docente"


    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)

        return url


class ProgressaoCreate(LoginRequiredMixin, CreateView):
    model = Progressao
    fields = ['data', 'data_final', 'observacao']
    template_name = 'form.html'
    success_url = reverse_lazy('listarprogressoes')


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


class ProgressaoList(ListView):
    model = Progressao
    template_name = 'progressoes.html'


    def get_queryset(self):
        self.object_list = Progressao.objects.filter(usuario=self.request.user)
        return self.object_list


class CampoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'form.html'
    success_url = reverse_lazy('listarcampos')

    group_required = u"Docente"


class AtividadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Atividade
    fields = ['campo', 'numero', 'descricao', 'detalhes', 'pontos']
    template_name = 'form.html'
    success_url = reverse_lazy('listaratividades')

    group_required = u"Docente"


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


class VerAtividade(LoginRequiredMixin, DetailView):
    model = Atividade
    template_name = 'ver_atividade.html'
