from django.db import models
from django.contrib.auth.models import User
from helpers.director.model_func.cus_fields.cus_picture import PictureField
# Create your models here.
INFO_STATUS=(
    (1,'在线'),
    (2,'离线'),
)

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
    status = models.IntegerField('状态',choices=INFO_STATUS,default=1)
    

COM_INFO_STATUS=(
    (0,'编辑中'),
    (1,'审批中'),
    (2,'审批通过'),
)
class CompanyInfo(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField('公司名称',max_length=200)
    contact = models.CharField('联系方式',max_length=200,)
    address = models.CharField('地址',max_length=400,blank=True)
    license = PictureField('营业执照',blank=True,max_length=300)
    account_certificate = PictureField('开户许可证书',blank=True,max_length=300)
    qualification_certificate = PictureField('资质证书',blank=True,max_length=300)
    update_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)
    status = models.IntegerField(verbose_name='当前状态',choices=COM_INFO_STATUS,default=0)
    