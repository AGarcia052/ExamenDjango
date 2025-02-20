from django.contrib import admin
from .models import Categoria, Programa, Autor, Podcast, Usuario, Reproduccion

class UsuarioAdmin(admin.ModelAdmin):
    filter_horizontal = ("programa_seguido", "podcast_pendientes", "podcast_likes", "programas_likes")

# Registrar modelos
admin.site.register(Categoria)
admin.site.register(Programa)
admin.site.register(Autor)
admin.site.register(Podcast)
admin.site.register(Reproduccion)

# Registrar Usuario con UsuarioAdmin
admin.site.register(Usuario, UsuarioAdmin)
