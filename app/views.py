from django.shortcuts import render
from app.models import Todo
from django.http import HttpResponseRedirect

def submit(request):
        task = request.POST.get('task')
        date = request.POST.get('date')

        todo = Todo(task=task, date=date)
        todo.save()
        return HttpResponseRedirect("/")

def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")

def edit(request, todo_id):
    if request.method == "POST":
        task = request.POST.get('task')
        date = request.POST.get('date')
        temp = Todo.objects.get(id = todo_id)
        temp.task = task
        temp.date = date
        temp.save()
        return HttpResponseRedirect("/")

    
    todo_item = Todo.objects.get(id=todo_id)
    context = {"todo_item" : todo_item}
    return render(request, 'Edit.html', context)




    
def index(request):
    todo_item = Todo.objects.all().order_by("-date")
    context = {"todo_items" : todo_item}
    return render(request, 'tasks.html', context)
