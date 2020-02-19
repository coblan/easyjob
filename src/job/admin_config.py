from helpers.director.shortcut import FieldsPage,Fields,page_dc,director
from helpers.director.kv import get_value,set_value

class ConfigPage(FieldsPage):
    def get_label(self):
        return '设置管理'
    
    def get_template(self, prefer=None):
        return 'jb_admin/fields.html'
    
    class fieldsCls(Fields):
        
        def get_heads(self):
            return [
                {'name':'company_cert_protocol','label':'商家认证协议','editor':'com-field-richtext'},
                {'name':'worker_cert_protocol','label':'求职者认证协议','editor':'com-field-richtext'},
            ]
        
        def dict_row(self):
            return {
                'company_cert_protocol':get_value('company_cert_protocol',''),
                'worker_cert_protocol':get_value('worker_cert_protocol',''),
            }
        
        def save_form(self):
            set_value('company_cert_protocol',self.kw.get('company_cert_protocol'))
            set_value('worker_cert_protocol',self.kw.get('worker_cert_protocol'))
        
        

director.update({
    'configpage':ConfigPage.fieldsCls,
})

page_dc.update({
    'configpage':ConfigPage
})