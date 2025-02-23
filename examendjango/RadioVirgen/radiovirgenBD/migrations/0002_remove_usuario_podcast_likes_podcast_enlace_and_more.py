# Generated by Django 5.1.4 on 2025-01-30 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radiovirgenBD', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='podcast_likes',
        ),
        migrations.AddField(
            model_name='podcast',
            name='enlace',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='programa',
            name='autor',
            field=models.ManyToManyField(to='radiovirgenBD.autor'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='duracion',
            field=models.CharField(max_length=100),
        ),
    ]
