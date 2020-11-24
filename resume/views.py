from django.shortcuts import render
from .models import Myself, Skill, Education, Job
#import models from resume models
# Create your views here.
def home(request): #resume only has a home page
    me = Myself.objects #all me objects
    skill = Skill.objects.order_by('-comfort') #skill objects, ordered by comfort. Higher numbers first
    edu = Education.objects.order_by('-end_date', 'start_date') #education objects ordered by latest end date, then latest start date
    job = Job.objects.order_by('-end_date', 'start_date') # jobs ordered by end date, then start date
    return render(request, 'resume.html', {'me':me,'skill':skill, 'edu':edu, 'job':job}) #render resume.html, pass me, skill, edu, and job
