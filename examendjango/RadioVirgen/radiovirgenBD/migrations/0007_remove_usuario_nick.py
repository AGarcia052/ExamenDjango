# Generated by Django 5.1.4 on 2025-02-01 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radiovirgenBD', '0006_usuario_nick'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='nick',
        ),
    ]
