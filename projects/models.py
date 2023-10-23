from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    stack = models.TextField()

    def __str__(self):
        return str(self.title)
