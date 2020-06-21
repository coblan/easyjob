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
                {'name':'company_empoly_protocol','label':'商家用工协议','editor':'com-field-richtext'},
                {'name':'apply_job_protocol','label':'求职申请协议','editor':'com-field-richtext'},
            ]
        
        def dict_row(self):
            return {
                'company_cert_protocol':get_value('company_cert_protocol',''),
                'worker_cert_protocol':get_value('worker_cert_protocol',''),
                'company_empoly_protocol':get_value('company_empoly_protocol',''),
                'apply_job_protocol':get_value('apply_job_protocol',''),
            }
        
        def save_form(self):
            set_value('company_cert_protocol',self.kw.get('company_cert_protocol'))
            set_value('worker_cert_protocol',self.kw.get('worker_cert_protocol'))
            set_value('company_empoly_protocol',self.kw.get('company_empoly_protocol'))
            set_value('apply_job_protocol',self.kw.get('apply_job_protocol'))
        
        

director.update({
    'configpage':ConfigPage.fieldsCls,
})

page_dc.update({
    'configpage':ConfigPage
})