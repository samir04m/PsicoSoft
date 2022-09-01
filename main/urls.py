from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('completar-registro/', views.CompletarRegistro, name='CompletarRegistro'),

    path('pacientes/', views.PacienteList, name='PacienteList'),
    path('pacientes-create/', views.PacienteCreate, name='PacienteCreate'),
    path('editar-paciente/<int:id>', views.PacienteUpdate, name='PacienteUpdate'),
    path('evolucion-paciente/<int:id>', views.PacienteEvolucion, name='PacienteEvolucion'),
    path('historia-clinica/<int:id>', views.PacienteDetails, name='PacienteDetails'),

    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('cambiar-contraseña/', views.change_password, name='change_password'),
    path('cuenta/', views.setting_account, name='setting_account'),
]