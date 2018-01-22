from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from . import view
from django.http import HttpResponseRedirect


def doLoginAction(request):

    if request.POST:
        getName = request.POST['username']
        password = request.POST['password']
        if getName:
            request.session['user'] = getName
            request.session['userID'] = getName
            print(getName)
            return HttpResponseRedirect("/showQuestion/")
    else:
        request.session['user'] = None
        return render(request, 'login.html')
