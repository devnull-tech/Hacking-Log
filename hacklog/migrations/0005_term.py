# Generated by Django 5.1.2 on 2024-12-20 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacklog', '0004_log_is_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
    ]