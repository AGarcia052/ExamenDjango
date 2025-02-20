from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre



class Podcast(models.Model):
    titulo = models.CharField(max_length=100)
    duracion = models.IntegerField()
    fecha_publicacion = models.DateField(null=True, blank=True)
    autor = models.ManyToManyField(Autor)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    enlace = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.titulo


class Programa(models.Model):
    nombre = models.CharField(max_length=50)
    autor = models.ManyToManyField(Autor)
    podcast = models.ManyToManyField(Podcast)
    def __str__(self):
        return self.nombre
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nick = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    programa_seguido = models.ManyToManyField(Programa, related_name="prog_seguido", blank=True)
    podcast_pendientes = models.ManyToManyField(Podcast, related_name="podcast_pendientes", blank=True)
    podcast_likes = models.ManyToManyField(Podcast, related_name="usu_podcast_like", blank=True)
    programas_likes = models.ManyToManyField(Programa, related_name="usu_programas_like", blank=True)
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"



class Reproduccion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    fecha_reproduccion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("usuario", "podcast","fecha_reproduccion")