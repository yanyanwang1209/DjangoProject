from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def login_view(request):
    # return HttpResponse('login success')
    return render(request, 'login.html')