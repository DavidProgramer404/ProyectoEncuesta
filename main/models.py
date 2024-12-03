from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=16)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Encuesta(models.Model):
    nombre = models.CharField(max_length=255)
    premio = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Pregunta(models.Model):
    texto = models.CharField(max_length=255)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto

class Respuesta(models.Model):
    valor = models.IntegerField()
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)

    def __str__(self):
        return f'Respuesta {self.valor} a {self.pregunta}'
    

class Contact(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    mensaje = models.TextField(max_length=1000)

    
    def __str__(self):
        return f'Contacto de {self.nombre}'
    