# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-31 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0009_auto_20180130_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speakercountry',
            name='country',
            field=models.CharField(help_text='Name of the conutry speaking right here', max_length=45),
        ),
    ]