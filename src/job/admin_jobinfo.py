from helpers.director.shortcut import page_dc,ModelFields,ModelTable,director,TablePage,RowFilter,director_view,get_request_cache,SelectSearch
from .models import JobInfo,ApplyRecord,WorkInfo
from helpers.mobile.shortcut import ModelFieldsMobile,ModelTableMobile
from django.db.models import F,Q
from helpers.director.model_func.dictfy import sim_dict

class JobInfoPage(TablePage):
    def get_label(self):
        return '招工信息'
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = JobInfo
        exclude =[]
        pop_edit_fields=['id']
        
        def get_operation(self):
            return []
        
        class filters(RowFilter):
            names = ['status','audit_status']
            range_fields = ['update_time']
            
        class search(SelectSearch):
            names = ['com__name','position','address']
            
            def get_option(self, name):
                dc = {
                    'com__name':{'value':'com__name','label':'公司'},
                    'position':{'value':'position','label':'职位'},
                    'address':{'value':'address','label':'地址'}
                }
                return dc.get(name)

class JobinfoForm(ModelFields):
    class Meta:
        model = JobInfo
        exclude =[]
    field_sort=['com','position','pay','appoint','admin_fee','audit_status','address','require_time','key_words','detail','plat_contract','contract','bid','status',]
    readonly=['com']
    
    def get_operations(self):
        ls =[
             {
                 'name':'audit_ok',
                'editor':'com-btn',
                'label':'审批通过', 
                'type':'success',
                'action':'scope.ps.vc.row.audit_status=3;scope.ps.vc.save()',
                'show':'scope.row.audit_status==2'
            }
        ]
        btns = super().get_operations()
        ls.extend(btns)
        return ls
    
    def dict_head(self, head):
        if head['name']=='appoint':
            head.update( 
               {'editor':'com-field-pop-table-select',
                
                #'init_express':'''
                #scope.head.table_ctx.par_row=scope.row; 
                #scope.head.table_ctx.search_args._q = scope.row.Team1En.replace(/-/g,' ');
                #scope.head.table_ctx.search_args._qf = "teamname";
                #Vue.set(scope.head.table_ctx.search_args,"_start_matchdate",scope.row.EventDateTime)
                #Vue.set(scope.head.table_ctx.search_args,"_end_matchdate",scope.row.EventDateTime)
                #Vue.set(scope.head.table_ctx.search_args,"sportid",scope.row.SportId)
                #''',
             #'after_select':'debugger;ex.vueAssign(scope.selected_row,{appoint:scope.row.pk,_appoint_label:scope.row._label},);',
             'table_ctx':WorkerTab().get_head_context(),'options':[],
             })
        return head
            

class WorkerTab(ModelTable):
    model = WorkInfo
    exclude =[]
    
    def inn_filter(self, query):
        return query.filter(status= 2)
    
    def dict_head(self, head):
        if head['name'] =='id':
            head['editor'] ='com-table-click'
            head['action']='scope.ps.vc.$emit("finish",scope.row)'
        return head

    
        
class JobinfoUserForm(ModelFieldsMobile):
    nolimit=True
    class Meta:
        model = JobInfo
        exclude =['com','admin_fee','appoint']
    
    def dict_row(self, inst):
        papers = [inst.plat_contract,inst.contract,inst.bid]
        dc = {
            'papers':papers
        }
        if inst.com:
            dc.update( {
                'com__name':inst.com.name,
                'com__contact':inst.com.contact,
            })
        
        return dc
        
    def clean_save(self):
        self.instance.com = self.crt_user.companyinfo
        self.instance.admin_fee = int(  self.instance.pay * 0.2 )
    
    def dict_head(self, head):
        head = super().dict_head(head)
        if head['name'] not in ['audit_status','status']:
            head['readonly'] = 'scope.row.audit_status !=1'
        if head['name'] == 'audit_status':
            head ['readonly'] = True
        if head['name'] == 'status':
            head['editor'] = 'com-field-switch'
            head['int_bool'] = True
        return head
    
    def get_operations(self):
        ops = super().get_operations()
        for op in ops:
            if op['name'] == 'save':
                op.update({
                    'label':'保存并提交审核',
                    'show':'scope.vc.row.audit_status ==1',
                    'action':'''if(scope.ps.vc.isValid()){
                        cfg.confirm("审核期间该条记录将不能被修改，确定提交审核吗?").then(()=>{ scope.ps.vc.row.audit_status=2; scope.ps.vc.submit() })
                        } '''
                })
        ops += [
            {'label':'保存','editor':'com-op-van-btn',
             'type':'primary',
             'show':'scope.vc.row.audit_status !=1',
             'action':'''if(scope.ps.vc.isValid()){ 
                  cfg.show_load();scope.ps.vc.submit().then(()=>{cfg.hide_load();cfg.toast("保存成功")}) 
              }'''
             }
        ]
        return ops
        
        

