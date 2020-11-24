from django.contrib import admin
from .models import Myself, Skill, Education, Job
# Register your models here.
#register decorator, followed by option information
@admin.register(Myself)
class MyselfAdmin(admin.ModelAdmin):
    list_display = ['position'] #What to display in admin when myself is selected
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['language','comfort']#What to display in admin when language is selected
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution','type', 'start_date', 'end_date', 'gpa'] #What to display in admin when education is selected
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['company','position','start_date','end_date'] #What to display in admin when Job is selected
