from django.core.management import BaseCommand
from radiovirgenBD.models import Categoria, Programa, Autor, Podcast, Usuario, Reproduccion


class Command(BaseCommand):
    help = "añade a lista de pendientes del usuario un podcast"

    def add_arguments(self, parser):
        parser.add_argument('--nick',
                            type=str,
                            help='nickname del usuario',
                            required=True
                            )
        parser.add_argument('--id_podcast',
                            type=int,
                            help='id del podcast',
                            required=True)

    def handle(self, *args, **options):

        podcast = Podcast.objects.get(id=options['id_podcast'])
        usuario = Usuario.objects.get(nick=options['nick'])

        check_podcast = usuario.podcast_pendientes.filter(id=podcast.id).exists()

        if check_podcast:
            self.stdout.write(self.style.WARNING("El podcast ya esta en la lista de pendientes del usuario"))
        else:
            try:
                usuario.podcast_pendientes.add(podcast)
                usuario.save()
                print("\n-------------------------------------------")
                self.stdout.write(
                    self.style.SUCCESS(f"Podcast {podcast.titulo} añadido a lista de pendientes del usuario {usuario.nick}"))
                print("-------------------------------------------")

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Error al añadir el podcast {podcast.titulo} a la lista de pendientes del usuario {usuario.nick}\n{e}"))

