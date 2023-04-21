from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Lopdaotao(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
       return self.name

class giangvien(models.Model):
    name = models.CharField(max_length=75, null=False, blank=False)
    def __str__(self):
       return self.name

class Noidungdaotao(models.Model):
    tenlop       = models.ForeignKey(Lopdaotao, on_delete=models.SET_NULL, null=True, blank=True)#

    image          = models.ImageField(null=False, blank=False)
    description    = models.TextField()

    ngay_daotao     = models.DateField(blank=True,null=True)
    educator        = models.TextField(max_length=50,null=True, blank=True)
    excerpt         = models.TextField(max_length=500,null=True, blank=True)

    number_lessons  = models.PositiveSmallIntegerField(default=1)

    #video           = models.FileField(upload_to='course-file')
    def __str__(self):
       return self.description

