from django.core.management.base import BaseCommand, CommandError
from ...helpers import collect

from crontab import CronTab

class Command(BaseCommand):
    help = 'Cron testing'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        #init cron
        cron = CronTab(user='your_username')

        #add new cron job
        job = cron.new(command='python <path_to>/example.py >>/tmp/out.txt 2>&1')

        #job settings
        job.minute.every(1)

        cron.write()

# class Command(BaseCommand):
#
#
#     def handle(self, *args, **options):
#         self.my_test()
#
#
#     def my_test(self):
#         try:
#             test = collect()
#             print('Hey guvna')
#
#         except:
#             raise CommandError("Error")


