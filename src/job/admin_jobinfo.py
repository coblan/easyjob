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
        exclude =['publisher']
    
    def clean_save(self):
        self.instance.publisher = self.crt_user

class JobinfUserList(ModelTableMobile):
    model = JobInfo
    exclude = []
    nolimit=True
    def inn_filter(self, query):
        return query.order_by('-update_time')
    
    class filters(RowFilter):
        names =['position','com_name']
        icontains = ['position','com_name']

class MyJobinfoList(ModelTableMobile):
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
    
    def dict_row(self, inst):
        return { '_director_name':'jobinfoform'}
    
    def inn_filter(self, query):
        return query.order_by('-update_time')
    
    

director.update({
    'jobinfo':JobInfoPage.tableCls,
    'jobinfo.edit':JobinfoForm,
    'jobinfoform':JobinfoUserForm,
    'jobinfolist':JobinfUserList,
    'MyJobinfoList':MyJobinfoList,
})
page_dc.update({
    'jobinfo':JobInfoPage
})