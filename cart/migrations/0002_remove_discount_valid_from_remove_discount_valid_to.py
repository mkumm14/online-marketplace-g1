# Generated by Django 4.2 on 2023-04-25 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='valid_from',
        ),
        migrations.RemoveField(
            model_name='discount',
            name='valid_to',
        ),
    ]
