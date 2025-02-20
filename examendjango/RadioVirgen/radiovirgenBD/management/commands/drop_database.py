from django.core.management import BaseCommand
from radiovirgenBD.models import Categoria, Programa, Autor, Podcast, Usuario, Reproduccion
from django.db import connection
class Command(BaseCommand):
    help = "Borrado"

    def handle(self, *args, **options):
        try:

            Categoria.objects.all().delete()
            Programa.objects.all().delete()
            Autor.objects.all().delete()
            Podcast.objects.all().delete()
            Usuario.objects.all().delete()
            Reproduccion.objects.all().delete()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM sqlite_sequence WHERE name='radiovirgenBD_categoria';")
                cursor.execute("DELETE FROM sqlite_sequence WHERE name='radiovirgenBD_programa';")
                cursor.execute("DELETE FROM sqlite_sequence WHERE name='radiovirgenBD_autor';")
                cursor.execute("DELETE FROM sqlite_sequence WHERE name='radiovirgenBD_podcast';")
                cursor.execute("DELETE FROM sqlite_sequence WHERE name='radiovirgenBD_usuario';")
                cursor.execute("DELETE FROM sqlite_sequence WHERE name='radiovirgenBD_reproduccion';")

            self.stdout.write(self.style.SUCCESS(f"Base de datos vaciada"))

        except Exception as e:

            self.stdout.write(self.style.ERROR(f"Error al borrar la base de datos\n{e}"))
