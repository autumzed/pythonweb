from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from . import view
from django.http import HttpResponseRedirect
from dc.models import hrmresource

def doLoginAction(request):

    if request.POST:
        getName = request.POST['username']
        password = request.POST['password']

        if getName and password:
            try:
                checkhrm = hrmresource.objects.get(uaccount=getName)
            except Exception as e:
                return render(request, 'loginPage.html', {'message': '用户名或密码无效'})
            if checkhrm is None:
                return render(request, 'loginPage.html', {'message': '用户名或密码无效'})
            if checkhrm.upws == password:
                request.session['user'] = checkhrm.uname
                request.session['userID'] = checkhrm.id
                return HttpResponseRedirect("/showQuestion/")
            else:
                request.session['user'] = None
                return render(request, 'loginPage.html', {'message': '用户名或密码无效'})
        else:
            request.session['user'] = None
            return render(request, 'loginPage.html', {'message': '请输入正确的用户名和密码'})
    else:
        request.session['user'] = None
        return render(request, 'loginPage.html', {'message': '请输入正确的用户名和密码'})
