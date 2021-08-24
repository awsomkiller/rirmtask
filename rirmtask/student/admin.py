import student
from django.contrib import admin
from .models import students, studentacademics
# Register your models here.
admin.site.register(students)
admin.site.register(studentacademics)