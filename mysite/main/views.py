from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    #print(args, kwargs)
    print(request.user)
    return render(request,"index.html", {})

def aboutme_view(request, *args, **kwargs):
    return render(request,"aboutme.html", {})

def techskills_view(request, *args, **kwargs):
    return render(request,"technical_skills.html", {})

def profskills_view(request, *args, **kwargs):
    return render(request,"professional_skills.html", {})

def projects_view(request, *args, **kwargs):
    return render(request,"projects.html", {})

def contact_view(request, *args, **kwargs):
    return render(request,"contact.html", {})