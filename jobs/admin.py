from django.contrib import admin
# Register your models here.
# Import all of the models from the models file
from .models import Framework, Language, JobNoFramework, JobYesFramework, Me
#register decorator, followed by option information
@admin.register(Framework)
class FrameworkAdmin(admin.ModelAdmin):
    list_display = ['framework','language'] #What to display in admin when Framework is selected
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['language'] #What to display in admin when Language is selected
@admin.register(JobNoFramework)
class JobNoFrameworkAdmin(admin.ModelAdmin):
    list_display = ['job','language']#What to display in admin when JobNoFramework is selected
@admin.register(JobYesFramework)
class JobYesFrameworkAdmin(admin.ModelAdmin):
    list_display = ['job', 'framework']#What to display in admin when JobYesFramework is selected
@admin.register(Me)
class MeAdmin(admin.ModelAdmin):
    list_display = ['name']#What to display in admin when Me is selected
