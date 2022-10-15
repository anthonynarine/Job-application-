from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

job_title = [
    "First Job",
    "Second Job",
    "Thrid Job"
]


job_description = [
    "First job description",
    "Second job description",
    "Third job description",
]


def job_list(request):
    """"will iterate over job_title[] and display each job on the home page"""
    list_of_job = "<ul>"
    for j in job_title:
        job_id = job_title.index(j) #the index of j is being saved as job_id then its passed as a url below
        detail_url = (reverse("jobs_detail", args=(job_id,)))
        list_of_job += f"<li><a href='{detail_url}'>{j}</a></li>" #<a href'job/{job_id}'></a> is a hyperlink
    list_of_job += "</ul>"
    return HttpResponse(list_of_job)



def job_detail(request, id):

    try:
        if id == 0:
            return redirect(reverse("jobs_home"))  #this will redirect the user to the home screen. 
        return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}"
        return HttpResponse(return_html)
    except:
        return HttpResponseNotFound("Not found")