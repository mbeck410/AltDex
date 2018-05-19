from django.core.management.base import BaseCommand, CommandError
from ...helpers import collect

class Command(BaseCommand):


    def handle(self, *args, **options):
        self.my_test()


    def my_test(self):
        try:
            test = collect()
            print('Hey guvna')

        except:
            raise CommandError("Error")


