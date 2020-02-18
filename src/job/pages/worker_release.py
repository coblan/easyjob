from hello.engin_menu import mb_page
from job.admin_seekjob import SeekJobUserForm
from job.decorator import need_worker_cert

class WorkerRelease(object):
    def __init__(self, *args, **kwargs):
        pass
    
    def get_template(self):
        return 'mobile/live_show.html'
    
    @need_worker_cert
    def get_context(self):
        return {
             'editor':'live_fields',
             'editor_ctx':{ 
                 'title':'发布招工',
                 'back_action':'location="/mb/index"',
                  'after_save':'cfg.toast("提交成功!");setTimeout(()=>{history.back()},1500)',
                   **SeekJobUserForm().get_context() 
                   }
             
        }

mb_page.update({
    'worker_release':WorkerRelease
})