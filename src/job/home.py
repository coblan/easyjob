from helpers.director.shortcut import page_dc
from . models import WorkInfo,JobInfo,ApplyRecord,CompanyInfo,SeekJobInfo

class MyHome(object):
    
    def __init__(self, *args, **kwargs):
        pass
    
    def get_template(self):
        return 'jb_admin/live.html'
    
    def get_context(self):
        rows =[
                {'label':'求职申请待审核','value':ApplyRecord.objects.filter(status=1).count(),'action':'location="/pc/applyrecord?status=1"'},
                {'label':'待结算','value':ApplyRecord.objects.filter(status=4).count(),'action':'location="/pc/applyrecord?status=4"'},
                {'label':'商户认证待审核','value':CompanyInfo.objects.filter(status=1).count(),'action':'location="/pc/cominfo?status=1"'},
                {'label':'个人认证待审核','value':WorkInfo.objects.filter(status=1).count(),'action':'location="/pc/applyrecord?status=1"'},
                {'label':'招工信息待审核','value':JobInfo.objects.filter(audit_status=2).count(),'action':'location="/pc/workinfo?audit_status=2"'},
                {'label':'求职信息待审核','value':SeekJobInfo.objects.filter(audit_status=2).count(),'action':'location="/pc/seekjob?audit_status=2"'},
                        
            ]
        for row in rows:
            if row.get('value') ==0:
                row.pop('action')
        
        return {
            'editor':'com-layout-vertical',
            'editor_ctx':{
                'items':[
                    {'name':'day_static','editor':'com-pan-static1',
                     'label':'任务统计',
                     'rows':rows
                     },
                ]
            }
        }

page_dc.update({
    'phome':MyHome
})