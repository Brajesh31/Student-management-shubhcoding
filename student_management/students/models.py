# from django.db import models

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     roll_number = models.CharField(max_length=20, unique=True)
#     email = models.EmailField(unique=True)
#     course = models.CharField(max_length=50)
#     attendance = models.IntegerField(default=0)

#     def __str__(self):
#         return f"{self.name} ({self.roll_number})"

from django.db import models
from djongo import models as djongo_models
from bson import ObjectId  # Add this import

class Student(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, editable=False, default=ObjectId)  # ← Fixed line
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=50)
    attendance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.roll_number})"
