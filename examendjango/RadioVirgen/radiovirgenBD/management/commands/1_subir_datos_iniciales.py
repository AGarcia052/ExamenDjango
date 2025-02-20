from django.core.management import BaseCommand

from radiovirgenBD.models import Categoria, Programa, Autor, Podcast, Usuario, Reproduccion
from random import randint, choice, random
from datetime import datetime, date
from faker import Faker


#40 personas con el siguiente formato:nombreX, apellidoX edad: número comprendido entre 1 y 65 (random)

class Command(BaseCommand):
    help = 'Creación de datos de ejemplo de Radio Virgen'

    def handle(self, *args, **kwargs):

        fake = Faker()

        # ------------------------------ Creación de categorías ------------------------------


        if not Categoria.objects.exists():

            try:

                for i in range(1,10):
                    categoria = Categoria.objects.create(nombre=fake.word())
                    self.stdout.write(self.style.SUCCESS(f'Categoría creada: {categoria.nombre}'))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error al crear las categorias\n{e}'))

        else:
            self.stdout.write(self.style.WARNING('Ya existen categorias'))
        # ------------------------------ Creación de programas Y Autores ------------------------------
        if not Programa.objects.exists():

            try:

                for i in range(1,10):
                    programa = Programa.objects.create(nombre=fake.word())

                    max_autores = randint(1, 5)

                    for i in range(1, max_autores):
                        autor = Autor.objects.create(nombre=fake.word())
                        programa.autor.add(autor)
                        self.stdout.write(self.style.SUCCESS(f'Autor creado: {autor.nombre}'))

                    self.stdout.write(self.style.SUCCESS(f'Programa creado: {programa.nombre} con {max_autores} números de autores'))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error al crear los programas\n{e}'))

        else:
            self.stdout.write(self.style.WARNING('Ya existen programas'))

        # ------------------------------ Creación de Podcast ------------------------------

        if not Podcast.objects.exists():

            try:

                listaProgramas = list(Programa.objects.all())
                listaCategorias = list(Categoria.objects.all())

                autoresDisponibles = list(programa.autor.all()) # una lista temporal de autores

                for programa in listaProgramas:

                    for i in range(1, 30): # para crear los 30 PODCAST

                        titulo = fake.sentence(nb_words=10)  # Título con 10 palabras
                        duracion = fake.random_int(min=10, max=300)  # Duración entre 10 y 300 minutos
                        fecha_publicacion = fake.date_this_decade()  # Fecha aleatoria de los últimos 10 años

                        numAutoresRandom = randint(1, 5)

                        listaAutores = []

                        for i in range(numAutoresRandom): # crea el número de autores perteneciente a ese podcast
                            if autoresDisponibles:
                                autor = choice(autoresDisponibles)
                                autoresDisponibles.remove(autor)

                                listaAutores.append(autor)

                        categoria = choice(listaCategorias)

                        podcast = Podcast.objects.create(titulo=titulo,
                                                         duracion=duracion,
                                                         fecha_publicacion=fecha_publicacion,
                                                         categoria=categoria,
                                                         enlace = f'www.dirve{i}.com/{programa.nombre}/podcast{i}.mp3')

                        podcast.autor.set(listaAutores)

                    self.stdout.write(self.style.SUCCESS(f'Creado podcast {titulo}'))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error al crear los podcast\n{e}'))
        else:
            self.stdout.write(self.style.WARNING('Ya existen Podcast'))
            # ------------------------------ Creación de Usuario ------------------------------

        if not Usuario.objects.exists():

            num_reproducciones = randint(20,70)

            try:

                for i in range(10):
                    nombre = fake.first_name()
                    apellido = fake.last_name()
                    nick = fake.user_name() + str(i)  # Genera un nombre de usuario único (apellido + número)
                    email = fake.email()
                    fecha_nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=80)

                    Usuario.objects.create(
                        nombre=nombre,
                        apellido=apellido,
                        nick=nick,
                        email=email,
                        fecha_nacimiento=fecha_nacimiento)

                    self.stdout.write(self.style.SUCCESS(f'Usuario creado: {nombre} {apellido}'))

                usuarios = Usuario.objects.all()
                podcast = Podcast.objects.all()

                for i in range(1,num_reproducciones):
                    Reproduccion.objects.create(usuario=choice(usuarios),
                                                podcast=choice(podcast),
                                                fecha_reproduccion=fake.date())
                    self.stdout.write(self.style.SUCCESS(f'Reproduccion creada.'))


            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error al crear los usuarios\n{e}'))

        else:
            self.stdout.write(self.style.WARNING('Ya existen usuarios'))