from django.urls import path
from main.views import index
from main.views import RegisterView
from . import views

urlpatterns = [
    path('', index, name='index'),
    
    path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('encuestas/crear/', views.crear_encuesta_view, name='crear_encuesta'),
    path('encuestas/guardar/', views.guardar_encuesta_view, name='guardar_encuesta'),
]
