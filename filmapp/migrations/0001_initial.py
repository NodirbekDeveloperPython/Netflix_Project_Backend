# Generated by Django 4.1.3 on 2022-11-13 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aktyor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(blank=True, max_length=50)),
                ('davlat', models.CharField(blank=True, max_length=30)),
                ('jins', models.CharField(blank=True, max_length=5)),
                ('tugulgan_yil', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=50)),
                ('janr', models.CharField(blank=True, max_length=50)),
                ('yil', models.DateField(null=True)),
                ('reyting', models.FloatField(null=True)),
                ('aktyorlar', models.ManyToManyField(blank=True, to='filmapp.aktyor')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=30)),
                ('sana', models.DateTimeField(auto_now_add=True, null=True)),
                ('kino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filmapp.kino')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
