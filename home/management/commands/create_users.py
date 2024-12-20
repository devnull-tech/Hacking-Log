from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import secrets
import string

class Command(BaseCommand):
    help = 'Create sample users'

    def get_random_password(self) -> str:
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(32))
        return password

    def handle(self, *args, **options):
        users = [
            User(username="morfeo", 
                 password=self.get_random_password(), 
                 is_staff=True, 
                 is_superuser=True), 
            User(username="neo", 
                 password=self.get_random_password(), 
                 is_staff=True, 
                 is_superuser=True),
            User(username="tank", 
                 password=self.get_random_password(), 
                 is_staff=True, 
                 is_superuser=True),
            User(username="trinity", 
                 password=self.get_random_password(), 
                 is_staff=True, 
                 is_superuser=True),
        ]
        User.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS('Successfully created users'))