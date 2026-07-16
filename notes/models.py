from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Course(models.Model):
    """A course/subject that groups related notes together."""
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        #if User delets their Couse their data will be deleted 
        related_name='courses',
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        #user cannot have two course with the same title
        unique_together = ['owner', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'pk': self.pk})


class Tag(models.Model):
    """A label for categorizing notes (e.g. 'exam', 'important')."""
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Note(models.Model):
    """A single note/lecture document belonging to a course."""
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='notes',
    )
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True)
    content = models.TextField(blank=True)  # Markdown 
    tags = models.ManyToManyField(Tag, blank=True, related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f'{self.title} ({self.course.title})'

    def get_absolute_url(self):
        return reverse('note_detail', kwargs={'pk': self.pk})
