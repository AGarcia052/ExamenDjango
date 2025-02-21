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
        parser.add_argument('--metodo_pago',
                            type=str,
                            help='metodos de pago: PayPal,Tarjeta,Transferencia',
                            required=True
                            )
    def handle(self, *args, **kwargs):
        try:
            idobt = kwargs['id_usuario']
            metodo_selecc = str(kwargs['metodo_pago']).lower()
            usuario = Usuario.objects.get(id=idobt)

            if metodo_selecc == "paypal" or metodo_selecc == "tarjeta" or metodo_selecc == "transferencia":

                if metodo_selecc == usuario.metodo_por_defecto.lower():
                    self.stdout.write(
                        self.style.WARNING(f'{metodo_selecc} ya es el pago por defecto del usuario'))
                else:
                    usuario.metodo_por_defecto = metodo_selecc
                    usuario.save()
                    self.stdout.write(self.style.SUCCESS(f'Metodo de pago por defecto cambiado a: {metodo_selecc}'))

            else:
                self.stdout.write(self.style.ERROR(f'Introduce uno metodo de pago válido: PayPal,Tarjeta,Transferencia'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'ERROR AL CAMBIAR METODO DE PAGO: \n{e}'))



