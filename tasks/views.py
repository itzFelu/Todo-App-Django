from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Tasks, Activity_log
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_page(request):
    if request.user.is_authenticated:
        print('already logged in')
        return redirect('/')
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        if not User.objects.filter(email=email):
            message="no user with this email!"
            messages.error(request,message)
            # print(message)
            return redirect('/login')
        user=authenticate(username=email, password=password)
        if user is None:
            message='Invalid password, please try again'
            messages.error(request,message)
            # print(message)
            Activity_log.objects.create(
                nameOf_action_performed="somebody tried to login",
                performed_by= User.objects.get(username=email)
            )
            return redirect('/login')
        login(request,user)
        Activity_log.objects.create(
            nameOf_action_performed="user logged in",
            performed_by= user
        )
        return redirect('/')
    return render(request,'login.html')
    
def register_page(request):
    if request.user.is_authenticated:
        print('already logged in')
        return redirect('/')
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')

        if User.objects.filter(email=email):
            message='email already exist, user another'
            messages.error(request,message)
            print(message)
            return redirect('/register')

        user= User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=email,
        )
        user.set_password(password)
        user.save()
        Activity_log.objects.create(
            nameOf_action_performed="New user created",
            performed_by= user
        )
        messages.success(request,'User created successfully, please login now')
        return redirect('/register')


    return render(request,'register.html')

@login_required(login_url='/login/')
def logout_page(request):
    Activity_log.objects.create(
            nameOf_action_performed="user logged out",
            performed_by= request.user
        )
    logout(request)
    return redirect('/login')

@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        data=request.POST
        print(data['status']+" "+data['id'])
        Tasks.objects.filter(id=data['id']).update(
            status=data['status'],
            timeOf_last_update=datetime.now(),
        )
        task=Tasks.objects.get(id=data['id'])
        Activity_log.objects.create(
            nameOf_action_performed="Task status updated",
            performed_by= request.user,

            task_id=task.id,
            title=task.title,
            description=task.description,
            status= task.status,
            timeOf_creation= task.timeOf_creation ,
            timeOf_last_update= task.timeOf_last_update,
        )
        return redirect('/')
    else:
        # read operations ~1
        data= Tasks.objects.filter(created_by=request.user)
        context={
            'page': 'index',
            'data': data,
        }
        return render(request,'index.html',context)
        # return HttpResponse("hello this is index page")

@login_required(login_url='/login/')
def taskList(request,filter):
    # print(request.path)
    if request.method == 'POST':
        data=request.POST
        print(data['status']+" "+data['id'])
        Tasks.objects.filter(id=data['id']).update(
            status=data['status'],
            timeOf_last_update=datetime.now(),
        )
        task=Tasks.objects.get(id=data['id'])
        Activity_log.objects.create(
            nameOf_action_performed="Task status updated",
            performed_by= request.user,

            task_id=task.id,
            title=task.title,
            description=task.description,
            status= task.status,
            timeOf_creation= task.timeOf_creation ,
            timeOf_last_update= task.timeOf_last_update,
        )
        return redirect(request.path)

    if filter == 'All':
        data= Tasks.objects.filter(created_by=request.user)
    else:
        data=Tasks.objects.filter(created_by=request.user, status = filter)
    context={
        'page': 'taskList',
        'data': data,
        'filter': filter,
    }
    return render(request,'taskList.html',context)

@login_required(login_url='/login/')
def taskDetails(request,id):
    if request.method == 'POST':
        data=request.POST
        print(data['status']+" "+data['id'])
        Tasks.objects.filter(id=data['id']).update(
            status=data['status'],
            timeOf_last_update=datetime.now(),
        )
        task=Tasks.objects.get(id=data['id'])
        Activity_log.objects.create(
            nameOf_action_performed="Task status updated",
            performed_by= request.user,

            task_id=task.id,
            title=task.title,
            description=task.description,
            status= task.status,
            timeOf_creation= task.timeOf_creation ,
            timeOf_last_update= task.timeOf_last_update,
        )
        return redirect(request.path)
    data=Tasks.objects.get(id=id, created_by=request.user)
    return render(request,'taskDetails.html',context={'data':data,})

@login_required(login_url='/login/')
def update_task(request,id):
    if request.method == 'POST':
        data = request.POST
        Tasks.objects.filter(id=id).update(
            title=data['title'],
            description=data['description'],
            status=data['status'],
            timeOf_last_update=datetime.now()
        )
        task=Tasks.objects.get(id=id)
        Activity_log.objects.create(
            nameOf_action_performed="Task details updated",
            performed_by= request.user,

            task_id=task.id,
            title=task.title,
            description=task.description,
            status= task.status,
            timeOf_creation= task.timeOf_creation ,
            timeOf_last_update= task.timeOf_last_update,
        )
        messages.success(request,'Task Updated successfully')
        return redirect(f"/taskDetails/{id}")
    else:
        data=Tasks.objects.get(id=id)
        return render(request,'updateTask.html',context={'data':data})

@login_required(login_url='/login/')
def addTask(request):
    if request.method == "POST":
        data = request.POST
        # print(data['title']+"meoww "+data['description'])
        task= Tasks.objects.create(
            title=data['title'],
            description=data['description'],
            created_by=request.user,
        )
        
        Activity_log.objects.create(
            nameOf_action_performed="new Task created",
            performed_by= request.user,

            task_id=task.id,
            title=task.title,
            description=task.description,
            status= task.status,
            timeOf_creation= task.timeOf_creation ,
            timeOf_last_update= task.timeOf_last_update,
        )
        messages.success(request,'Task added successfully')
        return redirect('/addtask')
    else:
        context={
            'page': 'addTask',
        }
        return render(request,'addTask.html',context)

""" Deleting task directly from url, get request, no securities are there"""
# need to know proper way of sending delete request
@login_required(login_url='/login/')
def del_task(request,id):
    task=Tasks.objects.get(id=id)
    # Tasks.objects.get(id = id).delete()
    Activity_log.objects.create(
            nameOf_action_performed="Task deleted",
            performed_by= request.user,

            task_id=task.id,
            title=task.title,
            description=task.description,
            status= task.status,
            timeOf_creation= task.timeOf_creation ,
            timeOf_last_update= task.timeOf_last_update,
        )
    task.delete()
    messages.success(request,'task deleted')
    return redirect('/tasklist/All')




"""
if 'filter' in data.keys():
            filter=data['filter']
            if filter=='All':
                data= Tasks.objects.all()
            else:
                data= Tasks.objects.filter(status=filter)
            context={
                'page': 'taskList',
                'data': data
            }
            return render(request,'taskList.html',context)
        else:
"""