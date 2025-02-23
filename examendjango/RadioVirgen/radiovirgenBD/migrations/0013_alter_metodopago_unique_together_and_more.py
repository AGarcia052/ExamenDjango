# Generated by Django 5.1.4 on 2025-02-21 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radiovirgenBD', '0012_rename_num_tarjeta_transferencia_num_cuenta'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='metodopago',
            unique_together={('usuario', 'transferencia', 'paypal', 'pago_tarjeta')},
        ),
        migrations.AlterUniqueTogether(
            name='pagotarjeta',
            unique_together={('num_tarjeta', 'cvc', 'nombreTitular')},
        ),
        migrations.AlterUniqueTogether(
            name='transferencia',
            unique_together={('num_cuenta', 'nombreTitular')},
        ),
    ]
