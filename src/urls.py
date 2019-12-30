"""easyjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from hello.engin_menu import MBpageEngine,PcMenu
from django.views.generic import RedirectView 
from helpers.authuser.engin_view import AuthEngine
from helpers.director.views import director_view

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^accounts/([\w\.]+)/?$',AuthEngine.as_view(),name=AuthEngine.url_name),
    url(r'^pc/([\w\.]+)/?$',PcMenu.as_view(),name=PcMenu.url_name),
    url(r'^d/',include('helpers.director.urls'),name='director'),
    url(r'^mb/([\w\.]+)/?$',MBpageEngine.as_view(),name=MBpageEngine.url_name),
    url(r'^dapi/(?P<director_name>[\w\/\.-]+)?/?$',director_view),
    url(r'^pc/?$',RedirectView.as_view(url='/pc/jobinfo')) ,
    url(r'^$',RedirectView.as_view(url='/mb/index')) ,
]
