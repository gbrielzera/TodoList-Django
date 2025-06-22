from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('criar/', views.criar_tarefa, name='criar_tarefa'),
    path('atualizar/<int:id>/', views.atualizar_tarefa, name='atualizar_tarefa'),
    path('deletar/<int:id>/', views.deletar_tarefa, name='deletar_tarefa'),
    path('editar/<int:id>/', views.editar_tarefa, name='editar_tarefa'),
]
