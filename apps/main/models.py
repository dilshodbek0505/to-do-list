from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=100, help_text='Task name')
    description = models.TextField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    