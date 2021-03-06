# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-06-09 23:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0020_auto_20200526_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, '申请'), (1, '同意'), (2, '完结')], verbose_name='状态')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.CompanyInfo', verbose_name='用人单位')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.WorkInfo', verbose_name='求职者')),
            ],
        ),
    ]
