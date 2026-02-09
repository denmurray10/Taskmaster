from django.shortcuts import render
from .models import Task


def index(request):
    """
    View to display all tasks separated by completion status.
    Todo tasks and done tasks are both sorted by due date.
    """
    # Get tasks that are NOT completed
    todo_tasks = Task.objects.filter(completed=False).order_by('due_date').select_related('category')
    
    # Get tasks that ARE completed
    done_tasks = Task.objects.filter(completed=True).order_by('due_date').select_related('category')
    
    # Pass both querysets to the template
    context = {
        'todo_tasks': todo_tasks,
        'done_tasks': done_tasks,
    }
    
    return render(request, 'tasks/index.html', context)
