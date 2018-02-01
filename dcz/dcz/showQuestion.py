#-*-coding:utf-8-*-
from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect
from dc.models import hrmresource
from dc.models import sales
from dc.models import qa
# from dc.models import uexam
import random
import time
import os
import configparser
# 读取配置文件
config = configparser.ConfigParser()
config.read("config.ini")

"""
    每日一题
"""
def mryt(request):
    config.read("config.ini")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM dc_qa')
    list = cursor.fetchall()
    list_show = []

    for i in list:
        dic = {'question':i[1],'opr_1':i[2],'opr_2': i[3],'opr_3':i[4],'opr_4':i[5],'opr_5':i[6],'opr_6':i[7], 'analysis':i[9],'beizhu': i[11], 'answer':i[14]}
        list_show.append(dic)

    # 根据日期读取今日是哪道题
    getLastDate = config.get("question", "update_date")
    nowdate = str(time.strftime("%Y-%m-%d", time.localtime(time.time())))
    # 从哪道题开始
    startNumber = 1
    # 从哪里结束
    endNumber = 2
    the_number_of_daily_questions = int(config.get("question", "the_number_of_daily_questions"))
    if getLastDate == nowdate:
        endNumber = int(config.get("question", "last_questionID"))
        startNumber = endNumber - the_number_of_daily_questions + 1
        if startNumber < 1:
            startNumber = 1
            endNumber = the_number_of_daily_questions
    else:

        startNumber = int(config.get("question", "last_questionID")) + 1
        endNumber = the_number_of_daily_questions + startNumber -1
        if startNumber > int(list_show.__len__()):
            startNumber = 1
            endNumber = the_number_of_daily_questions
        if endNumber > int(list_show.__len__()):
            endNumber = list_show.__len__()
        config.set("question", "update_date", str(nowdate))
        config.set("question", "last_questionID", str(endNumber))
        config.write(open("config.ini", "w"))

    list_show = list_show[startNumber-1:endNumber]


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
    if list_show.__len__() > int(config.get("question", "random_number")):
        list_show = random.sample(list_show, int(config.get("question", "random_number")))
    for i in range(0,list_show.__len__()):
        if i==list_show.__len__()-1 or list_show.__len__()==1:
            qaID += str(list_show.__getitem__(i)['id'])
        else:
            qaID += str(list_show.__getitem__(i)['id'])+','
    return render(request, 'showQuestion.html', {'userName': userName, 'userID': userID, 'qaID': qaID, 'list': list_show})