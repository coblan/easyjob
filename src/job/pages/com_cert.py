from hello.engin_menu import mb_page
from django.conf import settings
from helpers.director.shortcut import get_request_cache
from job.admin_companyinfo import CompanyInfoBasic,CompanyInfoLicense,CompanyInfoaccount_certificate,CompanyInfo_qualification_certificate
from helpers.director.kv import get_value

class Comcert(object):
    def __init__(self, request, engin):
        pass
    
    def get_template(self):
        return 'mobile/live_show.html'
    
    def get_context(self):
        return {
            'editor':'live_cell',
            'editor_ctx':{
                        'title':'商家认证',
                        'back_action':'location="/mb/index"',
                        'groups':[
                           {'label':'认证信息',
                             'cells':[
                                 {'label':'公司基本信息',
                                  'action':'live_root.open_live("live_fields",scope.head.fields_ctx)',
                                  'fields_ctx':{
                                      'title':'基本信息',
                                      **CompanyInfoBasic().get_context()
                                      }},
                                {'label':'营业执照','action':'live_root.open_live("live_fields",scope.head.fields_ctx)',
                                  'fields_ctx':{
                                      'title':'营业执照',
                                      **CompanyInfoLicense().get_context()}},
                                 {'label':'开户许可证','action':'live_root.open_live("live_fields",scope.head.fields_ctx)',
                                  'fields_ctx':{
                                      'title':'开户许可证',
                                      **CompanyInfoaccount_certificate().get_context()
                                      }},
                                 {'label':'资质证书','action':'live_root.open_live("live_fields",scope.head.fields_ctx)',
                                  'fields_ctx':{
                                      'title':'资质证书',
                                      **CompanyInfo_qualification_certificate().get_context()
                                      }},
                                 
                              ]
                             },
                            {'label':'审核',
                             'cells':[
                                 {'label':'审核进度',
                                  'action':'live_root.open_live("live_com_cert_progress",scope.head.progress_ctx)',
                                  'progress_ctx':{
                                      'title':'审核进度',
                                      'init_express':'cfg.show_load();ex.director_call("CompanyInfo/progress").then(resp=>{cfg.hide_load();scope.vc.active = resp})',
                                      'submit_info_express':'''cfg.pop_vue_com("com-pop-protocal",scope.vc.ctx.protocal_ctx) 
                                      .then(()=>{
                                          cfg.show_load();
                                          return ex.director_call("CompanyInfo/submit_info")
                                      }).then(resp=>{
                                          cfg.hide_load();
                                          cfg.toast("申请已经提交，请耐心等待!");
                                          scope.vc.active = resp
                                      })
                                     ''' ,
                                      'protocal_ctx':{
                                          'content':get_value('company_cert_protocol','商户认证协议不能为空!')
                                      }
                                      
                                  }
                                  },
                             ]}
                        ]
                                 
            }
        }
    
    
mb_page.update({
    'com_cert':Comcert
})