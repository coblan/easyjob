from helpers.director.shortcut import TablePage,ModelTable,ModelFields,page_dc,director,get_request_cache,director_view,RowFilter
from job . models import WorkInfo
from helpers.mobile.shortcut import ModelFieldsMobile
from helpers.director.model_func.dictfy import sim_dict

class WorkinfoPage(TablePage):
    def get_label(self):
        return '求职者信息'
    
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = WorkInfo
        exclude = ['user']
        pop_edit_fields=['id']
        
        def dict_head(self, head):
            width = {
                'address':120,
            }
            if head['name'] in width:
                head['width'] = width[head['name']]
            if head.get('editor') == 'com-table-picture':
                head['width'] = 200
                
            return head
        
        class filters(RowFilter):
            names = ['name','status']
            icontains =['name']
            range_fields =['update_time']
        
        def get_operation(self):
            return []
        

class WorkinfoForm(ModelFields):
    class Meta:
        model = WorkInfo
        exclude =['user']


class WorkinfoFormBase(ModelFieldsMobile):
    nolimit=True
    class Meta:
        model = WorkInfo
        exclude =[]
    
    def __init__(self, dc={}, pk=None, crt_user=None, *args, **kw):
        crt_user = get_request_cache()['request'].user
        instance,_ = WorkInfo.objects.get_or_create(user=crt_user)
        super().__init__(dc, pk, crt_user,instance=instance, *args, **kw)
    
    def dict_head(self, head):
        head = super().dict_head(head)
        if self.instance.status != 0:
            head['readonly'] = True
        return head
    
    def clean(self):
        if self.instance.status  !=0 :
            raise UserWarning('服务者信息已经被锁定，不能进行编辑!')
    def get_operations(self):
        if self.instance.status != 0:
            return []
        else:
            ops = super().get_operations()
            for op in ops:
                if op['name']  == 'save':
                    op['label'] = '保存'
            return ops

class WorkinfoBase(WorkinfoFormBase):
    class Meta:
        model = WorkInfo
        fields =['name','contact','address','head']
    
    def dict_head(self, head):
        head = super().dict_head(head)
        if head['name'] in ['name','contact']:
            head['required'] = True
        return head
    
class WorkinfoIdFace(WorkinfoFormBase):
    class Meta:
        model = WorkInfo
        fields=['id_face1','id_face2']
        
class WorkerBankInfo(WorkinfoFormBase):
    class Meta:
        model = WorkInfo
        fields=['bank_cover','bank_code','opening_bank']
        
class Workinfo_education(WorkinfoFormBase):
    class Meta:
        model = WorkInfo
        fields = ['education','vocational_certificate','skills_certificate']

#class WorkinfoAgreement(WorkinfoFormBase):
    #class Meta:
        #model = WorkInfo
        #fields = ['service_agreement']

@director_view('get_worker_info')
def get_worker_info(worker):
    worker_info = WorkInfo.objects.get(pk = worker)
    return sim_dict(worker_info)

@director_view('workerinfo/progress')
def get_workerInfo_cert_progress():
    user = get_request_cache()['request'].user
    info , _ = WorkInfo.objects.get_or_create(user=user)
    return info.status

@director_view('workerinfo/submit_info')
def submit_info():
    user = get_request_cache()['request'].user
    info , _ = WorkInfo.objects.get_or_create(user=user)
    if info.status !=0:
        raise UserWarning('认证信息不能提交审核')
    if not info.name or not info.contact:
        raise UserWarning('请完善基本信息后再提交审核')
    if not info.id_face1 or not info.id_face2:
        raise UserWarning('请完上传身份证正反面')
    #if not info.service_agreement:
        #raise UserWarning('请上传自由职业者服务者协议')
    info.status = 1
    info.save()
    return info.status



director.update({
    'workinfo':WorkinfoPage.tableCls,
    'workinfo.edit':WorkinfoForm,
    'workinfo.base':WorkinfoBase,
    'workinfo.idface':WorkinfoIdFace,
    'workinfo.education':Workinfo_education,
    'workinfo.bankcard':WorkerBankInfo,
    #'workinfo.agreement':WorkinfoAgreement,
})

page_dc.update({
    'workinfo':WorkinfoPage
})