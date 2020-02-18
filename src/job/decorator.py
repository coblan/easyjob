from helpers.director.decorator import get_request_cache
from django.shortcuts import redirect

def need_com(fun):
    def _fun(*args,**kws):
        user = get_request_cache()['request'].user
        if getattr(user,'companyinfo') and user.companyinfo.status==2:
            return fun(*args,**kws)
        else:
            return redirect('/mb/need_com')
    return _fun



def need_worker_cert(fun):
    def _fun(*args,**kws):
        user = get_request_cache()['request'].user
        if getattr(user,'workinfo')and user.workinfo.status==2:
            return fun(*args,**kws)
        else:
            return redirect('/mb/need_worker_cert')
    return _fun