from django.core.management.base import BaseCommand, CommandError
from ...helpers import collect
from time import sleep


class Command(BaseCommand):


    def handle(self, *args, **options):
        self.my_test()


    def my_test(self):
        try:
            test = collect()
            print('1')

        except:
            raise CommandError("Error")




    # def test(self):
    #     sleep(5)
    #     try:
    #         # test = collect()
    #         print('2')
    #
    #     except:
    #         raise CommandError("Error")





