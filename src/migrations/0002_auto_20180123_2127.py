# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-23 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='MUNID',
            field=models.CharField(default='', help_text='This is the google docs jotform id thingy', max_length=20),
        ),
    ]