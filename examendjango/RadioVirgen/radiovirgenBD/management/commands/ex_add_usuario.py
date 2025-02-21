from django.core.management import BaseCommand
from django.db.models import DateField
from sqlalchemy import Select

from radiovirgenBD.models import Categoria, Programa, Autor, Podcast, Usuario, Reproduccion, PayPal, MetodoPago, Transferencia, PagoTarjeta
from random import randint, choice, random
from datetime import datetime, date

class Command(BaseCommand):
    help = 'Creación de datos de ejemplo de Radio Virgen'

    def handle(self, *args, **kwargs):
        try:
            nombre = "NOMBRE2"
            apellido = "APELLIDO2"
            nick = "NICKNAME2"
            email = "correo@correo.com"
            fecha_nacimiento = "2003-02-02"
            num_tarjeta = 851205215215125
            num_cuenta = 5027011421521
            cvc = 100



            paypal = PayPal.objects.create(correo_usuario=email)
            transferencia = Transferencia.objects.create(num_cuenta=num_cuenta, nombreTitular=nombre+" "+apellido)
            tarjeta = PagoTarjeta.objects.create(num_tarjeta=num_tarjeta, nombreTitular=nombre+" "+apellido,cvc=cvc)

            new_user = Usuario.objects.create(
                nombre=nombre,
                apellido=apellido,
                nick=nick,
                email=email,
                fecha_nacimiento=fecha_nacimiento,
                metodo_por_defecto="paypal"
            )

            MetodoPago.objects.create(
                usuario=new_user,
                pago_tarjeta=tarjeta,
                transferencia=transferencia,
                paypal=paypal
            )
            self.stdout.write(self.style.SUCCESS(f'USUARIO CREADO'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al crear los met. pago y usuario\n{e}'))



