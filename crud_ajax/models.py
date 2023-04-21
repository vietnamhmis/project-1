from django.db import models
#https://www.youtube.com/watch?v=uQtIqh9mEgM&t=80s



class CrudUser(models.Model):
    name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)

