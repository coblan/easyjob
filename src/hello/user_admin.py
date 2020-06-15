from helpers.case.jb_admin.admin_user import UserPage,UserFields
from helpers.director.shortcut import page_dc,director,has_permit,RowFilter

#from maindb.models import TbMerchants
from django.contrib.auth.models import User,Group


class EasyJobUser(UserPage):
    class tableCls(UserPage.tableCls):
        #'first_name', 'groups'
        fields_sort = ['username','company','worker','is_superuser','is_staff','is_active','last_login']
        
        def getExtraHead(self):
            return [
                {'name':'company','label':'认证商家名','editor':'com-table-span','width':150},
                {'name':'worker','label':'认证个人名','editor':'com-table-span','width':100},
            ]
        
       
        def dict_row(self, inst):
            return {
                'company':str(getattr( inst,'companyinfo','') ),
                'worker':str(getattr(inst,'workinfo',''))
            }
        
        def inn_filter(self, query):
            if self.search_args.get('usertype') =='other':
                query = query.exclude(companyinfo__status=2,workinfo__status=2)
            elif self.search_args.get('usertype') =='company':
                query = query.filter(companyinfo__status=2)
            elif self.search_args.get('usertype') =='worker':
                query = query.filter(workinfo__status=2)
            return query
        
        #def inn_filter(self, query):
            #self.merchant_map = {x.pk:str(x) for x in TbMerchants.objects.all() }
            #query = super().inn_filter(query)
            #if self.crt_user.merchant:
                #query = query.filter(userprofile__merchantid = self.crt_user.merchant.id)
            #query = query.filter(userprofile__merchantid__isnull=False)
            #return query.select_related('userprofile')
        
        #def dict_row(self, inst):
            #return {
                #'merchantid': inst.userprofile.merchantid if getattr(inst,'userprofile',None) else '',
                #'_merchantid_label':self.merchant_map[ inst.userprofile.merchantid ]
            #}
         
        #def get_heads(self):
            #heads = super().get_heads()
            #if self.crt_user.merchant:
                #out_heads = []
                #for head in heads:
                    #if head['name'] != 'is_superuser':
                        #out_heads.append(head)
            #else:
                #out_heads = heads
            #return out_heads
        
        #def getExtraHead(self):
            #heads = super().getExtraHead()
            #heads.extend([
                #{'name':'merchantid','label':'商户','editor':'com-table-label-shower'},
            #])
            #return heads
        
        class filters(RowFilter):
            # 'groups__name',
            names=['first_name','is_superuser','is_staff','is_active']
            #icontains=['first_name','groups__name']
            icontains=['first_name']
            
            def getExtraHead(self):
                return [
                    {'name':'usertype','label':'用户类型','editor':'com-filter-select','options':[
                        {'value':'company','label':'公司认证账号'},
                        {'value':'worker','label':'个人认证账号'},
                        {'value':'other','label':'其他账号'},
                        ]},
                    #{'name':'groups__name','label':'权限分组','show':'!scope.ps.search_args.groups_id'},
                ]
            

class EasyJobUserForm(UserFields):
    class Meta:
        model=User
        fields=['username','is_active','is_staff', 'date_joined'] #'groups',
        
    #def getExtraHeads(self):
        #extra_ls = super().getExtraHeads()
        #if not getattr(self.crt_user,'userprofile',None):
            #extra_ls.extend([
                #{'name':'merchantid','label':'商户号','required':True,'editor':'com-field-select','options':[
                    #{'value':x.pk,'label':str(x)} for x in TbMerchants.objects.all()
                    #]}
            #])
        #return extra_ls
    
    #def dict_head(self, head):
        #if head['name'] =='username':
            #if getattr(self.crt_user,'userprofile',None):
                #merchant = TbMerchants.objects.get(id=self.crt_user.userprofile.merchantid)
                #head['prefix'] = merchant.merchantname + '_'
                #head['class']='merchant-username'
                #head['css']='.merchant-username input{width:19rem !important;}'
            ##head['on_mounted'] = '''if(! scope.vc.row.pk){ Vue.set( scope.vc.head,'prefix','bba')  } '''
            #head['readonly']='Boolean( scope.row.pk )'
        #if head['name'] =='groups':
            #head['options']=[
                #{'value':x.pk,'label':str(x)} for x in Group.objects.filter(name__startswith='商户-')
            #]
        
        #return head
    
    #def clean_dict(self, dc):
        #dc = super().clean_dict(dc)
        #if self.crt_user.merchant and not dc.get('pk') and dc.get('username'):
            #merchant = TbMerchants.objects.get(id=self.crt_user.userprofile.merchantid)
            #dc['username'] = merchant.merchantname + '_' + dc.get('username')
        #return dc
    
    #def after_save(self):
        #merchantid = self.kw.get('merchantid')
        #if self.crt_user.merchant:
            #merchantid = self.crt_user.userprofile.merchantid
        #if merchantid:
            #count = UserProfile.objects.filter(user = self.instance).update(merchantid= merchantid)
            #if not count:
                #UserProfile.objects.create(user = self.instance,merchantid = merchantid)
    
    #def dict_row(self, inst):
        #dc = super().dict_row(inst) 
        #if self.instance.pk:
            #self.instance.refresh_from_db()
            #if hasattr(self.instance,'userprofile'):
                #merchant = TbMerchants.objects.get(pk=self.instance.userprofile.merchantid )
                #dc.update({
                    #'merchantid': self.instance.userprofile.merchantid,
                    #'_merchantid_label':str(merchant)
                #})
        #return dc

director.update({
    'easyjob_user':EasyJobUser.tableCls,
    'easyjob_user.edit':EasyJobUserForm
})

page_dc.update({
    'easyjob_user':EasyJobUser
})