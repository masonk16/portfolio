from django.shortcuts import render
from .models import Project


def project_list(request):
    """This is a list of all the projects"""
    projects = Project.objects.all()
    return render(request, "projects/list.html", {"projects": projects})


def project_detail(request, pk):
    """This is the details view for a project."""
    project = Project.objects.get(pk=pk)
    return render(request, "projects/detail.html", {"project": project})
