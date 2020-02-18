from django.contrib import admin

# Register your models here.
from . import js_cfg
from .pages import home
from .pages import com_cert
from .pages import com_release
from .pages import need_com
from .pages import need_worker_crt
from .pages import worker_cert
from .pages import worker_release

from . import admin_jobinfo
from . import admin_companyinfo
from . import admin_workinfo
from . import admin_seekjob