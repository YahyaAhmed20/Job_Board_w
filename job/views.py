from audioop import reverse
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from .models import Job
from django.contrib.auth.decorators import login_required

# Create your views here.

def jop_list(request):
    job_list=Job.objects.all()
    paginator = Paginator( job_list, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'job_list':page_obj}
    return render(request,'job/job_list.html',context)

def jop_detail(request,id):

    job_detail=Job.objects.get(id=id)
    context={'job_detail':job_detail}
    return render(request,'job/job_detils.html',context)
   

