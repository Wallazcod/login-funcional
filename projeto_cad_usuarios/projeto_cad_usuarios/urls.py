from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # Rota, view responsavel, nome de referencia
    # Usuarios.com (pagina inicial)
    path('',views.home,name='home'),
    # usuarios.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
