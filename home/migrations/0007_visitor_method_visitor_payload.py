# Generated by Django 5.1.2 on 2024-12-20 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_visitor_city_visitor_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='method',
            field=models.TextField(default='GET'),
        ),
        migrations.AddField(
            model_name='visitor',
            name='payload',
            field=models.TextField(default=''),
        ),
    ]
