from django.contrib import admin
from main.models import User

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)



admin.site.site_header = "****Encuestas****"
admin.site.index_title = "Bienvenidos al portal de administración de Encuestas"