# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-28 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20170727_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='yields',
            field=models.IntegerField(default='1'),
        ),
    ]