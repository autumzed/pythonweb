# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-21 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dc', '0007_auto_20171025_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ns',
            name='imp_1',
            field=models.ImageField(upload_to='media/upto'),
        ),
    ]
