from django.urls import path
from .views import UsuarioCreate, Login, Logout, PerfilUpdate

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),
    path('atualizar-dados/', PerfilUpdate.as_view(), name='atualizar-dados'),
]
