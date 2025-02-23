# Generated by Django 5.1.4 on 2025-01-31 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radiovirgenBD', '0004_programa_podcast'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reproduccion',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='podcast_lista_escuchar',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='podcast_seguido',
        ),
        migrations.AddField(
            model_name='usuario',
            name='podcast_likes',
            field=models.ManyToManyField(related_name='usu_podcast_like', to='radiovirgenBD.podcast'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='podcast_pendientes',
            field=models.ManyToManyField(related_name='podcast_pendientes', to='radiovirgenBD.podcast'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='programa_seguido',
            field=models.ManyToManyField(related_name='prog_seguido', to='radiovirgenBD.programa'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='programas_likes',
            field=models.ManyToManyField(related_name='usu_programas_like', to='radiovirgenBD.programa'),
        ),
    ]
