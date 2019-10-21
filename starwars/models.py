from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CourseInfo(models.Model):
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=10)
    course_au = models.CharField(max_length=1)

    def __str__(self):
        return self.course_name