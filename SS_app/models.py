from django.db import models

class Queries(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,default="",null=True,blank=True)
    email = models.EmailField(default="",null=True,blank=True)
    mobile=models.BigIntegerField(default=0,null=True,blank=True)
    message=models.CharField(max_length=255,default="",null=True,blank=True)
    def __str__(self):
        return self.id


class adminlist(models.Model):
    id = models.AutoField(primary_key=True)
    adminid = models.CharField(max_length=255, default="", null=True, blank=True)    
    password = models.CharField(max_length=255, default="", null=True, blank=True)
    def __str__(self):
        return self.adminid


