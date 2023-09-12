from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View
from .models import Tasks
# Create your views here.
class HomePage(View):
    template_name = "index.html"

    def get(self, request):
        tasks = Tasks.objects.all()
        return render(request, self.template_name, {"tasks": tasks, "titulo": "hola mundo"})
    
    def post(self, request):
        title = request.POST.get("titulo")
        desc = request.POST.get("descrip")

        if title != "" and desc != "":
            my_task = Tasks.objects.create(task_name=request.POST.get("titulo"), task_desc=request.POST.get("descrip"))
            my_task.save()
        return HttpResponseRedirect("/")
    
    def put(self, request):
        id = request.POST.get("id")
        title = request.POST.get("titulo")
        desc = request.POST.get("descrip")

        if title != "" and desc != "":
            my_task = Tasks.objects.filter(pk=id).update(task_name=title, task_desc=desc)
            my_task.save()
        return HttpResponseRedirect("/")

    def delete(self, request, id):
        Tasks.objects.delete(pk=id)
        return HttpResponseRedirect("/")