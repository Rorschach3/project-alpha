from django.shortcuts import render, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
# related to models
def list_projects(request): 
    # related to admin
    my_projects = Project.objects.filter(owner=request.user)
    # related to templates
    context = {"projects": my_projects}
    # related to urls
    return render(request, "projects/list_projects.html", context)


@login_required()
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    context = {"project": project}
    return render(request, "projects/show_project.html", context)


@login_required()
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
    context = {"form": form}
    return render(request, "projects/create_project.html", context)