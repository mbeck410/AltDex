from django.core.management.base import BaseCommand, CommandError
from ...helpers import rsi_calc, day_data

class Command(BaseCommand):


    def handle(self, *args, **options):
        self.my_test()


    def my_test(self):
        # print('Do you wish to delete all index prices?')
        # response = input('y or n?: ')
        # if response is 'y':
        while True:
            try:
                test = rsi_calc()
                print('Done')

            except:
                raise CommandError("Error")

        # else:
        #     return
