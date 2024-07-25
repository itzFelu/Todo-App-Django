from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Tasks

def index(request):
    if request.method == 'POST':
        data=request.POST
        print(data['status']+" "+data['id'])
        Tasks.objects.filter(id=data['id']).update(
            status=data['status']
        )
        return redirect('/')
    else:
        # read operations ~1
        data= Tasks.objects.all()
        context={
            'page': 'index',
            'data': data,
        }
        return render(request,'index.html',context)
        # return HttpResponse("hello this is index page")

def taskList(request):
    # print(request.path)
    if request.method == 'POST':
        data=request.POST
        print(data['status']+" "+data['id'])
        Tasks.objects.filter(id=data['id']).update(
            status=data['status']
        )
        return redirect(request.path)
    data= Tasks.objects.all()
    context={
        'page': 'taskList',
        'data': data
    }
    return render(request,'taskList.html',context)

def taskDetails(request,id):
    if request.method == 'POST':
        data=request.POST
        print(data['status']+" "+data['id'])
        Tasks.objects.filter(id=data['id']).update(
            status=data['status']
        )
        return redirect(request.path)
    data=Tasks.objects.get(id=id)
    return render(request,'taskDetails.html',context={'data':data,})

def update_task(request,id):
    if request.method == 'POST':
        data = request.POST
        Tasks.objects.filter(id=id).update(
            title=data['title'],
            description=data['description'],
            status=data['status'],
        )
        data=Tasks.objects.filter(id=id)
        return render(request,'taskDetails.html',context={'message':'success', 'data': data[0],})
    else:
        data=Tasks.objects.get(id=id)
        return render(request,'updateTask.html',context={'data':data})

def addTask(request):
    if request.method == "POST":
        data = request.POST
        # print(data['title']+"meoww "+data['description'])
        Tasks.objects.create(
            title=data['title'],
            description=data['description'],
            status=False
        )
        return render(request,'addTask.html',context={'message':'success', 'page': 'addTask',})
    else:
        context={
            'page': 'addTask',
        }
        return render(request,'addTask.html',context)
    # return HttpResponse("hello this is add Task page")

def del_task(request,id):
    print(id)
    Tasks.objects.get(id = id).delete()
    return redirect('/')
