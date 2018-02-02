from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from . import view
from django.http import HttpResponseRedirect
from dc.models import qa,qa_record

def doScoringAction(request):
    # 分数计算

    if request.POST:
        # 获取登陆者id
        get_uid = request.POST['userid']
        # 检测是否已经提交过
        token = request.POST['token']
        if token==request.session.get("token", default=None):
            return render(request, 'thankingPage.html', {'message': '请勿重复提交！'})
        # 获取都是那些题目
        org_qaids = request.POST['qaid']
        qaids = org_qaids.split(',')

        # 获取所有题的答案
        answer = dict(qa.objects.values_list('id', 'answer'))
        weighted = dict(qa.objects.values_list('id', 'weighted'))
        record = {}
        result = {}
        select = ""
        score = 0
        # 获取每道题的答案

        for i in qaids:
            if i in request.POST:
                record.setdefault(i, request.POST[i])
                if i is qaids[qaids.__len__() - 1]:
                    select += request.POST[i]
                else:
                    select += request.POST[i] + ","
            else:
                record.setdefault(i, "N")
                if i is qaids[qaids.__len__() - 1]:
                    select += "N"
                else:
                    select += "N" + ","

        # 遍历，校对答案是否正确
        for key in record:
            if record.get(key) == answer.get(int(key)):
                result.setdefault(key, True)
                score += 1 * weighted.get(int(key))
            else:
                result.setdefault(key, False)
        qa_re = qa_record(uid=get_uid, questionIDs=org_qaids, select=select, test_score=score, type=1)
        qa_re.save()
        # 保存
        session_id_page = {get_uid: ''}
        request.session["token"] = token
    return render(request, 'thankingPage.html', {'message': '你好，您的分数是%s分'%score})
