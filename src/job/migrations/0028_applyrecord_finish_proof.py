# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-07-17 23:45
from __future__ import unicode_literals

from django.db import migrations
import helpers.director.model_func.cus_fields.cus_picture


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0027_auto_20200717_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyrecord',
            name='finish_proof',
            field=helpers.director.model_func.cus_fields.cus_picture.PictureField(blank=True, max_length=200, verbose_name='完结拍照'),
        ),
    ]