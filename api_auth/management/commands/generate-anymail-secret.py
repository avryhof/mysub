from django.core.management import BaseCommand
from django.utils import crypto


class Command(BaseCommand):
    def handle(self, *args, **options):
        print(':'.join(crypto.get_random_string(16) for _ in range(2)))
