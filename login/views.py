from django.shortcuts import render

from login.models import Login
# Create your views here.

def index(request):
    user=Login.objects.all()
    context = {'user': user}
    return render(request,'login/index.html',context)
