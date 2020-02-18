from helpers.director.shortcut import TablePage,ModelTable,ModelFields,page_dc,director
from .models import SeekJobInfo
from helpers.mobile.shortcut import ModelFieldsMobile,ModelTableMobile

class SeekJobPage(TablePage):
    def get_label(self):
        return '求职信息管理'
    
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = SeekJobInfo
        exclude =[]
        pop_edit_fields=['id']

class SeekJobForm(ModelFields):
    class Meta:
        model = SeekJobInfo
        exclude =[]
    

class SeekJobUserForm(ModelFieldsMobile):
    readonly=['audit_status']
    hide_fields=['worker']
    class Meta:
        model = SeekJobInfo
        exclude =[]
    
    def clean_dict(self, dc):
        if not dc.get('worker'):
            dc['worker'] = self.crt_user.workinfo.pk
        return dc
    
    def dict_head(self, head):
        head = super().dict_head(head)
        if head['name'] in ['salary','jobtime']:
            head['required']= True
        if head['name'] not in ['audit_status','status']:
            head['readonly'] = 'scope.row.audit_status !=1'
        return head
    
    #def clean_save(self):
        #if not self.instance.worker:
            #self.instance.worker = self.crt_user.workerinfo

    def get_operations(self):
        ops = super().get_operations()
        for op in ops:
            if op['name'] == 'save':
                op.update({
                'label':'保存并提交审核',
                'show':'scope.vc.row.audit_status ==1',
                'action':'''if(scope.ps.vc.isValid()){
                    cfg.confirm("审核期间该条记录将不能被修改，确定提交审核吗?").then(()=>{ scope.ps.vc.row.audit_status=1; scope.ps.vc.submit() })
                    } '''
                })
        ops += [
            {'label':'保存','editor':'com-op-van-btn',
             'type':'primary',
             'show':'scope.vc.row.audit_status !=1',
              'action':'''if(scope.ps.vc.isValid()){ 
                  cfg.show_load();scope.ps.vc.submit().then(()=>{cfg.hide_load();cfg.toast("保存成功")}) 
              }
              '''},
        ]
        return ops
        

class SeekjobUserList(ModelTableMobile):
    model = SeekJobInfo
    exclude =[ ]
    fields_sort=['key_words','status']
    

class Seekjob_Company(ModelTableMobile):
    model = SeekJobInfo
    exclude =[]
    
    #def inn_filter(self, query):
        #return query.anotate(head = ) 
        
    def dict_row(self, inst):
        cert_img = []
        if inst.worker.education:
            cert_img.append(inst.worker.education)
        if inst.worker.vocational_certificate:
            cert_img.append(inst.worker.vocational_certificate)
        if inst.worker.skills_certificate:
            cert_img.append(inst.worker.skills_certificate)
        if inst.worker.service_agreement:
            cert_img.append(inst.worker.service_agreement)
        return {
            'worker__head':inst.worker.head,
            'worker__name':inst.worker.name,
            'worker__contact':inst.worker.contact,
            'worker__address':inst.worker.address,
            'cert_images':cert_img
        }

director.update({
    'seekjob':SeekJobPage.tableCls,
    'seekjob.edit':SeekJobForm,
    
    'seekjobuserlist':SeekjobUserList,
    'seekjobuserlist.edit':SeekJobUserForm,
    
   
    'seekjob_company':Seekjob_Company,
})

page_dc.update({
    'seekjob':SeekJobPage
})