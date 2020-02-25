from helpers.director.shortcut import TablePage,ModelTable,ModelFields,director,page_dc,get_request_cache,director_view,RowFilter
from helpers.director.model_func.dictfy import sim_dict
from .models import CompanyInfo
from helpers.mobile.shortcut import ModelFieldsMobile

class CompanyInfoPage(TablePage):
    def get_label(self):
        return '公司信息'
    
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = CompanyInfo
        exclude =[]
        pop_edit_fields=['id']
        
        class filters(RowFilter):
            names = ['status']
        
        #def get_operation(self):
            #ops = super().get_operation()
            #ops += [
                #{'editor':'com-op-btn','label':'通过审核',}
            #]
            #return ops
        
class CompanyInfoForm(ModelFields):
    readonly = ['user']
    class Meta:
        model = CompanyInfo
        exclude =[]
    



class CompanyInfoBasic(ModelFieldsMobile):
    nolimit = True
    class Meta:
        model = CompanyInfo
        fields =['name','contact','address']
    
    def __init__(self, dc={}, pk=None, crt_user=None, *args, **kw):
        crt_user = get_request_cache()['request'].user
        cominfo ,_   = CompanyInfo.objects.get_or_create(user = crt_user)
        super(CompanyInfoBasic,self).__init__(dc,pk,crt_user,instance = cominfo,*args,**kw)
    
    def dict_head(self, head):
        if self.instance.status != 0:
            head['readonly'] = True
        return head
    
    def get_operations(self):
        if self.instance.status != 0:
            return []
        else:
            ops = super().get_operations()
            for op in ops:
                if op['name']  == 'save':
                    op['label'] = '保存'
            return ops
    
    #def clean_dict(self, inst):
        #if not inst.pk:
            #inst.user = self.crt_user

class CompanyInfoLicense(CompanyInfoBasic):
    class Meta:
        model = CompanyInfo
        fields =['license']
    
    def dict_head(self, head):
        if head['name'] =='license':
            head['maxspan'] = 1000
        if self.instance.status != 0:
            head['readonly'] = True
        return head

class CompanyInfoaccount_certificate(CompanyInfoBasic):
    class Meta:
        model = CompanyInfo
        fields =['account_certificate']
    
    def dict_head(self, head):
        if head['name'] =='account_certificate':
            head['maxspan'] = 1000
        if self.instance.status != 0:
            head['readonly'] = True
        return head
  
class CompanyInfo_qualification_certificate(CompanyInfoBasic):
    class Meta:
        model = CompanyInfo
        fields =['qualification_certificate']
    
    def dict_head(self, head):
        if head['name'] =='qualification_certificate':
            head['maxspan'] = 1000
        if self.instance.status != 0:
            head['readonly'] = True
        return head
  
@director_view('CompanyInfo/progress')
def get_companyInfo_cert_progress():
    user = get_request_cache()['request'].user
    info , _ = CompanyInfo.objects.get_or_create(user=user)
    return info.status

@director_view('CompanyInfo/submit_info')
def submit_info():
    user = get_request_cache()['request'].user
    info , _ = CompanyInfo.objects.get_or_create(user=user)
    if info.status !=0:
        raise UserWarning('认证信息不能提交审核')
    if not info.name or not info.contact:
        raise UserWarning('请完善基本信息后再提交审核')
    if not info.license:
        raise UserWarning('请上传营业执照后再提交审核')
    if not info.account_certificate:
        raise UserWarning('请上传开户许可证书后再提交审核')
    if not info.qualification_certificate:
        raise UserWarning('请上传资质证书后再提交审核')
    info.status = 1
    info.save()
    return info.status
    
  
   
director.update({
    'cominfo':CompanyInfoPage.tableCls,
    'cominfo.edit':CompanyInfoForm,
    'cominfo-basic':CompanyInfoBasic,
    'cominfo-license':CompanyInfoLicense,
    'cominfo-account_certificate':CompanyInfoaccount_certificate,
    'cominfo-qualification_certificate':CompanyInfo_qualification_certificate
})

page_dc.update({
    'cominfo':CompanyInfoPage,
})