from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.signin, name='login'),
    path('tempo', views.tempo, name='tempo'),
    path('logout', views.loggedoff, name='logout'),
    path('timesheet', views.timesheet, name = "timesheet"),
    path('kvm',views.kvm, name = "kvm"),
    #path('register',views.signup,name='register')
]
