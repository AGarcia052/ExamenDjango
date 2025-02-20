from django.core.management import BaseCommand
from radiovirgenBD.models import Categoria, Programa, Autor, Podcast, Usuario, Reproduccion


class Command(BaseCommand):
    help = "añade a lista de me gusta del usuario un podcast y mostrar su lista de me gusta"

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

        check_podcast = usuario.podcast_likes.filter(id=podcast.id).exists()

        if check_podcast:
            self.stdout.write(self.style.WARNING("\n\n****    El podcast ya esta en la lista de likes del usuario    ****"))

        else:

            try:
                usuario.podcast_likes.add(podcast)
                usuario.save()
                print("\n-------------------------------------------")
                self.stdout.write(
                    self.style.SUCCESS(f"Podcast {podcast.titulo} añadido a lista de favoritos del usuario {usuario.nick}"))
                print("-------------------------------------------")
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Error al añadir el podcast {podcast.titulo} a la lista de favoritos del usuario {usuario.nick}\n{e}"))

        podcast_like = usuario.podcast_likes.all()
        print("\nLista de podcast con likes del usuario:\n")
        for podcast in podcast_like:
            self.stdout.write(self.style.SUCCESS(str(podcast)), ending='\n')