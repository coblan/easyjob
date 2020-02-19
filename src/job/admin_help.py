from helpers.director.shortcut import TablePage,ModelFields,ModelTable,page_dc,director
from .models import MyHelp
from helpers.mobile.shortcut import ModelTableMobile

class MyHelpPage(TablePage):
    def get_label(self):
        return '帮助管理'
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = MyHelp
        exclude =[]
        pop_edit_fields=['id']


class MyhelpForm(ModelFields):
    class Meta:
        model = MyHelp
        exclude = []
        

class MyhelpUserList(ModelTableMobile):
    model = MyHelp
    exclude= []
    fields_sort=['title']

director.update({
    'myhelp':MyHelpPage.tableCls,
    'myhelp.edit':MyhelpForm,
    
    'myhelp.userlist':MyhelpUserList,
})

page_dc.update({
    'myhelp':MyHelpPage,
    
})
