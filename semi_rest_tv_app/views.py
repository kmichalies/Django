from django.shortcuts import render, HttpResponse, redirect
from .models import *
from datetime import datetime

def shows(request):
    context={
        'shows':Show.objects.all()
    }
    return render(request,"shows.html",context)

def new(request):
    return render(request,"new.html")
    #new.html for creating a new show.  Form action leads to views.create

def create(request):
    if(request.method == 'POST'):
        create_network=Network.objects.create(name=request.POST['network'])
        new_network=Network.objects.get(id=create_network.id)
        new_show = Show.objects.create(title = request.POST['title'], release_date = request.POST['release_date'], desc = request.POST['description'], network = new_network)
        id = new_show.id
        return redirect(f'/shows/{id}')

def oneshow(request,id):
    context={
        'shows':Show.objects.get(id=id)
    }
    return render(request,"tvshow.html", context)
    #displays new show - tvshow.html

def edit(request,id):
    context={
        'shows':Show.objects.get(id=id)

    }
    return render(request,"edit.html", context)
    #goes to edit page. Form action leads to views.update

def update(request,id):
    if request.method=='POST':
        update_show = Show.objects.get(id=id)
        update_show.title = request.POST['title']
        update_show.release_date = request.POST['release_date']
        update_show.desc = request.POST['description']
        update_show.network.name = request.POST['network']
        update_show.save()
        print(update_show.__dict__)
        return redirect(f'/shows/{id}') #updates tv show and redirects to shows/id tvshow.html

def destroy(request,id):
    if request.method == 'POST': # check if POST
        delete_show = Show.objects.get(id=id)
        delete_show.delete()  #use delete or clear or maybe both
        return redirect('/shows') #deletes tv show from schema/db
