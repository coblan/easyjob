from hello.engin_menu import mb_page
from job.admin_jobinfo import JobinfoUserForm
from ..decorator import need_com

class ComReleasePage(object):
    def __init__(self, request, engin):
        pass
    
    def get_template(self):
        return 'mobile/live_show.html'
    
    @need_com
    def get_context(self):
        return {
            'editor':'live_fields',
            'editor_ctx':  { 'title':'发布招工',
                             'back_action':'location="/mb/index"',
                             'after_save':'cfg.toast("发布成功!");setTimeout(()=>{history.back()},1500)',
                             **JobinfoUserForm().get_context() 
                 }
                
        }
    #{
            #'editor':'live_cell',
             #'editor_ctx':{
                        #'title':'招工发布',
                        #'back_action':'location="/mb/index"',
                        #'cells':[
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
                            #{
                                #'label':'发布招工信息',
                                #'action':'live_root.open_live("live_fields",scope.head.fields_ctx)',
                                #'fields_ctx':{ 'title':'发布招工','after_save':'cfg.toast("发布成功!");setTimeout(()=>{history.back()},1500)',
                                         #**JobinfoUserForm().get_context() }
                            #}
                        #]
            #}
        #}


mb_page.update({
    'com_release':ComReleasePage
})