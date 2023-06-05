# Generated by Django 4.1.7 on 2023-06-04 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '__first__'),
        ('casts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.IntegerField(default=0)),
                ('trailer_id', models.CharField(max_length=255)),
                ('rating', models.IntegerField()),
                ('release_date', models.DateField()),
                ('duration_minute', models.PositiveIntegerField()),
                ('age_limit', models.IntegerField()),
                ('cover_image', models.TextField()),
                ('banner_image', models.TextField()),
                ('casts', models.ManyToManyField(blank=True, related_name='casts', to='casts.cast')),
                ('directors', models.ManyToManyField(blank=True, related_name='directors', to='casts.cast')),
                ('tags', models.ManyToManyField(blank=True, to='tags.tag')),
            ],
        ),
    ]
