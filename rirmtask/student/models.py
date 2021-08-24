from django.db import models
from django.db.models.deletion import PROTECT
# Create your models here.

class students(models.Model):
    roll_number = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=20)
    student_class = models.CharField(max_length = 10)
    school_name = models.CharField(max_length = 10)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=50)

class studentacademics(models.Model):
    id = models.AutoField(primary_key=True)
    roll_number = models.ForeignKey(students, on_delete=PROTECT)
    maths = models.CharField(max_length=10)
    physics = models.CharField(max_length=10)
    chemistry = models.CharField(max_length=10)
    biology = models.CharField(max_length=10)
    english = models.CharField(max_length=10)
