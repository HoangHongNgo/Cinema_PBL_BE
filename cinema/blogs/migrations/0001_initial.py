# Generated by Django 4.1.7 on 2023-04-18 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0006_alter_movie_casts_alter_movie_directors_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog/')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blogs.blog')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(blank=True, to='blogs.category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='movies',
            field=models.ManyToManyField(blank=True, to='movies.movie'),
        ),
    ]