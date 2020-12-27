from django.contrib import admin
from .models import Categoria, Contact

# Register your models here.
# python manage.py createsuperuser

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')
    #list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    list_editable = ('telefone', 'mostrar')

admin.site.register(Categoria)
admin.site.register(Contact, ContactAdmin)


