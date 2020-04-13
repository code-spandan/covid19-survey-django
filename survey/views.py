from django.http import HttpResponse
from django.shortcuts import render, redirect
from .surveyform import *
from .models import *
from django.contrib import messages
import _sqlite3
import os


#Function to read the db and get latest row of data entered and work on that data to get the risk level

def read_db():
    obj = PersonalInfo.objects.last()
    val = getattr(obj, 'count')
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    database = os.path.join(BASE_DIR, 'survey.sqlite3')
    print(database)
    conn = _sqlite3.connect(database)
    c = conn.cursor()
    c.execute('SELECT * FROM  finaltable WHERE ID = (SELECT MAX(ID) FROM finaltable)')
    data = c.fetchone()
    c.close()
    conn.close()
    counter = 0
    score = 0
    for i in data:
        if counter == 12:
            score = score + 3
            counter = counter + 1
            continue
        if counter == 13:
            if i == 1:
                score = score + 2
                print(counter)
            elif i == 2:
                score = score + 1
                print(counter)
            else:
                pass
            counter = counter + 1
            continue
        if i == 'Yes':
            score = score + 1
        counter = counter + 1

    risk = score / 13
    obj = Risk()
    if risk >= 0.8:
        obj.risk = "High"
        obj.save()
        return f"High Risk"
    elif 0.8 > risk >= 0.4:
        obj.risk = "Medium"
        obj.save()
        return f"Medium Risk"
    elif risk < 0.4:
        obj.risk = "Low"
        obj.save()
        return f"Low Risk"
    else:
        pass

# view function of "survey/" page


def index(request):

    if request.method == "GET":
        form = SurveyFormInfo
        context = {'form': form}
        return render(request, 'survey/form.html', context)
    else:
        form = SurveyFormInfo(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/survey/main/')
        else:
            messages.error(request,"Enter valid Information")
            return redirect('/survey')


# view function of "survey/main" page


def formmain(request):

    if request.method == "GET":
        form = SurveyFormMain
        context = {'form': form }
        return render(request, 'survey/formmain.html', context)
    else:
        form = SurveyFormMain(request.POST)
        if form.is_valid():
            form.save()
            obj = PersonalInfo.objects.last()
            val = getattr(obj, 'count')
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            database = os.path.join(BASE_DIR, 'survey.sqlite3')
            conn = _sqlite3.connect(database)
            c = conn.cursor()
            c.execute(
                f'UPDATE survey_surveymain SET personal_id = {val} WHERE id = (SELECT MAX(ID) FROM survey_surveymain)')
            conn.commit()
            c.close()
            conn.close()
            return redirect(f'/survey/main/second/')
        else:
            print(form.errors)
            print("form invalid")

# view function of "survey/main/second" page


def formsecond(request):

    obj = PersonalInfo.objects.last()
    val = getattr(obj, 'count')
    if request.method == "GET":
        form = SurveyFormSecond
        context = {'form': form}
        return render(request, 'survey/formsecond.html', context)
    else:
        form = SurveyFormSecond(request.POST)
        if form.is_valid():
            form.save()
            obj = PersonalInfo.objects.last()
            val = getattr(obj, 'count')
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            database = os.path.join(BASE_DIR, 'survey.sqlite3')
            conn = _sqlite3.connect(database)
            c = conn.cursor()
            c.execute(
                    f'UPDATE survey_surveysecond SET main_id = {val} WHERE id = (SELECT MAX(ID) FROM survey_surveysecond)')
            conn.commit()
            c.close()
            conn.close()
            messages.success(request, read_db())
            return redirect('/survey/main/second')
        else:
            print(form.errors)
            print("form invalid")

