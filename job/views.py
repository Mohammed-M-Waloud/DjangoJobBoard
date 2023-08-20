from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm
from .form import AddJobform
# Create your views here.



def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list,5)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj}
    return render(request, 'job/job_list.html', context)  


def job_details(request , slug):  
    job_details = Job.objects.get(slug=slug)
    if request.method=="POST":
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user  # Assign the authenticated user as the owner
            myform.job = job_details
            myform.save()
            return redirect(reverse('jobs:job_list'))  # Redirect to job list or another appropriate page

    else:
        form = ApplyForm()

    context = {'job': job_details, 'form': form} 
    return render(request, "job/job_details.html", context) 


def add_job(request):
    if request.method == "POST":
        form = AddJobform(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user  # Assign the authenticated user as the owner
            myform.slug = myform.title
            myform.save()
            return redirect(reverse('jobs:job_list'))  # Redirect to job list or another appropriate page
    else:
        form = AddJobform()
    return render(request, 'job/add_job.html', {'form1': form})