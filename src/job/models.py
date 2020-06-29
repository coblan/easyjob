from django.db import models
from django.contrib.auth.models import User
from helpers.director.model_func.cus_fields.cus_picture import PictureField
from helpers.director.model_func.cus_fields.richtext import RichtextField
# Create your models here.

    

COM_INFO_STATUS=(
    (0,'编辑中'),
    (1,'审批中'),
    (2,'审批通过'),
)
class CompanyInfo(models.Model):
    user = models.OneToOneField(User,verbose_name = '账号')
    name = models.CharField('公司名称',max_length=200)
    contact = models.CharField('电话',max_length=200,)
    address = models.CharField('公司地址',max_length=400,blank=True)
    license = PictureField('营业执照',blank=True,max_length=300)
    account_certificate = PictureField('开户许可证书',blank=True,max_length=300)
    
    opening_bank = models.CharField('开户行',blank=True,max_length = 400)
    bank_code = models.CharField('银行账号',blank=True,max_length=300)
    website = models.CharField('网站',blank=True, max_length=400)
    
    qualification_certificate = PictureField('资质证书',blank=True,max_length=300)
    update_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)
    status = models.IntegerField(verbose_name='当前状态',choices=COM_INFO_STATUS,default=0)
    
    def __str__(self):
        return self.name
    
    
    
INFO_STATUS=(
    (0,'离线'),
    (1,'在线'),
    #(2,'离线')
)

AUDIT_STATUS=(
    (1,'编辑中'),
    (2,'审批中'),
    (3,'审批通过'),
)

class JobInfo(models.Model):
    com = models.ForeignKey(CompanyInfo,verbose_name='发布商家',blank=True,null=True)
    #title = models.CharField('标题',max_length=100)
    position = models.CharField('职位',max_length=100)
    #com_name = models.CharField('公司名称',max_length=200)
    address = models.CharField('上班地址',max_length=400,blank=True)
    pay= models.CharField('薪酬待遇',max_length=100,blank=True)
    require_time = models.CharField('要求时间',max_length=100,blank=True)
    key_words = models.CharField('关键字',max_length=30,default='',help_text='最多不超过30个字')
    #contact = models.CharField('联系方式',max_length=200,)
    update_time = models.DateTimeField('更新时间',auto_now_add=True)
    detail = models.TextField('详细介绍',blank=True)
    #publisher = models.ForeignKey(User,)
    plat_contract = PictureField('服务合同',max_length=300,blank=True,help_text='请在[资料下载]中下载模板')
    contract = PictureField('合同',max_length=300,blank=True)
    bid = PictureField('中标书',max_length=300,blank=True)
    status = models.IntegerField('在线状态',choices=INFO_STATUS,default=1)
    audit_status = models.IntegerField('审批状态',choices=AUDIT_STATUS,default=1)
    
    def __str__(self):
        return self.position


class WorkInfo(models.Model):
    user = models.OneToOneField(User,verbose_name = '账号')
    name = models.CharField('姓名',max_length=200,blank=True)
    contact = models.CharField('电话',max_length=200,blank=True)
    address = models.CharField('地址',max_length=400,blank=True)
    head = PictureField('头像',blank=True,max_length = 300,help_text='2寸标准证件照')
    id_face1 = PictureField('身份证正面',blank=True,max_length=300)
    id_face2 = PictureField('身份证反面',blank=True,max_length=300)
    bank_cover = PictureField('银行卡正面', blank=True ,max_length =300)
    bank_code = models.CharField('卡号',blank=True,max_length=300)
    opening_bank = models.CharField('开户行',blank=True,max_length = 400)
    
    education = PictureField('学历证明',blank=True,max_length=300)
    vocational_certificate = PictureField('职业证书',blank=True,max_length=300)
    skills_certificate = PictureField('技能证书',blank=True,max_length=300)
    #service_agreement = PictureField('自由职业者服务协议',blank=True,max_length=300)

    update_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)
    status = models.IntegerField(verbose_name='当前状态',choices=COM_INFO_STATUS,default=0)
    
    def __str__(self):
        return self.name


class SeekJobInfo(models.Model):
    worker = models.ForeignKey(WorkInfo,verbose_name='求职者')
    salary = models.CharField('薪资要求',max_length = 200,blank=True)
    jobtime = models.CharField('可以上班时间',max_length = 200,blank=True)
    key_words = models.CharField('关键字',max_length=30,help_text='最多不超过30个字')
    desp = models.TextField('详细描述')
    status = models.IntegerField('在线状态',choices=INFO_STATUS,default=1)
    audit_status = models.IntegerField('审批状态',choices=AUDIT_STATUS,default=1)
    update_time = models.DateTimeField(verbose_name='更新时间',auto_now= True)
    
    def __str__(self):
        return self.key_words
    
    
class MyHelp(models.Model):
    title = models.CharField('标题',max_length=300)
    content = RichtextField('内容',)
    
    def __str__(self):
        return self.title

APPLY_STATUS= (
    (0,'待商户查看'),
    (1,'接受申请/待平台审批'),
    (3,'平台审批通过'),
    (4,'商户确定工作完成'),
    (5,'平台已结算'),
    
    (2,'拒绝申请'),
    (101,'平台审批不通过'),
)

class ApplyRecord(models.Model):
    worker = models.ForeignKey(WorkInfo,verbose_name='求职者')
    job = models.ForeignKey(JobInfo,verbose_name='申请职位')
    status = models.IntegerField(verbose_name='状态',choices=APPLY_STATUS,default=0)
    updatetime = models.DateTimeField(verbose_name='更新时间',auto_now=True)
    createtime = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    
    def __str__(self):
        return self.job.position + ' 申请'