from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Project(models.Model):
    """
    测试项目的model
    """
    # 产品类型 字典
    PROJECT_TYPE = [
        (1, 'Web'),
        (2, 'APP'),
        (3, '微服务')
    ]
    id = models.AutoField(primary_key=True)
    # 项目名称
    name = models.CharField(max_length=200, verbose_name='测试项目名称')
    # 版本
    version = models.CharField(max_length=20, verbose_name='版本')
    # 产品类型
    type = models.IntegerField(verbose_name='产品类型', choices=PROJECT_TYPE)  # 32bit 4bytes
    # 描述
    description = models.CharField(max_length=200, verbose_name='项目描述', blank=True, null=True)
    # 状态
    status = models.BooleanField(default=True, verbose_name='状态')  # default默认值
    # 创建人
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   db_column='created_by',
                                   null=True, verbose_name='创建人')  # 逻辑删除 《----》物理删除
    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    updated_at = models.DateTimeField(auto_now=True, verbose_name='最近更新时间')

    # 项目成员 TODO 有什么用？怎么用？
    members = models.ManyToManyField(User, related_name='project_members',
                                     through='ProjectMember',
                                     through_fields=('project', 'user')
                                     )

    # 测试环境（暂缓） TODO
    # 默认显示
    # 成功添加时返回添加的名字
    def __str__(self):
        return self.name

    # 内部类Meta
    class Meta:
        # 对应右边页面操作页
        verbose_name = '测试项目'
        # 对应左边栏目
        verbose_name_plural = verbose_name


class ProjectMember(models.Model):
    """
    项目成员（项目和用户之间的关系）
    """
    MEMBER_ROLE = [
        (1, '测试员'),
        (2, '测试组长'),
        (3, '测试经理'),
        (4, '开发'),
        (5, '运维'),
        (6, '项目经理'),
    ]
    # 主键
    id = models.AutoField(primary_key=True)
    # 项目
    project = models.ForeignKey(Project, on_delete=models.PROTECT, verbose_name='测试项目')  # PROTECT不能随意删除
    # 用户
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='用户')
    # 加入日期
    join_date = models.DateField(verbose_name='加入日期')
    # 角色
    role = models.IntegerField(choices=MEMBER_ROLE, verbose_name='角色')
    # 状态
    status = models.BooleanField(default=True, verbose_name='状态')
    # 退出日期
    quire_date = models.DateField(null=True, blank=True, verbose_name='退出日期')
    # 备忘录
    memo = models.CharField(max_length=200, verbose_name='备忘录', blank=True, null=True)

    def __str__(self):
        if not self.user:
            return '-'

        else:
            # 崔某某（username） | -（）username
            fistname = self.user.first_name if self.user.first_name else '-'
            username = self.user.username
            return f"{fistname}({username})"

    class Meta:
        verbose_name = '项目成员'
        verbose_name_plural = verbose_name
        db_table = 'test_plt_project_member'


class DeployEnv(models.Model):
    """
    部署环境
    """
    # 主键
    id = models.AutoField(primary_key=True)
    # 项目
    project = models.ForeignKey(Project, on_delete=models.PROTECT, verbose_name='测试项目')
    # 名称
    name = models.CharField(max_length=50, verbose_name='环境名称')
    # 主机名（IP）
    hostname = models.CharField(max_length=50, verbose_name='主机名', help_text='主机名（IP）')
    # 端口
    port = models.IntegerField(verbose_name='端口')
    # 状态
    status = models.BooleanField(default=True, verbose_name='状态')
    # 备忘录
    memo = models.CharField(max_length=200, verbose_name='备忘录', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '部署环境'
        verbose_name_plural = verbose_name
