from django.contrib import admin
from .models import ToDoItem, Tag

@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'status', 'due_date')
    list_filter = ('status', 'tags')
    search_fields = ('title', 'description')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
