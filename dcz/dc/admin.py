from django.contrib import admin
from dc.models import qa,hrmresource,sales,ns

class QQA(admin.ModelAdmin):
    list_display = ('question', 'opr_1', 'opr_2', 'opr_3', 'opr_4', 'opr_5', 'answer', 'analysis')
    fields = ('question', 'opr_1', 'opr_2', 'opr_3', 'opr_4', 'opr_5',  'answer','analysis')
    search_fields = ('question', 'opr_1', 'opr_2', 'opr_3', 'opr_4', 'opr_5',  'answer','analysis')


class Qhr(admin.ModelAdmin):
    list_display = ('zyear', 'zdate', 'schoolname', 'zcity', 'uname', 'tel', 'uaddress', 'zpostcode', 'ubank', 'uid', 'uqq', 'uaccount', 'upws','uwechat', 'denum', 'idcopy', 'ptype', 'birth')
    fields = ('zyear', 'zdate', 'schoolname', 'zcity', 'uname', 'tel', 'uaddress', 'zpostcode', 'ubank', 'uid', 'uqq', 'uaccount', 'upws','uwechat', 'denum', 'idcopy', 'ptype', 'birth')
    search_fields = ('zyear', 'zdate', 'schoolname', 'zcity', 'uname', 'tel', 'uaddress', 'zpostcode', 'ubank', 'uid', 'uqq', 'uaccount', 'upws','uwechat', 'denum', 'idcopy', 'ptype', 'birth')

class Qsales(admin.ModelAdmin):
    list_display = ('uid', 'uname', 'product', 'ztype', 'ucount', 'uamt', 'zbsamt', 'splace', 'snote', 'fprestored', 'channel')
    fields = ('uid', 'uname', 'product', 'ztype', 'ucount', 'uamt', 'zbsamt', 'splace', 'snote', 'fprestored', 'channel')
    search_fields = ('uid', 'uname', 'product', 'ztype', 'ucount', 'uamt', 'zbsamt', 'splace', 'snote', 'fprestored', 'channel')

class Qns(admin.ModelAdmin):
    list_display = ('opr_1', 'imp_1', 'ty_1', 'beizhu')
    fields = ('opr_1', 'imp_1', 'ty_1', 'beizhu')
    search_fields = ('opr_1', 'imp_1', 'ty_1', 'beizhu')


admin.site.register(hrmresource, Qhr)
admin.site.register(qa, QQA)
admin.site.register(sales, Qsales)
admin.site.register(ns, Qns)