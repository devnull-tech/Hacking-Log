# Generated by Django 5.1.2 on 2024-12-20 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacklog', '0005_term'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='term',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]