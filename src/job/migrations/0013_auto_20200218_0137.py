# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-02-18 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_seekjobinfo_udpate_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seekjobinfo',
            name='desp',
            field=models.TextField(verbose_name='详细描述'),
        ),
        migrations.AlterField(
            model_name='seekjobinfo',
            name='key_words',
            field=models.CharField(help_text='最多不超过30个字', max_length=30, verbose_name='关键字'),
        ),
    ]