# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dc', '0005_ns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ns',
            name='imp_1',
            field=models.ImageField(upload_to='icons'),
        ),
    ]
