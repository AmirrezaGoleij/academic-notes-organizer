from django.contrib import admin
from .models import Course, Tag, Note

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'updated_at']
    list_filter = ['course', 'tags']
    search_fields = ['title', 'content']
