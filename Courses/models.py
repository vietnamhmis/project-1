
from django.db import models


class Courses(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    educator = models.CharField(max_length=100)
    description = models.TextField()
    excerpt = models.TextField(max_length=300)
    number_lessons =models.PositiveSmallIntegerField(default=0)
    picture = models.ImageField(upload_to='course_pictures')
    video = models.FileField(upload_to='course-file')
    def __str__(self):
        return self.name

