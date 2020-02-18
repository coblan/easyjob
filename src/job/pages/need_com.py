from hello.engin_menu import mb_page

class NeedCom(object):
    need_login=False
    
    def __init__(self, *args,**kws):
        pass
    
    def get_template(self):
        return 'mobile/live_show.html'
    
    def get_label(self):
        return '用户登录'
    
    def get_context(self):
        return {
            'editor':'live_info',
            'editor_ctx':{
                'info':'请先完成商户资格认证!',
                'ops':[
                    {'editor':'com-op-submit','label':'确定','action':'location="/mb/index"',}
                ]
            }
        }

mb_page.update({
    'need_com':NeedCom
})