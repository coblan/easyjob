# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-02-18 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_auto_20200218_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='seekjobinfo',
            name='udpate_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
