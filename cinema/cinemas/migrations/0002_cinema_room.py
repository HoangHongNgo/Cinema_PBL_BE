# Generated by Django 4.1.7 on 2023-04-05 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinemas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema_Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cinema', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinemas.cinema')),
            ],
        ),
    ]