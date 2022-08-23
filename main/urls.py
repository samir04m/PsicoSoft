from django.urls import path

from . import views

urlpatterns = [
    path('', views.Inicio, name='inicio'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
]