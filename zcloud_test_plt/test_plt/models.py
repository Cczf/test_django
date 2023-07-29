from django.db import models

# Create your models here.

class Project(models.Model):
    '''
    测试项目的model
    '''
    id = models.AutoField(primary_key=True)
    #项目名称
    name = models.CharField(max_length=200)