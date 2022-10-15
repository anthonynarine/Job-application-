from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Lets get you grinding homie")

#"<domain>/job1" --> job detail page **create this url
def job_detail(request):
    return HttpResponse("Job detail page")