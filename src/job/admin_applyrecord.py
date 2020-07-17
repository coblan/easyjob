from helpers.director.shortcut import TablePage,ModelTable,ModelFields,page_dc,director,RowFilter,SelectSearch
from .models import ApplyRecord,WorkInfo
from helpers.mobile.shortcut import ModelFieldsMobile
from helpers.director.model_func.dictfy import sim_dict
from helpers.director.kv import get_value

class ApplyRecordPage(TablePage):
    def get_label(self):
        return '申请记录'
    
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = ApplyRecord
        exclude =[]
        fields_sort=['id','worker','company','job','status','updatetime','createtime']
        pop_edit_fields = ['id']
        
        def getExtraHead(self):
            return [
                {'name':'company','label':'公司','width':150},
            ]
        
        def inn_filter(self, query):
            return query.select_related('job__com')
        
        def dict_head(self, head):
            width={
                'job':150,
                'status':150,
            }
            if head['name'] in width:
                head['width'] = width.get(head['name'])
            
            if head['name'] == 'status':
                head['editor'] = 'com-table-tag-map'
                head['class_map']={
                    0:'info',
                    1:'success',
                    2:'warning',
                    3:'success',
                    4:'success',
                    101:'warning',
                    
                }

            return head
        
        def dict_row(self, inst):
            return {
                'company':str(inst.job.com)
            }
        
        def get_operation(self):
            return [
                {'editor':'com-btn',
                 'label':'审批通过',
                 'action':'scope.ps.selected_set_and_save(scope.head)',
                 'pre_set':'rt={status:3}',
                 'row_match':'many_row',
                 'match_express':'scope.row.status == 1',
                 'match_msg':'只能选择商家已经接受了的申请',
                 },
                {'editor':'com-btn',
                 'label':'审批不通过',
                 'action':'scope.ps.selected_set_and_save(scope.head)',
                 'pre_set':'rt={status:101}',
                 'row_match':'many_row',
                 'match_express':'scope.row.status == 1',
                 'match_msg':'只能选择商家已经接受了的申请',
                 }
            ]
            
        class filters(RowFilter):
            names = ['status']
            range_fields = ['createtime','updatetime']
        
        class search(SelectSearch):
            names = ['job__com__name','worker_name']
            
            def get_option(self, name): 
                if name =='job__com__name':
                    return {'value':'job__com__name','label':'公司'}
                    
                if name =='worker_name':
                    return {'value':'worker__name','label':'个人'}
            
class ApplyRecordFrom(ModelFields):
    class Meta:
        model = ApplyRecord
        exclude = []
    
    def dict_head(self, head):
        if head['name'] =='status':
            head['editor'] ='com-field-flow'
            head['chain']={
                0:{
                    'last':[],
                    'next':[1,2]
                },
                1:{
                    'last':[0],
                    'next':[3,101]
                },
                2:{
                    'last':[0],
                    'next':[]
                },
                3:{
                    'last':[0,1],
                    'next':[4,]
                },
                4:{
                    'last':[0,1,3],
                    'next':[5]
                },
                5:{
                    'last':[0,1,3,4],
                    'next':[],
                },
                101:{
                    'last':[0,1],
                    'next':[]
                }
            }
        return head
        

class WorkinfoCompany(ModelFieldsMobile):
    nolimit = True
    class Meta:
        model = WorkInfo
        exclude = ['status','update_time']
    
    def dict_head(self, head):
        head['readonly'] = True
        head['required'] = False
        head['help_text'] = ''
        return head

class ApplyRecordFormCompany(ModelFieldsMobile):
    nolimit = True
    class Meta:
        model = ApplyRecord
        exclude = []
    
    def dict_head(self, head):
       
        if head['name'] == 'finish_proof':
            head['show'] = 'scope.row.status == 3'
        else:
            head['readonly'] = True
            head['required'] = False
        return head
    
    def getExtraHeads(self):
        #self.workinfo = WorkInfo.objects.get(pk = self.instance.worker)
        return WorkinfoCompany().get_heads()
    
    def get_head_context(self):
        ctx = super().get_head_context()
        ctx.update({
            'fields_group':[
                {'label':'申请信息','heads':['worker','job','status','createtime','finish_proof'],},
                {'label':'求职者信息','heads':['head','contact','address','id_face1','id_face2','education','vocational_certificate','skills_certificate']}
            ]
        })
        return ctx
    
    def dict_row(self, inst):
        dc = sim_dict(inst.worker,exclude=['id','status','update_time'])
        dc.pop('pk')
        return dc
    
    def get_operations(self):
        return [
                 { 
                  'editor':'com-op-submit',
                  'label':'接受申请', 
                  'protocal':get_value('company_empoly_protocol','请在后台完善《商家用工协议》'),
                  'show':'scope.vc.row.status==0',
                  'action':'''cfg.pop_vue_com("com-pop-protocal",{content:scope.head.protocal}).then(()=>{  
                        cfg.show_load();scope.ps.vc.row.status=1; 
                        return scope.ps.vc.submit()
                     }) .then(()=>{
                      cfg.hide_load();
                      cfg.toast("操作成功");
                      scope.ps.vc.par_row.status=1
                      history.back()
                      })
                      '''},
                 { 
                  'editor':'com-op-van-btn',
                  'label':'拒绝申请', 
                  'type':'warning',
                  'show':'scope.vc.row.status==0',
                  'action':'''cfg.show_load();scope.ps.vc.row.status=2; scope.ps.vc.submit().then(()=>{
                      cfg.hide_load();
                      cfg.toast("操作成功");
                      scope.ps.vc.par_row.status=2
                      })
                      '''},
                 
                 { 
                  'editor':'com-op-van-btn',
                  'type':'info',
                  'label':'项目完结', 
                  'show':'scope.vc.row.status==3',
                  'action':'''cfg.show_load();scope.ps.vc.row.status=4; scope.ps.vc.submit().then(()=>{
                      cfg.hide_load();
                      cfg.toast("操作成功");
                      scope.ps.vc.par_row.status=4
                      })'''}
        ]
    
                
director.update({
    'applyrecord':ApplyRecordPage.tableCls,
    'applyrecord.edit':ApplyRecordFrom,
    'applyrecord.company':ApplyRecordFormCompany,
})

page_dc.update({
    'applyrecord':ApplyRecordPage
})