from django.db import models



class Gender(models.Model):

    name        =models.CharField(max_length=25)
    def __str__(self):
        return self.name



class StudentData(models.Model):
    id          =models.AutoField(primary_key=True)
    name        =models.CharField(max_length=255)
    email       =models.CharField(max_length=255)
    #gender      =models.ForeignKey(Gender, blank=True, null=True,  on_delete= models.CASCADE)
    gender      =models.CharField(max_length=255)
    created_at  =models.DateTimeField(auto_now_add=True)
    objects     =models.Manager()

