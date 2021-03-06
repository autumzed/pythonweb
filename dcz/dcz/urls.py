"""dcz URL Configuration

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
from django.conf.urls import *
from django.contrib import admin
from . import view, loginHandler, scoring, showQuestion

urlpatterns = [
    url(r'^index/', view.getsql),
    url(r'^admin/', admin.site.urls),
    # url(r'^testdb/', testdb.testdb),
    url(r'^uin/', view.uin),
    url(r'^sin/', view.sin),
    url(r'^mryt/', showQuestion.mryt),
    url(r'^showQuestion/', showQuestion.sjnt),
    url(r'^zsjz/', view.zsjz),
    url(r'^fxhd/', view.fxhd),
    url(r'^zxgg/', view.zxgg),
    url(r'^login/', loginHandler.doLoginAction),
    url(r'^thankingPage/', scoring.doScoringAction),

    #url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}), 
]

