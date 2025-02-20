from django.core.management import BaseCommand

from radiovirgenBD.models import Categoria, Programa, Autor, Podcast, Usuario, Reproduccion
from random import randint, choice, random
from datetime import datetime, date



class Command(BaseCommand):
    help = 'Obtener datos sobre todos usuarios'

    def handle(self, *args, **kwargs):

        try:

            usuarios = Usuario.objects.all()

            for usuario in usuarios:
                mensaje = (
                    f"ID: {usuario.id}\n"
                    f"Nombre: {usuario.nombre}\n"
                    f"Apellidos: {usuario.apellido}\n"
                    f"Nick : {usuario.nick}\n"
                    "----------------------------------------------\n"
                )
                self.stdout.write(self.style.SUCCESS(mensaje))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al listar los usuarios:\n{e}'))