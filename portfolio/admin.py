from django.contrib import admin
from .models import Project

#Aqui podemos añadir un modelo(models.py), en este caso 'Project' para ser mostrado en la pagina de admin de Django 
admin.site.register(Project) 
