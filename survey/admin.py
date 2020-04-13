from django.contrib import admin
from .models import *


#Creating a ModelAdmin for our PersonalInfo Model


class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'age', 'contactno', 'city')


#Creating a ModelAdmin for our SurevyMain Model


class SurveyMainAdmin(admin.ModelAdmin):
    list_display = ('feverhave', 'sorethroat', 'cough', 'breathing', 'chestpain', 'weak', 'foreigntrip')


#Creating a ModelAdmin for our SurveySecond Model


class SurveySecondAdmin(admin.ModelAdmin):
    list_display = ('diabetes', 'highbp', 'heart', 'lung', 'stroke', 'immunity')


#Registering all the models to our admin page

admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(Fever)
admin.site.register(SurveyMain, SurveyMainAdmin)
admin.site.register(SurveySecond, SurveySecondAdmin)
admin.site.register(Risk)