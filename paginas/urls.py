from django.urls import path
from .views import HomeView, CampoCreate, AtividadeCreate, CampoList, AtividadeList, \
    CampoUpdate,\
    AtividadeUpdate, CampoDelete, AtividadeDelete, VerAtividade, ProgressaoCreate, ProgressaoList

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cadastrar/campo', CampoCreate.as_view(), name='cadastrarcampo'),
    path('cadastrar/atividade', AtividadeCreate.as_view(), name='cadastraratividade'),
    path('cadastrar/progressao', ProgressaoCreate.as_view(), name='cadastrarprogressao'),

    path('listar/campos', CampoList.as_view(), name='listarcampos'),
    path('listar/atividades', AtividadeList.as_view(), name='listaratividades'),
    path('listar/progressoes', ProgressaoList.as_view(), name='listarprogressoes'),
    path('ver/atividade/<int:pk>', VerAtividade.as_view(), name='veratividade'),

    path('editar/campo/<int:pk>', CampoUpdate.as_view(), name='editarcampo'),
    path('editar/atividade/<int:pk>', AtividadeUpdate.as_view(), name='editaratividade'),

    path('excluir/campo/<int:pk>', CampoDelete.as_view(), name='excluircampo'),
    path('excluir/atividade/<int:pk>', AtividadeDelete.as_view(), name='excluiratividade'),
]
