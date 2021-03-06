# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-05-26 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0019_auto_20200526_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='bank_code',
            field=models.CharField(blank=True, max_length=300, verbose_name='银行账号'),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='opening_bank',
            field=models.CharField(blank=True, max_length=400, verbose_name='开户行'),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='website',
            field=models.CharField(blank=True, max_length=400, verbose_name='网站'),
        ),
    ]
