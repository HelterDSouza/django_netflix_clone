# Generated by Django 4.0.1 on 2022-01-21 19:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('identifier', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Seasonal'), (2, 'Single')])),
                ('flyer', models.ImageField(blank=True, null=True, upload_to='flyers')),
                ('maturity_rating', models.PositiveSmallIntegerField(choices=[(1, 'L'), (2, '10'), (3, '12'), (4, '14'), (5, '16'), (6, '18')], verbose_name='maturity rating')),
                ('kid_profile', models.BooleanField(blank=True, default=False, verbose_name="Kid's movie")),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('file', models.FileField(upload_to='movies')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
