# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-19 04:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('start_date', models.DateTimeField(blank=True)),
                ('end_date', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('latitude', models.CharField(blank=True, max_length=100)),
                ('longitude', models.CharField(blank=True, max_length=100)),
                ('size', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(blank=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_url', models.CharField(blank=True, max_length=1000)),
                ('unit_value', models.CharField(blank=True, max_length=100)),
                ('unit_name', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('farm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Farm')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificado', models.BooleanField(default=False)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True)),
                ('state', models.CharField(blank=True, max_length=10)),
                ('session', models.CharField(blank=True, max_length=50, null=True)),
                ('create_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('basket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Basket')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'ShoppingItem',
                'verbose_name_plural': 'ShoppingItems',
            },
        ),
        migrations.AddField(
            model_name='farm',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Provider'),
        ),
    ]
