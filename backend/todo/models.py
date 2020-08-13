from django.db import models

class Todo (models.Model):
    title = models.CharField(max_length=120)
    descr = models.TextField()
    compl = models.BooleanField(default = False)

    def __str__(self):
        return self.title