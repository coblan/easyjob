from hello.engin_menu import mb_page
from django.conf import settings
from helpers.director.shortcut import get_request_cache
from job.admin_jobinfo import JobinfoUserForm,JobinfUserList,MyJobinfoList
from job.admin_seekjob import SeekjobUserList,SeekJobUserForm,Seekjob_Company

class Home(object):
    def __init__(self, request, engin):
        pass
    
    def get_template(self):
        return 'mobile/live_show.html'
    
    def get_context(self):
        #named_ctx = get_request_cache()['named_ctx']
        #named_ctx.update({
            #'jobinfo.edit':
        #})
        return {
             'editor_ctx':{
                 'layout_editors':[
                    {'editor':'com-top-home-brand',},
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
                                       'table_editor':'com-list-row-cell',
                                       'fields_ctx':{ 'title':'发布招工',
                                                      'after_save':'cfg.toast("修改成功!");setTimeout(()=>{history.back()},1500);',
                                                      **JobinfoUserForm().get_context() },
                                       'block_click':'''scope.ps.vc.ctx.fields_ctx.row=scope.row;
                                       scope.ps.vc.ctx.fields_ctx.title=scope.row.position;
                                       live_root.open_live("live_fields",scope.ps.vc.ctx.fields_ctx)''',
                                       **MyJobinfoList().get_head_context()}, 
                           'action':'live_root.open_live("live_list",scope.head.table_ctx)',
                           },
                         
                         ]},
                    {'editor':'com-van-grid',
                     'title':'个人',
                     'heads':[
                         {'label':'求职认证','icon':'/static/images/个人简历.png',
                           'action':'location = "/mb/workercert"',
                           },
                         {'label':'发布求职','icon':'/static/images/发布招工.png',
                           'action':'location = "/mb/worker_release"',
                           },
                         {'label':'招工信息','icon':'/static/images/工厂招工.png',
                          'action':'live_root.open_live("live_list",scope.head.table_ctx)',
                          'table_ctx':{'title':'需求职位',
                                       'table_editor':'com-list-jobinfo-item',
                                       'block_click':'live_root.open_live("live_jobinfo_detail",{row:scope.row})',
                                       **JobinfUserList().get_head_context()} },
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
                             }
                        ]
                    }
                 ]
            },
             'editor':'live_layout',
            
        }




mb_page.update({
    'index':Home
})