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
    
    class filters(RowFilter):
        names =['position']
        icontains = ['position']

director.update({
    'jobinfo':JobInfoPage.tableCls,
    'jobinfo.edit':JobinfoForm,
    'jobinfoform':JobinfoUserForm,
    'jobinfolist':JobinfUserList,
})
page_dc.update({
    'jobinfo':JobInfoPage
})