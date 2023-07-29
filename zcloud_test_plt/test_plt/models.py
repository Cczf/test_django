from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Project(models.Model):
    '''
    测试项目的model
    '''
    #产品类型 字典
    PROJECT_TYPE=[
        (1,'Web'),
        (2,'APP'),
        (3,'微服务')
    ]
    id = models.AutoField(primary_key=True)
    # 项目名称
    name = models.CharField(max_length=200, verbose_name='测试项目名称')
    # 版本
    version = models.CharField(max_length=20, verbose_name='版本')
    # 产品类型
    type = models.IntegerField(verbose_name='产品类型',choices=PROJECT_TYPE) #32bit 4bytes
    # 描述
    description = models.CharField(max_length=200, verbose_name='项目描述', blank=True, null=True)
    # 状态
    status = models.BooleanField(default=True, verbose_name='状态') #default默认值
    # 创建人
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL,
                                   db_column='created_by',
                                   null=True, verbose_name='创建人') #逻辑删除 《----》物理删除
    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    # 最后更新时间
    uodated_at = models.DateTimeField(auto_now=True,verbose_name='最近更新时间')

    # 项目成员 TODO
    # 测试环境（暂缓） TODO
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