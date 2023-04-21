from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
       return self.name


class Photo(models.Model):
    category       = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image          = models.ImageField(null=False, blank=False)
    description    = models.TextField()
    ho_lot_thuong_dung = models.CharField(max_length=50, blank=True, null=True)
    ten_thuong_dung = models.CharField(max_length=15, blank=True, null=True)
    ma_nhan_vien    = models.CharField(max_length=5, blank=True, null=True)
    ngay_vao_nganh  = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.description
