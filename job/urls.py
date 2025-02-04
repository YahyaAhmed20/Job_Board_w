from django.urls import path,include
from . import views
from . import api
app_name='job'

urlpatterns = [
    path('',views.jop_list,name='job_list'), 
    path('add/', views.add_job,name='add_job'),
    path('<str:slug>', views.job_detail,name='job_detils'),
    
    

    #API 
    path('api/list/<int:id>', api.Job_List_Api.as_view(), name='Job_List_Api'),
    path('api/list/v2/', api.Job_Create_Api.as_view(), name='Job_Create_Api'),
    

]
