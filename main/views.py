from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.db.utils import IntegrityError
from main.services import crear_usuario

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')
def index(request):
    return render(request, 'index.html')
class RegisterView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        name = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']
        # Validación del passoword ingresado
        if password != password_repeat:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, 'registration/register.html')
        try:
            crear_usuario(name, first_name, last_name, email, password)
        except IntegrityError:
            messages.error(request, 'El el correo ya existe')
            return render(request, 'registration/register.html')
        except Exception:
            messages.error(request, 'No se ha podido registrar el usuario')
            return render(request, 'registration/register.html')
        # Si llega aquí, es porque no hubo errores.
        messages.success(request, '¡Usuario creado con éxito! Por favor, ingrese')
        return redirect('login')

    def get(self, request):
        return render(request, 'registration/register.html')
    

# crear encuesta

def dashboard_view(request):
    return render(request, 'dashboard.html')

def crear_encuesta_view(request):
    if request.method == 'POST':
        
        return redirect('dashboard')
    return render(request, 'crear_encuesta.html')

def guardar_encuesta_view(request):
    if request.method == 'POST':
        nombre_encuesta = request.POST.get('nombre_encuesta')
        preguntas = request.POST.getlist('pregunta')
        # Guardar encuesta en la base de datos
        # ...
        messages.success(request, 'Encuesta creada exitosamente')
        return redirect('dashboard')
    return render(request, 'guardar_encuesta.html')