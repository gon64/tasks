from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Project, Task
from .forms import createTask, createProject
# Create your views here.

def hello(request, username):
    print (username)
    return HttpResponse("hello %s" % username)

def about(request):
    username = {
        'name':"gon"
    }
    return render(request,'about.html',{
        'username' : username
    })

def index(request):
    title='Welcome'
    return render(request,'index.html', {
        'title':title
    })

def projects(request):
    return render(request,'projects/projects.html')
    # return JsonResponse(list(Project.objects.values()), safe=False)

def projects(request, id=None):
    # projects = list(Project.objects.values())
    # return HttpResponse("id: %s" % id)
    projects = Project.objects.all()
    return render(request,'projects/projects.html', {
        'projects' : projects
    })

def tasks(request):
    #return render(request,'tasks.html')
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks' : tasks
    })
    #return HttpResponse('tasks')

def create_task(request):
    if request.method == 'GET':
        print(request.GET)
        # show interface
        return render(request, 'tasks/create_task.html', {
            'form' : createTask()
        })
    else:
        print(request.POST)
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            project_id=1
        )
        return redirect('/tasks')


def create_project(request):
    if request.method == 'GET':
        # do stuff
        return render(request,'projects/create_project.html', {
            'form': createProject()
        })
    else:
        Project.objects.create(
            name=request.POST['name']
        )
        # do that other stuff
        return redirect('/projects')
