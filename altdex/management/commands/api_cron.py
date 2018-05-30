from django.core.management.base import BaseCommand, CommandError
from ...helpers import collect
from time import sleep


class Command(BaseCommand):


    def handle(self, *args, **options):
        self.my_test()


    def my_test(self):
        while True:
            try:
                test = collect()
                # print(1)
                # sleep(5)
                # test2 = collect()
                # print('done')

            except:
                raise CommandError("Error")









