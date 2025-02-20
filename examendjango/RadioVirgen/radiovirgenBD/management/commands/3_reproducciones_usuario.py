from django.core.management.base import BaseCommand
from radiovirgenBD.models import Usuario, Reproduccion

class Command(BaseCommand):
    help = 'lista de reproducciones de un usuario'

    def add_arguments(self, parser):
        parser.add_argument('--nick',
                            type=str,
                            help='nickname del usuario'
                            )


    def handle(self, *args, **kwargs):
        nick = kwargs['nick']

        if not nick:
            self.stdout.write(self.style.ERROR('Se debe proporcionar el nick del usuario --nick'))
            return

        # comando para listar las reproducciones de un usuario
        try:
            usuario = Usuario.objects.get(nick=nick)
            reproducciones = Reproduccion.objects.filter(usuario=usuario)

            if reproducciones:
                for reproduccion in Reproduccion.objects.filter(usuario=usuario):
                    self.stdout.write(
                        f'Podcast: {reproduccion.podcast.titulo}, fecha: {reproduccion.fecha_reproduccion}')
            else:
                self.stdout.write(self.style.WARNING(f'El usuario {nick} no tiene reproducciones'))


        except Usuario.DoesNotExist:
            self.stdout.write(self.style.ERROR('el usuario NO existe'))