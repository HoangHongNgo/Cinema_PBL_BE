# Generated by Django 4.1.7 on 2023-04-23 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='description',
        ),
    ]
