from hello.engin_menu import mb_page
from django.conf import settings
from helpers.director.shortcut import get_request_cache
from job.admin_jobinfo import JobinfoUserForm,JobinfUserList,MyJobinfoList,CompanySJobApplyList,WorkerSJobApplyList
from job.admin_seekjob import SeekjobUserList,Seekjob_Company
from job.admin_help import MyhelpUserList
from . worker_cert import get_worker_info_heads
from job.admin_applyrecord import ApplyRecordFormCompany
from helpers.func.collection.container import evalue_container

def has_valid_company(user):
    if getattr(user,'companyinfo',None):
        return user.companyinfo.status ==2

def has_valid_workinfo(user):
    if getattr(user,'workinfo',None):
        return user.workinfo.status ==2

class Home(object):
    def __init__(self, request, engin):
        self.request =request
    
    def get_template(self):
        return 'mobile/live_show.html'
    
    def get_context(self):
        #named_ctx = get_request_cache()['named_ctx']
        #named_ctx.update({
            #'jobinfo.edit':
        #})
        crt_user = self.request.user
        ctx =  {
             'editor_ctx':{
                 'layout_editors':[
                    {'editor':'com-top-home-brand','username':self.request.user.username},
                    #{   
                        #'editor':'com-layout-grid',
                        #'heads':[
                            #{'editor':'com-grid-icon-btn','icon':'/static/images/发布招工.png','label':'发布招工','action':'live_root.open_live("live_attendence_btn",{title:"员工打卡"})'},
                            #{'editor':'com-grid-icon-btn','icon':'/static/images/招工信息.png','label':'求职信息','action':'live_root.open_live("live_attendence_btn",{title:"员工打卡"})'},
                            ##{'editor':'com-grid-icon-btn','icon':'/static/images/招工信息.png','label':'招工信息','table_ctx':AttendenceList().get_head_context(),'action':'live_root.open_live("live_list",scope.head.table_ctx)'},
                            ##{'editor':'com-grid-icon-btn','icon':'/static/images/client.png','label':'我的客户','table_ctx':ClientList().get_head_context(),'action':'live_root.open_live("live_list",scope.head.table_ctx)'},
                            ##{'editor':'com-grid-icon-btn','icon':'/static/images/work_record.png','table_ctx':WorkNoteList().get_head_context(),'label':'工作总结','action':'live_root.open_live("live_list",scope.head.table_ctx)'},
                            ##{'editor':'com-grid-icon-btn','icon':'/static/images/visit.png','label':'拜访记录','table_ctx':VisitList().get_head_context(),'action':'live_root.open_live("live_list",scope.head.table_ctx)'},
                            ###{'editor':'com-grid-icon-btn','icon':'/static/images/myinfo.png','label':'我的资料','fields_ctx':EmployeeForm().get_head_context(),'action':'ex.director_call("get_row",{director_name:scope.head.fields_ctx.director_name}).then((row)=>{scope.head.fields_ctx.row=row; live_root.open_live("live_fields",scope.head.fields_ctx)} )'},
                            ##{'editor':'com-grid-icon-btn','icon':'/static/images/myinfo.png','label':'我的资料','fields_ctx':EmployeeForm().get_head_context(),'action':'live_root.open_live("live_fields",scope.head.fields_ctx)'},
                        #]
                    #},
                    {'editor':'com-van-grid',
                     'title':'商家',
                     'heads':[
                         {
                             'label':'商家认证',
                             'icon':'/static/images/认证.png',
                             'action':'location = "/mb/com_cert"',
      
                         },
                         #{'label':'发布招工','icon':'/static/images/发布.png',
                          #'action':'live_root.open_live("live_fields",scope.head.fields_ctx)',
                          #'fields_ctx':{ 'title':'发布招工','after_save':'cfg.toast("发布成功!");setTimeout(()=>{history.back()},1500)',
                                         #**JobinfoUserForm().get_context() } },
                         {'label':'发布招工',
                          'icon':'/static/images/发布.png',
                          'action':'location = "/mb/com_release"',
                          'visible': has_valid_company(crt_user),
                           },
                         
                         {'label':'求职信息','icon':'/static/images/求职.png',
                          'action':'live_root.open_live("live_list",scope.head.table_ctx)',
                          'table_ctx':{'title':'求职信息',
                                       'table_editor':'com-top-seekjob-item',
                                       'block_click':'live_root.open_live("live_seekjob_detail",{row:scope.row})',
                                       **Seekjob_Company().get_head_context()} 
          
                          },
                         {'label':'我的发布',
                          'icon':'/static/images/发放.png',
                          'table_ctx':{'title':'我发布的职位',
                                       #'table_editor':'com-list-row-cell',
                                       #'fields_ctx':{ 
                                                      #'after_save':'cfg.toast("修改成功!");setTimeout(()=>{history.back()},1500);',
                                                      #**JobinfoUserForm().get_context(),
                                                      #},
                                       #'block_click':'''debugger;scope.ps.vc.ctx.fields_ctx.row=scope.row;
                                       #scope.ps.vc.ctx.fields_ctx.title=scope.row.position;
                                       #live_root.open_live("live_fields",scope.ps.vc.ctx.fields_ctx)''',
                                       **MyJobinfoList().get_head_context()}, 
                           'action':'live_root.open_live("live_list",scope.head.table_ctx)',
                            'visible': has_valid_company(crt_user),
                           },
                        {'label':'申请列表',
                          'icon':'/static/images/列表.png',
                          'table_ctx':{'title':'申请列表',
                                       #'block_click':'live_root.open_live("live_company_apply_detail",{jobinfo:scope.row,worker:scope.row.worker})',
                                       'block_click':'''ex.director_call("applyrecord.company",{pk:scope.row.pk}).then(resp=>{
                                          scope.head.fields_ctx.par_row = scope.row
                                          scope.head.fields_ctx.row= resp.row
                                          scope.head.fields_ctx.title= resp.row._label
                                          live_root.open_live("live_fields",scope.head.fields_ctx)
                                       })  '''  ,
                                       'fields_ctx':{
                                           **ApplyRecordFormCompany().get_head_context()
                                           },
                                       
                                       'table_editor':'com-apply-list-company',
                                       **CompanySJobApplyList().get_head_context()}, 
                           'action':'live_root.open_live("live_list",scope.head.table_ctx)',
                           'visible': has_valid_company(crt_user),
                           },
                         
                                                                   #debugger
                                          #scope.head.fields_ctx.par_row = scope.row
                         
                         ]},
                    {'editor':'com-van-grid',
                     'title':'个人',
                     'heads':[
                         {'label':'求职认证','icon':'/static/images/个人简历.png',
                           'action':'location = "/mb/workercert"',
                           },
                         {'label':'发布求职','icon':'/static/images/发布招工.png',
                           'action':'location = "/mb/worker_release"',
                           'visible':has_valid_workinfo(crt_user),
                           },
                         {'label':'招工信息','icon':'/static/images/工厂招工.png',
                          'action':'live_root.open_live("live_list",scope.head.table_ctx)',
                          'table_ctx':{
                              **JobinfUserList().get_head_context(),
                              'title':'需求职位',
                                'table_editor':'com-list-jobinfo-item',
                                'block_click':'live_root.open_live("live_jobinfo_detail",{row:scope.row,title:"职位详情"})',
                                       } },
                        {'label':'我的求职',
                         'icon':'/static/images/请求.png',
                         'table_ctx':{'title':'我的求职',
                                       #'table_editor':'com-list-row-cell',
                                       #'fields_ctx':{ 'title':'求职信息',
                                                      #'after_save':'cfg.toast("修改成功!");setTimeout(()=>{history.back()},1500);',
                                                      #**SeekJobUserForm().get_context() },
                                       #'block_click':'''scope.ps.vc.ctx.fields_ctx.row=scope.row;
                                       #live_root.open_live("live_fields",scope.ps.vc.ctx.fields_ctx)''',
                                       **SeekjobUserList().get_head_context()}, 
                           'action':'live_root.open_live("live_list",scope.head.table_ctx)',
                           'visible':has_valid_workinfo(crt_user),
                          },
                        
                         {'label':'我的申请',
                         'icon':'/static/images/列表1.png',
                         'table_ctx':{'title':'我的申请',
                                      'table_editor':'com-apply-detail',
                                      'block_click':'cfg.show_load();ex.director_call("d.get_row",{director_name:"MyJobinfoList.edit",pk:scope.row.job}).then((resp)=>{cfg.hide_load(); live_root.open_live("live_jobinfo_detail",{row:resp,title:"职位详情"})  })' ,
                                       **WorkerSJobApplyList().get_head_context()}, 
                           'action':'live_root.open_live("live_list",scope.head.table_ctx)',
                           'visible':has_valid_workinfo(crt_user),
                          },
   
                         ]},
                    {
                        'editor':'com-van-grid',
                        'title':'其他',
                        'heads':[
                            {'label':'资料下载','icon':'/static/images/下载.png',
                             'action':'live_root.open_live("live_layout",scope.head.live_ctx)',
                              'live_ctx':{
                                  'layout_editors':[
                                      {'editor':'com-lay-navbar','title':'资料下载',},
                                      
                                      {'editor':'com-top-filedownload',
                                       'title':'企业',
                                       'files':[
                                          {'url':'/static/material/易职通平台服务合同（企业）.docx','label':'易职通平台服务合同（企业认证）'},
                                          {'url':'/static/material/服务完成确认单.docx','label':'服务完成确认单'},
                                          
                                          ]},
                                      
                                      {'editor':'com-top-filedownload',
                                       'title':'求职者',
                                       'files':[
                                          {'url':'/static/material/自由职业者服务协议.docx','label':'自由职业者服务协议(求职者认证)'}
                                          ]},
                                  ]
                              }
                             },
                            {'label':'客服',
                             'icon':'/static/images/客服.png',
                             'action':'live_root.open_live("live_layout",scope.head.live_ctx)',
                             'live_ctx':{
                                 'layout_editors':[
                                     {'editor':'com-lay-navbar','title':'客服',},
                                     {'editor':'com-top-kefu','phone':'0831-2022777','worktime':'工作日9:00-17:00'},
                                 ]
                             }
                             },
                             {'label':'帮助',
                             'icon':'/static/images/帮助.png',
                             'action':'live_root.open_live("live_list",scope.head.table_ctx)',
                             'table_ctx':{
                                 'title':'帮助中心',
                                  'table_editor': 'com-list-row-cell',
                                 'block_click':'live_root.open_live("live_html",scope.row)',
                                 **MyhelpUserList().get_context()
                             }
                             },
                            
                        ]
                    },
                    
                 ]
            },
             'editor':'live_layout',
            
        }
        return evalue_container(ctx)




mb_page.update({
    'index':Home
})