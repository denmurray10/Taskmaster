from django.contrib import admin
from .models import Category, Task

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'due_date', 'completed', 'category']
    list_filter = ['completed', 'category']
