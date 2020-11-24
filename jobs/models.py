from django.db import models
from datetime import date
# Create your models here. This is what will define the database schema, using a ORM to generate SQL. DB in use, SQLLite.
# To Do: Learn if I can write raw SQL in here
class Me(models.Model): #Class for myself, so I can dynamically update the picture and summary
    image = models.ImageField(upload_to='images/')
    name=models.CharField(max_length=30, default="Brenden Price")
    summary = models.TextField()

class Language(models.Model): #Class for any programming languages I know
    language = models.CharField(max_length = 30) #Language Name
    image = models.ImageField(upload_to='images/') #language image

    def __str__(self): #String representation, useful for admin instead of seeing Language Object (1)
        return self.language #language name

class Framework(models.Model): #Any frameworks I've used
    image = models.ImageField(upload_to='images/') #framework image
    framework = models.CharField(max_length = 30) #framework name
    language = models.ForeignKey(Language, on_delete=models.CASCADE) #what language is the framework in? ForeignKey to language creates a dropdown box in admin

    def __str__(self): #String representation is framework name
        return self.framework

class JobNoFramework(models.Model): #projects that didnt use a framework
    job = models.CharField(max_length=30) #A name for the project
    language = models.ForeignKey(Language, on_delete=models.CASCADE) #what language was it in? foreign key
    image = models.ImageField(upload_to='images/') #image for job
    summary = models.CharField(max_length=200, blank = True) #summary of project, not required
    submissionDate = models.DateField(default = date.today, blank = True) #submission date? Can be blank
    paste = models.CharField(max_length = 100, blank = True) #src for pastebin script
    def __str__(self): #String representation is project name and language written in
        return self.job + ", " + self.language

class JobYesFramework(models.Model): #projects with a framework
    job = models.CharField(max_length=30)  #project name
    framework = models.ForeignKey(Framework, on_delete=models.CASCADE) #framework used, foreign key to framework
    image = models.ImageField(upload_to='images/') #image for project
    summary = models.CharField(max_length=200, blank=True) #summary of project
    submissionDate = models.DateField(default = date.today, blank = True) #submission date, can be blank
    paste = models.CharField(max_length = 100, blank=True) #pastebin script src

    def __str__(self):#String representation is project name and framework used
        return self.job + ", " + self.framework
