# from django.http import Http404, JsonResponse
import json
from django.shortcuts import render, redirect
from django.core import serializers
from export_app.models import Project, TildaRequest


def projects_list(request):
    context = dict()
    context["projects"] = []
    for project in Project.objects.all():
        context["projects"].append({
            "id": project.id,
            "title": project.title,
            "descr": project.descr
        }
        )
    return render(request, "projects.html", context)


def update_projects(request):
    tr = TildaRequest.objects.latest("id")
    tr.getprojectslist()
    print("TildaRequest.objects.latest()", TildaRequest.objects.latest("id"))
    return redirect("/projects/")


def project(request, project_id):
    print("project_id: ", project_id)
    obj = Project.objects.get(pk=project_id)
    data = serializers.serialize('json', [obj,])
    struct = json.loads(data)
    data = json.dumps(struct[0])
    return render(request, "project.html", data)
