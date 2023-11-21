from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Todo




class TodoView(View):
    def get(self, request):
        todo_list = Todo.objects.order_by('-id')
        return render(request, 'index.html', {
            'todo_list': todo_list,
        })

    def post(self, request):
        data = request.POST
        name = data.get("task")
        print(name)
        Todo.objects.create(name = name)
        return redirect('home')
    
class EditView(View):
    def get(self, request , pk):
        task = Todo.objects.get(id = pk)
        return render(request, 'edit.html',{'task': task})
    def post(self, request, pk):
        name = request.POST.get("task")
        description = request.POST.get("description")
        is_done = request.POST.get("is_done")
        task = Todo.objects.get(id = pk)
        task.name = name
        task.description = description
        if is_done == 'on':
            task.is_done = True
        else:
            task.is_done = False
        task.save()
        return redirect('home')

class DeleteView(View):
    def get(self, request, pk):
        task = Todo.objects.get(id = pk)
        task.delete()
        return redirect('home')