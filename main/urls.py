from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('pacientes/', views.PacienteList, name='PacienteList'),
    path('pacientes-create/', views.PacienteCreate, name='PacienteCreate'),
    path('historia-clinica/<int:id>', views.PacienteUpdate, name='PacienteUpdate'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
]