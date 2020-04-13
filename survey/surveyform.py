from django import forms
from django.forms import ModelForm

from .models import *


#Creating a ModelAdmin for our PersonalInfo Model


class SurveyFormInfo(forms.ModelForm):

    class Meta:
        model = PersonalInfo
        fields = ('firstname', 'lastname', 'age', 'contactno', 'city')

    def __init__(self, *args, **kwargs ):
        super(SurveyFormInfo,self).__init__(*args, **kwargs)
        self.fields['contactno'].empty_label = "0123456789"


#Creating a ModelForm for our SurveyMain Model


class SurveyFormMain(forms.ModelForm):

    class Meta:
        model = SurveyMain
        fields = ('feverhave', 'sorethroat', 'chestpain', 'cough', 'breathing', 'weak', 'foreigntrip')
        labels = {
            'feverhave': 'Do you have fever?',
            'sorethroat': 'Do you have Sore throat?',
            'chestpain': 'Do you have chest pain?',
            'cough': 'Do you have dry cough and sneezing & running nose?',
            'breathing': 'Do you have difficulty in breathing?',
            'weak': 'Do you feel weak?',
            'foreigntrip': 'Have you recently returned from a foreign trip?'
        }

    # The following is done to get select as the first option in our dropdown list

    def __init__(self, *args, **kwargs):
        super(SurveyFormMain, self).__init__(*args, **kwargs)
        self.fields['feverhave'].choices = [("", "Select"), ] + list(self.fields["feverhave"].choices)[1:]
        self.fields["sorethroat"].choices = [("", "Select"), ] + list(self.fields["sorethroat"].choices)[1:]
        self.fields["chestpain"].choices = [("", "Select"), ] + list(self.fields["chestpain"].choices)[1:]
        self.fields["cough"].choices = [("", "Select"), ] + list(self.fields["cough"].choices)[1:]
        self.fields["breathing"].choices = [("", "Select"), ] + list(self.fields["breathing"].choices)[1:]
        self.fields["weak"].choices = [("", "Select"), ] + list(self.fields["weak"].choices)[1:]
        self.fields["foreigntrip"].choices = [("", "Select"), ] + list(self.fields["foreigntrip"].choices)[1:]


#Creating a ModelAdmin for our SurveySecond Model


class SurveyFormSecond(forms.ModelForm):

    class Meta:
        model = SurveySecond
        fields = ('diabetes', 'highbp', 'heart', 'lung', 'stroke', 'immunity')
        labels = {
            'diabetes': 'Do you have Diabetes?',
            'highbp': 'Do you have High Blood Pressure?',
            'heart': 'Do you have Heart Disease?',
            'lung': 'Do you have Lung Disease?',
            'stroke': 'Do you have Stroke?',
            'immunity': 'Have your Immunity decreased?',
            }

    #The following is done to get select as the first option in our dropdown list

    def __init__(self, *args, **kwargs):
        super(SurveyFormSecond, self).__init__(*args, **kwargs)
        self.fields["diabetes"].choices = [("", "Select"), ] + list(self.fields["diabetes"].choices)[1:]
        self.fields["highbp"].choices = [("", "Select"), ] + list(self.fields["highbp"].choices)[1:]
        self.fields["heart"].choices = [("", "Select"), ] + list(self.fields["heart"].choices)[1:]
        self.fields["lung"].choices = [("", "Select"), ] + list(self.fields["lung"].choices)[1:]
        self.fields["stroke"].choices = [("", "Select"), ] + list(self.fields["stroke"].choices)[1:]
        self.fields["immunity"].choices = [("", "Select"), ] + list(self.fields["immunity"].choices)[1:]

