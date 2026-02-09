from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Task
from .forms import TaskForm


def index(request):
    """
    View to display all tasks separated by completion status.
    Todo tasks and done tasks are both sorted by due date.
    """
    # Get tasks that are NOT completed
    todo_tasks = (
        Task.objects.filter(completed=False, is_trashed=False)
        .order_by('due_date')
        .select_related('category')
    )
    # Get tasks that ARE completed
    done_tasks = (
        Task.objects.filter(completed=True, is_trashed=False)
        .order_by('due_date')
        .select_related('category')
    )
    # Handle task creation form
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.completed = False
            task.is_trashed = False
            task.save()
            return redirect('index')
    else:
        form = TaskForm()

    # Pass querysets and form to the template
    context = {
        'todo_tasks': todo_tasks,
        'done_tasks': done_tasks,
        'form': form,
    }

    return render(request, 'tasks/index.html', context)


def bin_view(request):
    """Show trashed tasks (recycle bin)."""
    trashed = (
        Task.objects.filter(is_trashed=True)
        .order_by('-trashed_at')
        .select_related('category')
    )
    return render(request, 'tasks/bin.html', {'trashed_tasks': trashed})


def delete_task(request, pk):
    """Soft-delete: move a task to the trash."""
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.is_trashed = True
        task.trashed_at = timezone.now()
        task.save()
    return redirect('index')


def restore_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.is_trashed = False
        task.trashed_at = None
        task.save()
    return redirect('tasks_bin')


def hard_delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
    return redirect('tasks_bin')


def empty_bin(request):
    if request.method == 'POST':
        Task.objects.filter(is_trashed=True).delete()
    return redirect('tasks_bin')
