# Generated by Django 5.1.2 on 2024-12-22 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacklog', '0007_bot'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='in_use',
            field=models.BooleanField(default=False),
        ),
    ]