from django.shortcuts import render

from tasks.models import Task


def main_page(request):
    completed_tasks = Task.objects.filter(is_done=True)
    tasks_todo = Task.objects.filter(is_done=False)

    return render(request=request,
                  template_name='index.html',
                  context={'completed_tasks': completed_tasks,
                           'tasks_todo': tasks_todo})
