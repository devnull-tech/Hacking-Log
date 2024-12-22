# Generated by Django 5.1.2 on 2024-12-22 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacklog', '0006_term_term'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=100)),
                ('system_prompt', models.CharField(max_length=200)),
                ('temperature', models.FloatField()),
                ('base_url', models.CharField(max_length=50)),
                ('api_key', models.CharField(max_length=200)),
                ('input_max_tokens', models.IntegerField()),
            ],
        ),
    ]
