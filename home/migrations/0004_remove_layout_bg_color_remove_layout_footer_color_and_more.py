# Generated by Django 5.1.2 on 2024-12-20 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_layout_contact_html_layout_home_html'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='layout',
            name='bg_color',
        ),
        migrations.RemoveField(
            model_name='layout',
            name='footer_color',
        ),
        migrations.RemoveField(
            model_name='layout',
            name='navbar_color',
        ),
        migrations.RemoveField(
            model_name='layout',
            name='text_color',
        ),
    ]
