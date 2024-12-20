from django.core.management.base import BaseCommand
from home.models import Visitor

class Command(BaseCommand):
    help = 'Clear all Visitor records'

    def handle(self, *args, **kwargs):
        Visitor.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared all Visitor records.'))
