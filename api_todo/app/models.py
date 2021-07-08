from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=120)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    