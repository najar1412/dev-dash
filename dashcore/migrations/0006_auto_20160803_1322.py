# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 20:22
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashcore', '0005_asset_collect_asset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='collect_asset',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, size=None),
        ),
    ]
