from django.contrib import admin
from .models import Editorial, Autor, Libro, AutorCapitulo, LibroCronica

admin.site.register(Editorial)
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(AutorCapitulo)
admin.site.register(LibroCronica)


