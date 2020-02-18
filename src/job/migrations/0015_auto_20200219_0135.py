# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-02-19 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_auto_20200218_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobinfo',
            name='address',
            field=models.CharField(blank=True, max_length=400, verbose_name='上班地址'),
        ),
        migrations.AlterField(
            model_name='jobinfo',
            name='audit_status',
            field=models.IntegerField(choices=[(1, '编辑中'), (2, '审批中'), (3, '审批通过')], default=1, verbose_name='审批状态'),
        ),
        migrations.AlterField(
            model_name='seekjobinfo',
            name='audit_status',
            field=models.IntegerField(choices=[(1, '编辑中'), (2, '审批中'), (3, '审批通过')], default=1, verbose_name='审批状态'),
        ),
    ]
