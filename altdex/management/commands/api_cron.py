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


            except:
                sleep(60)
                try:
                    test2 = collect()

                except:
                    sleep(60)
                    try:
                        test3 = collect()

                    except:
                        raise CommandError("Error")









