from django.db import models
from datetime import date
from django import forms
# Create your models here.
INTEGER_CHOICES= [tuple([x,x]) for x in range(0,101)] #tuples (0,0) to (100,100)
class Myself(models.Model):#Me
    image = models.ImageField(upload_to='images/') #image of self
    position = models.CharField(max_length=75, blank = True) #position name, can be blank
    summary = models.TextField(blank = True) #summary of position
class Education(models.Model): #educations
    institution = models.CharField(max_length = 75) #school name
    gpa = models.FloatField() #GPA
    start_date = models.DateField() #start date
    end_date = models.DateField(blank=True, null=True) #end date, can be blank
    summary = models.TextField() # summary of activities
    type = models.CharField(max_length = 30) #type of education, e.g. high school diploma, bachelors, masters, etc
class Skill(models.Model): #Skills, languages, etc
    language = models.CharField(max_length = 30) #skill name
    comfort = models.IntegerField(choices=INTEGER_CHOICES) #comfort level, 0-100
class Job(models.Model): #Jobs
    company = models.CharField(max_length = 75) # company
    position = models.CharField(max_length = 75) # position
    summary = models.TextField() # job summary
    start_date = models.DateField() #start date
    end_date = models.DateField(blank=True, null=True) #end date, can be blank
