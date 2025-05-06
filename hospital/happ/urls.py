from django.contrib import admin
from django.urls import path
from happ import views

urlpatterns = [

    path('',views.index,name='index'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('patienthome',views.patienthome,name='patienthome'),
    path('doctorhome',views.doctorhome,name='doctorhome'),
    path('reg_patient',views.reg_patient,name='reg_patient'),
    path('reg_doctor',views.reg_doctor,name='reg_doctor'),
    path('dep_add',views.dep_add,name='dep_add'),
    path('viewpatients',views.viewpatients,name='viewpatients'),
    path('viewdoctors',views.viewdoctors,name='viewdoctors'),
    path('logins',views.logins,name='logins'),
    path('lgout',views.lgout,name='lgout'),
    path('page',views.page,name='page'),
    path('log',views.log,name='log'),
    path('updatepat/', views.updatepat, name='updatepat'),
    path('updatepatient/<int:uid>/', views.updatepatient, name='updatepatient')







]