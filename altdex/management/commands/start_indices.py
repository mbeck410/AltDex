from django.core.management.base import BaseCommand, CommandError
from ...helpers import collect, first_weight

class Command(BaseCommand):


    def handle(self, *args, **options):
        self.my_test()


    def my_test(self):
        print('Do you wish to delete all index prices?')
        response = input('y or n?: ')
        if response is 'y':
            try:
                print('Collecting...')
                test = collect()
                print('Setting prices...')
                test2 = first_weight()
                print('Done')

            except:
                raise CommandError("Error")

        else:
            return

        