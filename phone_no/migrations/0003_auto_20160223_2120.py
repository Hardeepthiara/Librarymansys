# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_no', '0002_remove_mno_des'),
    ]

    operations = [
        migrations.AddField(
            model_name='sep',
            name='facebook',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='sep',
            name='twitter',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]
