# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 02:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170424_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournamentdefinition',
            name='name',
        ),
    ]