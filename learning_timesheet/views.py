from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import Timesheet_Data, KVM_data

@never_cache
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
    return render(request,'login.html')

@never_cache
@login_required(login_url='login')
def tempo(request):
    return render(request,'main.html')

def loggedoff(request):
    logout(request)
    return redirect('login')


def timesheet(request):
    if request.method == "POST":
        ts = request.POST.get('timesheet_date')
        print(type(ts))
        un = request.user
        wd = request.POST.get('time_utilized_ws')
        wd1 = request.POST.get('time_utilized_rs')
        wd2 = request.POST.get('time_utilized_report')
        mt = request.POST.get('time_utilized_meeting')
        ml = request.POST.get('time_utilized_mail')
        t = Timesheet_Data(user=un, date=ts,time_utilised_ws=wd,time_utilised_rs=wd1,time_utilised_rp=wd2,time_utilised_mt=mt,time_utilised_ml=ml)
        t.save()

        print(ts)
        print(wd)
        print(mt)
        print(ml)
        print(wd1)
        print(wd2)

    return render(request, 'timesheet_new.html')

def kvm(request):
    if request.method == "POST":
        month = request.POST.get('month_value')
        un = request.user
        ss = datetime.strptime(month,"%Y-%m-%d")
        abc = ss.strftime("%B")
        ls = request.POST.get('ls')
        lr = request.POST.get('lr')
        dr = request.POST.get('dr')
        tat = request.POST.get('tat')
        A = KVM_data(user = un, month=abc,link_scraped=ls,link_resolved=lr,days_to_reply=dr,average_tat=tat)
        A.save()
        print(ls)
        print(lr)
        print(dr)
        print(tat)

    return render(request, 'kvm.html')
