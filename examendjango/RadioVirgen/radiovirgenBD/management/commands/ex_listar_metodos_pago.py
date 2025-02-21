from django.core.management import BaseCommand
from django.db.models import DateField
from radiovirgenBD.models import Categoria, Programa, Autor, Podcast, Usuario, Reproduccion, PayPal, MetodoPago, Transferencia, PagoTarjeta
from sqlalchemy import Select



class Command(BaseCommand):
    help = 'listar metodos de pago'

    def add_arguments(self, parser):
        parser.add_argument('--id_usuario',
                            type=int,
                            help='id del usuario',
                            required=True
                            )
    def handle(self, *args, **kwargs):
        idobt = kwargs['id_usuario']

        usuario = Usuario.objects.get(id=idobt)
        try:

            metodos_pago = MetodoPago.objects.get(usuario=usuario)
            if metodos_pago:
                self.stdout.write(self.style.SUCCESS(f'Métodos de pago de {usuario}:\n'))
                if metodos_pago.paypal:
                    self.stdout.write(self.style.SUCCESS(f'Paypal: {metodos_pago.paypal}:\n'))
                if metodos_pago.pago_tarjeta:
                    self.stdout.write(self.style.SUCCESS(f'Tarjeta: {metodos_pago.pago_tarjeta}:\n'))
                if metodos_pago.transferencia:
                    self.stdout.write(self.style.SUCCESS(f'Transferencia: {metodos_pago.transferencia}:\n'))
            else:
                self.stdout.write(self.style.WARNING(f'{usuario} no tiene metodos de pago'))



        except Exception as e:
            self.stdout.write(self.style.WARNING(f'{usuario} no tiene metodos de pago'))



