# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-30 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0008_auto_20180129_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruitvote',
            name='InitDate',
            field=models.DateTimeField(auto_now=True, help_text='Date and time of creation'),
        ),
        migrations.AlterField(
            model_name='speakercountry',
            name='voteEndTime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
