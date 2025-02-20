from django.core.management.base import BaseCommand
from radiovirgenBD.models import Usuario, Reproduccion, Podcast

class Command(BaseCommand):
    help = 'añadir podcast pendiente a un usuario'

    def add_arguments(self, parser):
        parser.add_argument('--nick',
                            type=str,
                            help='Nick del usuario',
                            required=True)
        parser.add_argument('--podcast_pendiente',
                            type=str,
                            help='nombre podcast',
                            required=False
                            )

    def handle(self, *args, **kwargs):
        podcast_pendiente = kwargs['podcast_pendiente']
        nick = kwargs['nick']

        try:

            podcast = Podcast.objects.get(titulo=podcast_pendiente)

            usuario = Usuario.objects.filter(nick=nick).first()

            if usuario.podcast_pendientes.filter(id=podcast.id).exists():
                self.stdout.write(self.style.ERROR(f'Error el podcast ya está en la lista del usuario'))
            else:
                usuario.podcast_pendientes.add(podcast)
                usuario.save()
                # usuario = Usuario.objects.set(podcast_pendientes = podcast_pendiente)
                self.stdout.write(self.style.SUCCESS(f'Podcast pendiente añadido a {usuario.nombre}'))

            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al añadir el podcast pendiente: {e}'))
