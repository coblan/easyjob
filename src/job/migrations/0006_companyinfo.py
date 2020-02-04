# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-02-02 20:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import helpers.director.model_func.cus_fields.cus_picture


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0005_jobinfo_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='公司名称')),
                ('contact', models.CharField(max_length=200, verbose_name='联系方式')),
                ('address', models.CharField(blank=True, max_length=400, verbose_name='地址')),
                ('license', helpers.director.model_func.cus_fields.cus_picture.PictureField(blank=True, max_length=300, verbose_name='营业执照')),
                ('account_certificate', helpers.director.model_func.cus_fields.cus_picture.PictureField(blank=True, max_length=300, verbose_name='开户许可证书')),
                ('qualification_certificate', helpers.director.model_func.cus_fields.cus_picture.PictureField(blank=True, max_length=300, verbose_name='资质证书')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('status', models.IntegerField(choices=[(0, '未审批'), (1, '审批中'), (2, '审批通过')], default=0, verbose_name='当前状态')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]