from helpers.director.shortcut import TablePage,ModelTable,ModelFields,page_dc,director,get_request_cache,director_view
from job . models import WorkInfo
from helpers.mobile.shortcut import ModelFieldsMobile

class WorkinfoPage(TablePage):
    def get_label(self):
        return '求职者信息'
    
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = WorkInfo
        exclude = []
        pop_edit_fields=['id']

class WorkinfoForm(ModelFields):
    class Meta:
        model = WorkInfo
        exclude =[]


class WorkinfoFormBase(ModelFieldsMobile):
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
            return super().get_operations()

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

class Workinfo_education(WorkinfoFormBase):
    class Meta:
        model = WorkInfo
        fields = ['education','vocational_certificate','skills_certificate']

class WorkinfoAgreement(WorkinfoFormBase):
    class Meta:
        model = WorkInfo
        fields = ['service_agreement']


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
    if not info.service_agreement:
        raise UserWarning('请上传自由职业者服务者协议')
    info.status = 1
    info.save()
    return info.status



director.update({
    'workinfo':WorkinfoPage.tableCls,
    'workinfo.edit':WorkinfoForm,
    'workinfo.base':WorkinfoBase,
    'workinfo.idface':WorkinfoIdFace,
    'workinfo.education':Workinfo_education,
    'workinfo.agreement':WorkinfoAgreement,
})

page_dc.update({
    'workinfo':WorkinfoPage
})