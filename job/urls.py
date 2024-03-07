from django.urls import path,include
from . import views
app_name='job'

urlpatterns = [
    path('',views.jop_list ),
    path('<str:slug>', views.jop_detail,name='job_detils'),

]
