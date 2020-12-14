from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Task(models.Model):
    title = models.CharField(max_length=64)
    complete = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks')
    