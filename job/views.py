from audioop import reverse
from .filters import JobFilter
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from .models import Job
from .forms import ApplyForm,Jobform
from django.contrib import messages


from django.contrib.auth.decorators import login_required

# Create your views here.

def jop_list(request):
    job_list=Job.objects.all()
    myfilter=JobFilter(request.GET,queryset=job_list)
    job_list=myfilter.qs
    paginator = Paginator(job_list,10) 
    page_number = request.GET.get('page')
    job_list = paginator.get_page(page_number)
    context={'job_list':job_list,'myfilter':myfilter}
    return render(request,'job/job_list.html',context)

def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)
    context = {'job_detail': job_detail}  # Define context outside the else block

    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
            messages.success(request, 'Applying for the job was successful!')
            request.session['show_message'] = True  # Set session variable

            return redirect('jobs:job_list')
    else:
        form = ApplyForm()

    context['form'] = form  # Update the context with the 'form' variable
    
    # In your Django view
    request.session.pop('show_message', None)


    return render(request, 'job/job_detils.html', context)


@login_required
def add_job(request):
    if request.method=='POST':
        form=Jobform(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
            
            messages.success(request, 'Congratulations! The job has been successfully posted. We look forward to receiving qualified candidates!')
            request.session['show_message'] = True  # Set session variable
            return redirect('jobs:job_list')


            
    else:
        form=Jobform()
        
    context = {
            
        'form1':form
         
        }
    request.session.pop('show_message', None)

    
    return render(request,'job/add_job.html',context)

