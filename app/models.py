from django.db import models
from django.contrib.postgres.fields import ArrayField

class Student(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    tags = ArrayField(models.CharField(max_length=30))

    def __str__(self):
        return self.name