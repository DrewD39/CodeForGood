# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-13 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataTables', '0002_erg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='erg',
            name='post_date',
            field=models.CharField(max_length=50),
        ),
    ]