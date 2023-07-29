from django.db import models

# Create your models here.

class Project(models.Model):
    '''
    测试项目的model
    '''
    id = models.AutoField(primary_key=True)
    # 项目名称
    name = models.CharField(max_length=200,verbose_name='测试项目名称')
    # 默认显示
    # 成功添加时返回添加的名字
    def __str__(self):
        return self.name

    # 内部类Meta
    class Meta:
        # 对应右边页面操作页
        verbose_name='测试项目'
        # 对应左边栏目
        verbose_name_plural=verbose_name