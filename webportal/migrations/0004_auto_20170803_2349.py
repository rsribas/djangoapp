# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-03 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webportal', '0003_auto_20170803_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='user',
        ),
        migrations.AlterField(
            model_name='module',
            name='builtin',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1),
        ),
    ]