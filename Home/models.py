from django.db import models


class AssignedTo(models.Model):
    username = models.CharField(max_length=250)
    actualName = models.CharField(max_length=250, default='john doe')

    def __str__(self):
        return self.actualName
