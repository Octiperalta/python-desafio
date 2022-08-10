from django.urls import path
from . import views

urlpatterns = [
    path('mostrarFamiliares/', views.familiares),
    path('cargarFamiliares/', views.cargarFamiliares),
]
