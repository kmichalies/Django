from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

def courses(request):
    context={
        'courses':Course.objects.all(),
    }
    return render(request,"index.html",context)

def create(request):
    course_errors = Course.objects.course_validation(request.POST)
    #description_errors = Description.objects.description_validation(request.POST)
    
    if(request.method == 'POST'):
    # pass the post data to the method we wrote and save the response in a variable called errors
    
    # check if the errors dictionary has anything in it
        if len(course_errors) > 0: # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in course_errors.items():
                messages.error(request, value)
            return redirect('/') # redirect the user back to the form to fix

        else:
            create_course = Course.objects.create(name = request.POST['name'], desc = request.POST['description'])
            #id = Course.id
            return redirect('/')
    else:
        return redirect('/')

def destroy(request,id):
    context={
        'courses':Course.objects.get(id=id)
    }
    return render(request,"delete.html", context)

def delete_yes(request,id):
    if request.method == 'POST': # check if POST
        delete_course = Course.objects.get(id=id)
        delete_course.delete()  #use delete or clear or maybe both
        return redirect('/') #deletes tv show from schema/db