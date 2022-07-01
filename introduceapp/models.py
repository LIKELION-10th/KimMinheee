from django.utils import timezone
from django.db import models

class Comment(models.Model):
    comment=models.TextField()
    date=models.DateTimeField(default=timezone.now())
    def __str__(self):
        return self.comment