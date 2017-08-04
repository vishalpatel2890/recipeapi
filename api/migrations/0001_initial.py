# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-04 19:13
from __future__ import unicode_literals

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
            name='Ingredients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ingredient', models.CharField(default='flour', max_length=50)),
                ('quantity', models.FloatField(default='100')),
                ('measuresize', models.CharField(choices=[('PNCH', 'PINCH'), ('TSP', 'TSP'), ('TBSP', 'TBSP'), ('CUP', 'CUP'), ('PINT', 'PINT'), ('QT', 'QUART'), ('GAL', 'GALLON'), ('G', 'GRAM'), ('KG', 'KILOGRAM'), ('OZ', 'OUNCE'), ('FLOZ', 'FLUID OUNCE')], default='TBSP', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('recipename', models.CharField(default='Enter A Recipe Name', max_length=50)),
                ('yields', models.IntegerField(default='1')),
                ('portionsize', models.CharField(default='Enter Portion Size', max_length=50)),
                ('dateadded', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(default='static/about-black-1240x600.jpg', upload_to='recipes')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stepno', models.IntegerField()),
                ('steps', models.TextField()),
                ('step_image', models.ImageField(default='static/about-black-1240x600.jpg', upload_to='')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Recipes')),
            ],
        ),
        migrations.AddField(
            model_name='ingredients',
            name='recipe',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='api.Recipes'),
        ),
        migrations.AlterUniqueTogether(
            name='steps',
            unique_together=set([('recipe', 'stepno')]),
        ),
    ]
