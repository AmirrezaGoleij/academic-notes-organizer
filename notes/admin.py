from django.contrib import admin
from .models import Course, Note, Tag


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created_at']
    list_filter = ['owner']
    search_fields = ['title']


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'created_at', 'updated_at']
    list_filter = ['course', 'tags']
    search_fields = ['title', 'content']


admin.site.register(Tag)
