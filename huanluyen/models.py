from django.contrib.auth.models import User
from django.db import models

# -----------------
class Duan_c_giao(models.Model):
    name        = models.CharField(max_length=100, null=False, blank=False)
    content     = models.TextField(max_length=2000,null=True, blank=True)
    image        = models.ImageField(null=True, blank=True)

    def __str__(self):
       return self.name

class giangvien(models.Model):
    class Meta:
          ordering= ['id', 'name', ]

    name        = models.CharField(max_length=75, null=False, blank=False)
    profile     = models.TextField(max_length=2000,null=True, blank=True)
    image        = models.ImageField(null=True, blank=True)
    CTV         =models.BooleanField(default=True)
    def __str__(self):
       return self.name

class khach_hang(models.Model):
    name_kh       = models.CharField(max_length=75, null=False, blank=False)
    content_Kh    = models.TextField(max_length=2000,null=True, blank=True)
    image_kh      = models.ImageField(null=True, blank=True)
    Leader_kh     = models.CharField(max_length=75, null=True, blank=True)
    Leader_img    = models.ImageField(null=True, blank=True)
    def __str__(self):
       return self.name_kh

class Loptu_van(models.Model):
    name        = models.CharField(max_length=100, null=False, blank=False)
    content     = models.TextField(max_length=2000,null=True, blank=True)
    image        = models.ImageField(null=True, blank=True)

    def __str__(self):
       return self.name

class Noidungtu_van(models.Model):
    tenlop       = models.ForeignKey(Loptu_van, on_delete=models.SET_NULL, null=True, blank=True)
    image        = models.ImageField(null=False, blank=False)
    description  = models.TextField()
    ngay_tu_van  = models.DateField(blank=True,null=True)
    educator     = models.TextField(max_length=50,null=True, blank=True)
    excerpt       = models.TextField(max_length=500,null=True, blank=True)
    number_lessons  = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
       return self.description