class JobinfUserList(ModelTableMobile):
    "招工信息"
    model = JobInfo
    exclude = []
    nolimit=True
    def inn_filter(self, query):
        return query.filter(status=1,audit_status=3).filter(Q(appoint__isnull=True) | Q(appoint=self.crt_user.workinfo)).order_by('-update_time')
    
    def dict_row(self, inst):
        papers = [inst.plat_contract,inst.contract,inst.bid]
        
        return {
            'com__name':inst.com.name,
            'com__contact':inst.com.contact,
            'papers':papers,
            'pay':inst.pay - inst.admin_fee
        }
    
    class filters(RowFilter):
        names =['key_words','position','address','com__name']
        icontains = ['position','address','com__name','key_words']
        fields_sort = ['position','address','key_words','com__name']
        
        def getExtraHead(self):
            return [
                {'name':'com__name','label':'公司名称'}
            ]

class MyJobinfoList(ModelTableMobile):
    "我的发布"
    model = JobInfo
    exclude = []
    nolimit=True
    fields_sort=['position','status']
    
    def dict_head(self, head):
        if head['name'] =="position":
            head['css'] ='''
        .xxx{white-space: nowrap;
            max-width: 5.2rem;
            overflow: hidden;
            text-overflow: ellipsis;} '''
            head['class'] ='xxx'
        if head['name'] =='status':
            head['css']='''
            .offline{color:#b4b4b4}
            .online{color:#15dd15}
            '''
            head['class_express'] ='scope.row.status==1?"online":"offline"'
        return head
    
    #def dict_row(self, inst):
        #return { '_director_name':'jobinfoform'}
    
    def inn_filter(self, query):
        return query.filter(com=self.crt_user.companyinfo).order_by('-update_time')
    
    def get_operation(self):
        return []

class CompanySJobApplyList(ModelTableMobile):
    model = ApplyRecord
    exclude = []
    nolimit = True
    
    def inn_filter(self, query):
        return query.filter(job__com__user = self.crt_user)
    
    class filters(RowFilter):
        names=['status']
    

class WorkerSJobApplyList(ModelTableMobile):
    model = ApplyRecord
    exclude =[]
    nolimit = True
    def inn_filter(self, query):
        return query.filter(worker = self.crt_user.workinfo).annotate(company=F('job__com__name'))
    
    def dict_row(self, inst):
        return {
            'company':inst.company
        }


@director_view('job.apply_work')
def apply_work(pk):
    user=get_request_cache()['request'].user
    job = JobInfo.objects.get(pk=pk)
    ApplyRecord.objects.create(worker= user.workinfo,job= job)
  
@director_view('job.apply_status')
def apply_status(pk):
    user=get_request_cache()['request'].user
    job = JobInfo.objects.get(pk=pk)
    if getattr(user,'workinfo') and user.workinfo.status ==2:
        if ApplyRecord.objects.filter(worker = user.workinfo,job = job).exists():
            out = 'applyed'
        else:
            out = 'can_apply'
    else:
        out = 'need_workinfo'
    return out

director.update({
    'jobinfo':JobInfoPage.tableCls,
    'jobinfo.edit':JobinfoForm,
   
    'jobinfolist':JobinfUserList,
    'MyJobinfoList':MyJobinfoList,
    'MyJobinfoList.edit':JobinfoUserForm,
    'company_job_apply_list':CompanySJobApplyList,
    'worker_s_job_apply_list':WorkerSJobApplyList,
    
    'workerTab':WorkerTab,
     #'jobinfoform':JobinfoUserForm,
})
page_dc.update({
    'jobinfo':JobInfoPage
})