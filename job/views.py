from audioop import reverse
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from .models import Job
from .forms import ApplyForm
from django.contrib import messages


from django.contrib.auth.decorators import login_required

# Create your views here.

def jop_list(request):
    job_list=Job.objects.all()
    paginator = Paginator( job_list, 2) 
    page_number = request.GET.get('page')
    job_list = paginator.get_page(page_number)
    context={'job_list':job_list}
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

            return redirect('/')
    else:
        form = ApplyForm()

    context['form'] = form  # Update the context with the 'form' variable
    
    # In your Django view
    request.session.pop('show_message', None)


    return render(request, 'job/job_detils.html', context)
