from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_list_or_404, render
from jobs.models import Jobs
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from jobs.forms import Jobform
from django.urls import reverse_lazy


#from django.http import Http404
# Create your views here.
#def index(request):
 #   try:
  #     jobs=Jobs.objects.all()
   # except Jobs.DoesNotExist:
    #   raise Http404("Error: does not exist")
    #return render(request,"jobs/index.html",context)


#def index(request):
 #   jobs=get_list_or_404(Jobs)
  #  return render(request,"jobs/index.html",{'jobs':jobs})

class JobList(ListView):
   # model=Jobs
    context_object_name="jobs"
    template_name="jobs/base.html"

   # template_name="jobs/index.html"
    
    def get_queryset(self):
        return Jobs.objects.all()
    
    
class JobDetailView(DetailView):
    model = Jobs
            #context_object_name="detailjob"
    template_name= "jobs/jobs_detail.html"
    

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["light"]="breaktime"
        return context



class JobsCreateView(CreateView):
     model=Jobs
     template_name="jobs/jobs_form.html"
     success_url=reverse_lazy('jobs:index')



class JobsUpdateView(UpdateView):
     model=Jobs
     form_class=Jobform
     template_name="jobs/jobs_form.html"
     success_url=reverse_lazy('jobs:index')

    

class JobsDeleteView(DeleteView):
    model=Jobs
    template_name="jobs/jobs_form.html"
    success_url=reverse_lazy('jobs:index')
