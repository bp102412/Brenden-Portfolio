from django.shortcuts import render, get_object_or_404

#import all models from models file that are needed in any view
from .models import Framework, Language, JobNoFramework, JobYesFramework, Me

# Create your views here.
def home(request): #home page
    languages = Language.objects #all language objects from db
    me = get_object_or_404(Me, pk=1) #get the only me object out of the db (primary key = 1)
    return render(request, 'home.html',{'languages':languages, 'me':me}) #return the request, render home.html, pass languages as languages and me as me
def lang_detail(request, lang_id): #Page when a language is clicked on, takes the pk of the language selected as an argument
    language = get_object_or_404(Language, pk=lang_id) # get the language out of db or a 404
    projects = JobNoFramework.objects # all projects without a framework, I filter for the correct language within the template
    frameworks = Framework.objects #all frameworks, filter within template
    return render(request, 'language.html', {'languages':language, "projects":projects, "frameworks":frameworks}) #render language.html and pass projects and frameworks
def frame_detail(request, frame_id): # page when a framework is selected, takes the pk of that framework as an argument
    framework = get_object_or_404(Framework, pk=frame_id) #get that specific framework page or a 404 page
    projects = JobYesFramework.objects # get all projects with frameworks, filter in template
    return render(request, 'framework.html', {"projects":projects, "framework":framework}) #render framework.html, passing the framework and projects

#The Following two views are the same, they just reference a different table in the db to pull up the correct page
def project_detail(request, project_id): #project with no framework
    project_detail = get_object_or_404(JobNoFramework, pk=project_id) #get the project from JobNoFramework or 404
    return render(request, 'detail.html', {'project_detail':project_detail}) #render detail.html and pass it the project
def framework_project_detail(request, project_id): #project with a framework
    project_detail = get_object_or_404(JobYesFramework, pk=project_id) #get the project from JobYesFramework or a 404
    return render(request, 'detail.html', {'project_detail':project_detail}) #render detail.html and pass it the project
