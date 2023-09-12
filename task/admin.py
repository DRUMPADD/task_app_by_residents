from django.contrib import admin
from .models import Tasks
# Register your models here.
@admin.register(Tasks)
class TaskViewModel(admin.ModelAdmin):
    model = Tasks
    list_display = ['pk', 'task_name', 'task_desc']