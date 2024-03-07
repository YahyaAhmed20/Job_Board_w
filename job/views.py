from audioop import reverse
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from .models import Job
from django.contrib.auth.decorators import login_required

# Create your views here.

def jop_list(request):
    job_list=Job.objects.all()
    paginator = Paginator( job_list, 1) 
    page_number = request.GET.get('page')
    job_list = paginator.get_page(page_number)
    context={'job_list':job_list}
    return render(request,'job/job_list.html',context)

def jop_detail(request,slug):

    job_detail=Job.objects.get(slug=slug)
    context={'job_detail':job_detail}
    return render(request,'job/job_detils.html',context)
   