# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-20 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='day',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='address',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]