# Generated by Django 5.1.2 on 2024-10-23 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='layout',
            name='in_use',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
