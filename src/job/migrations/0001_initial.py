# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-12-28 15:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('position', models.CharField(max_length=100, verbose_name='职位')),
                ('address', models.CharField(blank=True, max_length=400, verbose_name='地址')),
                ('pay', models.CharField(blank=True, max_length=100, verbose_name='薪酬待遇')),
                ('require_time', models.CharField(blank=True, max_length=100, verbose_name='要求时间')),
                ('contact', models.CharField(max_length=200, verbose_name='联系方式')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
