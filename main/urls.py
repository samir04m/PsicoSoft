from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('pacientes/', views.PacienteList, name='PacienteList'),
    path('pacientes-save/', views.PacienteSave, name='PacienteSave'),
    path('historia-clinica/<int:id>', views.PacienteCreate, name='PacienteCreate'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
]