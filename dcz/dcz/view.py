#-*-coding:utf-8-*- 
from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect
from dc.models import hrmresource
from dc.models import sales
from dc.models import qa
# from dc.models import uexam
import random

def uin(request):
    ctx = {}
    ctx['返回状态'] = "未提交"
    if request.POST:
        try:
            zyear_1 = request.POST['zyear']
            zdate_1= request.POST['zdate']
            schoolname_1=request.POST['schoolname']
            zcity_1=request.POST['zcity']
            uname_1=request.POST['uname']
            tel_1= request.POST['tel']
            uaddress_1=request.POST['uaddress']
            zpostcode_1=request.POST['zpostcode']
            ubank_1=request.POST['ubank']
            uid_1=request.POST['uid']
            uqq_1=request.POST['uqq']
            uaccount_1=request.POST['uaccount']
            upws_1 = request.POST['upws']
            uwechat_1 = request.POST['uwechat']
            denum_1 = request.POST['denum']
            idcopy_1 = request.POST['idcopy']
            ptype_1 = request.POST['ptype']
            birth_1 = request.POST['birth']

            db = hrmresource(zyear=zyear_1,zdate=zdate_1,schoolname=schoolname_1,zcity=zcity_1,uname=uname_1,tel=tel_1,uaddress=uaddress_1,zpostcode=zpostcode_1,ubank=ubank_1,uid=uid_1,uqq=uqq_1,uaccount=uaccount_1,upws=upws_1,uwechat=uwechat_1,denum=denum_1,idcopy=idcopy_1,ptype=ptype_1,birth=birth_1)
            db.save()
            ctx['返回状态'] = "成功！"
        except:
            ctx['返回状态'] = "失败！"

    return render(request, 'uin.html',ctx)


def sin(request):
    ctx = {}
    ctx['返回状态'] = "未提交"
    if request.POST:
        try:
            uid_1 = request.POST['uid']
            uname_1 = request.POST['uname']
            product_1=request.POST['product']
            zcity_1=request.POST['zcity']
            ucount_1=request.POST['ucount']
            uamt_1= request.POST['uamt']
            zbsamt_1=request.POST['zbsamt']
            splace_1=request.POST['splace']
            snote_1=request.POST['snote']
            fprestored_1=request.POST['fprestored']
            channel_1 = request.POST['channel']
            db = sales(uid=uid_1,uname=uname_1,product=product_1,zcity=zcity_1,ucount=ucount_1,uamt=uamt_1,zbsamt=zbsamt_1,splace=splace_1,snote=snote_1,fprestored=fprestored_1,channel=channel_1)
            db.save()
            ctx['返回状态'] = "成功！"
        except:
            ctx['返回状态'] = "失败！"

    return render(request, 'sin.html',ctx)


def getsql(request):
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM dc_hrmresource LEFT JOIN dc_sales ON dc_hrmresource.uid=dc_sales.uid')
    list = cursor.fetchall()
    list_show = []

    for i in list:
        dic = {'zdate': i[2],'shoolname':i[3],'zcity':i[4],'uname': i[5],'tel':i[6],'uaddress':i[7],'zpostcode':i[8],'product':i[28], 'ztype':i[29],'ucount':i[30],'uamt':i[31],'ubank':i[9],'splace':i[33],'uid': i[10],'uqq':i[11],'snote':i[34],'yc':i[35],'uaccount':i[12],'upws':i[13],'denum':i[15],'wx':i[14],'channel':i[36],'icopy':i[16],'ptype':i[17]}

        list_show.append(dic)
    date = {}
    date['list'] = list_show
    return render(request, 'show.html', {'list': list_show})

"""
    每日一题
"""
def mryt(request):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM dc_qa')
    list = cursor.fetchall()
    list_show = []

    for i in list:
        dic = {'question':i[1],'opr_1':i[2],'opr_2': i[3],'opr_3':i[4],'opr_4':i[5],'opr_5':i[6],'opr_6':i[7], 'analysis':i[9],'beizhu': i[11], 'answer':i[14]}
        list_show.append(dic)
    date = {}
    date['list'] = list_show
    return render(request, 'mryt.html', {'list': list_show})
"""
随机N题
"""
def sjnt(request):
    # 判断用户是否登陆
    userName = request.session.get("user", default=None)
    userID = request.session.get("userID", default=None)
    if not (userName or userID):
        return render(request, 'login.html')

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM dc_qa')
    list = cursor.fetchall()
    list_show = []
    qaID = ''
    for i in list:
        dic = {"id":i[0],'question': i[1], 'opr_1': i[2], 'opr_2': i[3], 'opr_3': i[4], 'opr_4': i[5], 'opr_5': i[6],
               'opr_6': i[7], 'analysis': i[9], 'beizhu': i[11], 'answer': i[14]}
        list_show.append(dic)
    # 从show里面随机取出N个
    if list_show.__len__() > 3:
        list_show = random.sample(list_show, 3)
    for i in range(0,list_show.__len__()):
        if i==list_show.__len__()-1 or list_show.__len__()==1:
            qaID += str(list_show.__getitem__(i)['id'])
        else:
            qaID += str(list_show.__getitem__(i)['id'])+','
    return render(request, 'showQuestion.html', {'userName': userName, 'userID': userID, 'qaID': qaID, 'list': list_show})


def zsjz(request):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM dc_ns WHERE ty_1=1')
    list = cursor.fetchall()
    list_show = []
    ctx = {}
    for i in list:
        dic = {'opr_1':i[1],'img_1':i[2]}
        ctx['d1'] = i[2]
        list_show.append(dic)
    date = {}
    date['list'] = list_show
    return render(request, 'zsjz.html', ctx)


def fxhd(request):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM dc_ns WHERE ty_1=2')
    list = cursor.fetchall()
    list_show = []
    ctx = {}
    for i in list:
        dic = {'opr_1':i[1],'img_1':i[2]}
        ctx['d2'] = i[2]
        list_show.append(dic)
    date = {}
    date['list'] = list_show
    return render(request, 'fxhd.html', ctx)


def zxgg(request):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM dc_ns WHERE ty_1=3')
    list = cursor.fetchall()
    list_show = []
    ctx = {}
    for i in list:
        dic = {'opr_1':i[1],'img_1':i[2]}
        ctx['d3'] = i[2]
        list_show.append(dic)
    date = {}
    date['list'] = list_show

    # ctx['图片地址']=""
    return render(request, 'zxgg.html', ctx)
