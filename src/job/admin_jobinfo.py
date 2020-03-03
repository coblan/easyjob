from helpers.director.shortcut import page_dc,ModelFields,ModelTable,director,TablePage,RowFilter
from .models import JobInfo
from helpers.mobile.shortcut import ModelFieldsMobile,ModelTableMobile

class JobInfoPage(TablePage):
    def get_label(self):
        return '招工信息'
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = JobInfo
        exclude =[]
        pop_edit_fields=['id']

class JobinfoForm(ModelFields):
    class Meta:
        model = JobInfo
        exclude =[]
        
class JobinfoUserForm(ModelFieldsMobile):
    nolimit=True
    class Meta:
        model = JobInfo
        exclude =['com']
    
    def clean_save(self):
        self.instance.com = self.crt_user.companyinfo
    
    def dict_head(self, head):
        head = super().dict_head(head)
        if head['name'] not in ['audit_status','status']:
            head['readonly'] = 'scope.row.audit_status !=1'
        if head['name'] == 'audit_status':
            head ['readonly'] = True
        if head['name'] == 'status':
            head['editor'] = 'com-field-switch'
            head['int_bool'] = True
        return head
    
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
              }'''
             }
        ]
        return ops
        
        

class JobinfUserList(ModelTableMobile):
    "招工信息"
    model = JobInfo
    exclude = []
    nolimit=True
    def inn_filter(self, query):
        return query.filter(status=1).order_by('-update_time')
    
    def dict_row(self, inst):
        papers = [inst.plat_contract,inst.contract,inst.bid]
        
        return {
            'com__name':inst.com.name,
            'com__contact':inst.com.contact,
            'papers':papers,
            
        }
    
    class filters(RowFilter):
        names =['key_words','position','address','com__name']
        icontains = ['position','address','com__name','key_words']
        fields_sort = ['position','address','key_words','com__name']
        
        def getExtraHead(self):
            return [
                {'name':'com__name','label':'公司名称'}
            ]

class MyJobinfoList(ModelTableMobile):
    "我的发布"
    model = JobInfo
    exclude = []
    nolimit=True
    fields_sort=['position','status']
    
    def dict_head(self, head):
        if head['name'] =="position":
            head['css'] ='''
        .xxx{white-space: nowrap;
            max-width: 5.2rem;
            overflow: hidden;
            text-overflow: ellipsis;} '''
            head['class'] ='xxx'
        if head['name'] =='status':
            head['css']='''
            .offline{color:#b4b4b4}
            .online{color:#15dd15}
            '''
            head['class_express'] ='scope.row.status==1?"online":"offline"'
        return head
    
    #def dict_row(self, inst):
        #return { '_director_name':'jobinfoform'}
    
    def inn_filter(self, query):
        return query.filter(com=self.crt_user.companyinfo).order_by('-update_time')
    
    def get_operation(self):
        return []
    
    

director.update({
    'jobinfo':JobInfoPage.tableCls,
    'jobinfo.edit':JobinfoForm,
   
    'jobinfolist':JobinfUserList,
    'MyJobinfoList':MyJobinfoList,
    'MyJobinfoList.edit':JobinfoUserForm,
     #'jobinfoform':JobinfoUserForm,
})
page_dc.update({
    'jobinfo':JobInfoPage
})