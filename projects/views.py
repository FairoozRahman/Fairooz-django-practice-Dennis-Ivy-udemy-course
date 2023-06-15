from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm
from .utils import searchProjects, paginateProjects


def projects(request):
    projectsObj, search_query = searchProjects(request)
    custom_range, projectsObj = paginateProjects(request, projectsObj, 3)
    context = {'projects': projectsObj,
               'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'projectObj': projectObj})


@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm(request.POST, request.FILES)
    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST)
        if form.is_valid():
            projectObj = form.save(commit=False)
            projectObj.owner = profile
            projectObj.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    projectObj = profile.project_set.get(id=pk)
    form = ProjectForm(instance=projectObj)
    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST, request.FILES, instance=projectObj)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    projectObj = profile.project_set.get(id=pk)
    if request.method == 'POST':
        projectObj.delete()
        return redirect('account')
    context = {'object': projectObj}
    return render(request, 'delete_object.html', context)
