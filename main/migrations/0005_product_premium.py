# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-12 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_provider_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='premium',
            field=models.BooleanField(default=False),
        ),
    ]