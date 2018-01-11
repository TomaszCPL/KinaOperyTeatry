# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 12:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Nazwa')),
                ('lat', models.FloatField(blank=True)),
                ('long', models.FloatField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Shows',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128, verbose_name='Tytuł')),
                ('time', models.CharField(max_length=128, verbose_name='Czas')),
                ('date', models.CharField(max_length=128, verbose_name='Data')),
                ('place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='map.Place')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]