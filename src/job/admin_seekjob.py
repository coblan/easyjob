from helpers.director.shortcut import TablePage,ModelTable,ModelFields,page_dc,director,RowFilter,SelectSearch
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
        
        def get_operation(self):
            return []
        
        class filters(RowFilter):
            names = ['status','audit_status']
            range_fields=['update_time']
        
        class search(SelectSearch):
            names = ['key_words','worker__name']
            
            def get_option(self, name):
                if name =='key_words':
                    return {'value':'key_words','label':'关键字'}
                if name == 'worker__name':
                    return {'value':'worker__name','label':'求职者'}
            

class SeekJobForm(ModelFields):
    class Meta:
        model = SeekJobInfo
        exclude =[]
    

class SeekJobUserForm(ModelFieldsMobile):
    hide_fields=['worker']
    nolimit=True
    class Meta:
        model = SeekJobInfo
        exclude =[]
    
    def clean_dict(self, dc):
        if not dc.get('worker') and getattr(self.crt_user,'workinfo',None):
            dc['worker'] = self.crt_user.workinfo.pk
        return dc
    
    def dict_head(self, head):
        head = super().dict_head(head)
        if head['name'] in ['salary','jobtime']:
            head['required']= True
        if head['name'] not in ['audit_status','status']:
            head['readonly'] = 'scope.row.audit_status !=1'
        if head['name'] == 'audit_status':
            head ['readonly'] = True
        if head['name'] == 'status':
            head['editor'] = 'com-field-switch'
            head['int_bool'] = True
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
                    cfg.confirm("审核期间该条记录将不能被修改，确定提交审核吗?").then(()=>{ scope.ps.vc.row.audit_status=2; scope.ps.vc.submit() })
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
    nolimit=True
    exclude =[ ]
    fields_sort=['key_words','status']
    
    def inn_filter(self, query):
        return query.filter(worker = self.crt_user.workinfo)
    
    def get_operation(self):
        return []
    

class Seekjob_Company(ModelTableMobile):
    model = SeekJobInfo
    exclude =[]
    nolimit=True
    #def inn_filter(self, query):
        #return query.anotate(head = ) 
    
    def inn_filter(self, query):
        return query.filter(status =1 ).order_by('-update_time')
        
    def dict_row(self, inst):
        cert_img = []
        if inst.worker.education:
            cert_img.append(inst.worker.education)
        if inst.worker.vocational_certificate:
            cert_img.append(inst.worker.vocational_certificate)
        if inst.worker.skills_certificate:
            cert_img.append(inst.worker.skills_certificate)
        #if inst.worker.service_agreement:
            #cert_img.append(inst.worker.service_agreement)
        return {
            'worker__head':inst.worker.head,
            'worker__name':inst.worker.name,
            'worker__contact':inst.worker.contact,
            'worker__address':inst.worker.address,
            'cert_images':cert_img
        }
    
    class filters(RowFilter):
        names = ['key_words',]
        icontains = ['key_words',]

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