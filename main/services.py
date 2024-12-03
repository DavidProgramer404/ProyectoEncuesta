from django.contrib.auth.models import User
from main.models import User

def crear_usuario(username:str, first_name:str, last_name:str, email:str, password:str) -> bool:
    user = User.objects.create_user(
        username,
        email,
        password,
        first_name=first_name,
        last_name=last_name
        )
    User.objects.create(
        tipo='cliente', 
        user=user
        )
    return True