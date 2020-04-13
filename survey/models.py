from django.core.validators import MaxValueValidator, RegexValidator
from django.db import models


class Fever(models.Model):
    fever = models.CharField(max_length=10)

    def __str__(self):
        return self.fever


class PersonalInfo(models.Model):

    count = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255, validators=[RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])
    lastname = models.CharField(max_length=255, validators=[RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])
    age = models.PositiveIntegerField(validators=[MaxValueValidator(150)])
    contactno = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    city = models.CharField(max_length=255, validators=[RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])

    def __str__(self):
        return self.count



class SurveyMain(models.Model):

    yesno = (('Yes','Yes'),
             ('No', 'No'))
    personal_id = models.PositiveIntegerField(default=0)
    feverhave = models.ForeignKey(Fever,blank='false', on_delete= models.ForeignKey)
    sorethroat = models.CharField(max_length=10, blank='false', choices=yesno)
    chestpain = models.CharField(max_length=10, blank='false', choices=yesno)
    cough = models.CharField(max_length=10, blank='false', choices=yesno)
    breathing = models.CharField(max_length=10, blank='false', choices=yesno)
    weak = models.CharField(max_length=10, blank='false', choices=yesno)
    foreigntrip = models.CharField(max_length=10, blank='false', choices=yesno)



class SurveySecond(models.Model):
    yesno = (('Yes', 'Yes'),
             ('No', 'No'))
    main_id = models.PositiveIntegerField(default= 0)
    diabetes = models.CharField(max_length=10, choices=yesno, blank='false')
    highbp = models.CharField(max_length=10, choices=yesno, blank='false')
    heart = models.CharField(max_length=10, choices=yesno, blank='false')
    lung = models.CharField(max_length=10, choices=yesno, blank='false')
    stroke = models.CharField(max_length=10, choices=yesno, blank='false')
    immunity = models.CharField(max_length=10, choices=yesno, blank='false')


class Risk(models.Model):
    risk = models.CharField(max_length= 255)

    def __str__(self):
        return self.risk
