from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class JobInfo(models.Model):
    #title = models.CharField('标题',max_length=100)
    position = models.CharField('职位',max_length=100)
    com_name = models.CharField('公司名称',max_length=200)
    address = models.CharField('地址',max_length=400,blank=True)
    pay= models.CharField('薪酬待遇',max_length=100,blank=True)
    require_time = models.CharField('要求时间',max_length=100,blank=True)
    contact = models.CharField('联系方式',max_length=200,)
    update_time = models.DateTimeField('更新时间',auto_now_add=True)
    detail = models.TextField('详细介绍',blank=True)
    publisher = models.ForeignKey(User,)
    