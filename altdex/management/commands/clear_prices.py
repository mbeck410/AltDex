from django.core.management.base import BaseCommand, CommandError
from ...helpers import clear_price


class Command(BaseCommand):


    def handle(self, *args, **options):
        self.my_test()


    def my_test(self):
        while True:
            print('Do you wish to delete all index prices?')
            response = input('y or n?: ')
            if response is 'y':
                try:
                    test = clear_price()
                except:
                    raise CommandError("Error")

            else:
                return


