# Generated by Django 5.1.2 on 2024-12-20 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tool',
            old_name='zip_url',
            new_name='releases_url',
        ),
    ]
