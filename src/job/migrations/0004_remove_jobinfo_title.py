# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-12-30 15:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_jobinfo_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobinfo',
            name='title',
        ),
    ]
