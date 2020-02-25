from hello.engin_menu import mb_page
from ..admin_workinfo import WorkinfoBase,WorkinfoIdFace,Workinfo_education #,WorkinfoAgreement
from helpers.director.kv import get_value

class WorkerCert(object):
    def __init__(self, request, engin):
        pass
    
    def get_template(self):
        return 'mobile/live_show.html'
    
    def get_context(self):
        return {
            'editor':'live_cell',
            'editor_ctx':{
                        'title':'个人认证',
                        'back_action':'location="/mb/index"',
                        'groups':[
                            {
                                'label':'认证信息',
                                 'cells':[
                          
                                    {
                                       'label':'基本信息',
                                       'action':'live_root.open_live("live_fields",scope.head.fields_ctx)',
                                         'fields_ctx':{
                                             'title':'基本信息',
                                             **WorkinfoBase().get_context()
                                             }
                                   },
                                    {
                                        'label':'身份证上传',
                                        'action':'live_root.open_live("live_fields",scope.head.fields_ctx)',
                                         'fields_ctx':{
                                             'title':'身份证',
                                             **WorkinfoIdFace().get_context()
                                             }
                                        
                                    },
                                    {
                                        'label':'学历证明',
                                        'action':'live_root.open_live("live_fields",scope.head.fields_ctx)',
                                         'fields_ctx':{
                                             'title':'学历证明',
                                             **Workinfo_education().get_context()
                                             }
                                    },
                                    #{
                                        #'label':'职业证书',
                                    #},
                                    #{
                                        #'label':'技能证书'
                                    #},
                                    #{
                                        #'label':'自由职业者服务协议',
                                        #'action':'live_root.open_live("live_fields",scope.head.fields_ctx)',
                                         #'fields_ctx':{
                                             #'title':'服务协议',
                                             #**WorkinfoAgreement().get_context()
                                             #}
                                        
                                    #},
                            
                               ]
                                
                            },
                            {
                                'label':'审核',
                                'cells':[
                                    #{'label':'资料下载',
                                     #'action':'live_root.open_live("live_layout",scope.head.live_ctx)',
                                     #'live_ctx':{
                                         #'layout_editors':[
                                             #{'editor':'com-lay-navbar','title':'资料下载',},
                                             #{'editor':'com-top-filedownload','files':[
                                                 #{'url':'/static/material/易职通平台服务合同（企业）.docx','label':'易职通平台服务合同（企业）'}
                                                 #]},
                                         #]
                                     #}
                                   #},
                                    {
                                        'label':'审核进度',
                                        'action':'live_root.open_live("live_com_cert_progress",scope.head.progress_ctx)',
                                         'progress_ctx':{
                                             'title':'审核进度',
                                             'init_express':'cfg.show_load();ex.director_call("workerinfo/progress").then(resp=>{cfg.hide_load();scope.vc.active = resp})',
                                             'submit_info_express':'''cfg.pop_vue_com("com-pop-protocal",scope.vc.ctx.protocal_ctx)
                                             .then(()=>{
                                                 cfg.show_load();
                                                 return ex.director_call("workerinfo/submit_info")
                                             }).then(resp=>{
                                                 cfg.hide_load();
                                                 cfg.toast("服务者认证申请已经提交成功，请耐心等待!");
                                                 scope.vc.active = resp
                                             })'''  ,
                                              'protocal_ctx':{
                                                  'content':get_value('worker_cert_protocol','求职者认证协议不能为空!')
                                              }
                                         }
                                    }
                                ]
                            }
                        ]
                       
            }
        }
    

mb_page.update({
    'workercert':WorkerCert
})