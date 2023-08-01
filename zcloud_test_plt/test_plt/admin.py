from django.contrib import admin
from django.forms import TextInput, Textarea

from .models import Project, ProjectMember, DeployEnv, ApiDef, QueryParam, RequesHeader, RequesBody
from django.contrib.admin import ModelAdmin
from django.db import models


class ProjectMemberInline(admin.TabularInline):  # 还有StackedInline 规矩化布局
    """
    项目成员_内联到项目管理
    """
    model = ProjectMember  # 对应的是哪个Model
    extra = 1


class DeployEnvInline(admin.TabularInline):
    """
    部署环境_内联到项目管理
    """
    model = DeployEnv
    extra = 1


class QueryParamInline(admin.TabularInline):  # 还有StackedInline 规矩化布局
    model = QueryParam
    extra = 2


class RequesHeaderInline(admin.TabularInline):  # 还有StackedInline 规矩化布局
    model = RequesHeader
    extra = 2


class RequesBodyInline(admin.TabularInline):  # 还有StackedInline 规矩化布局
    model = RequesBody
    extra = 2
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': '3', 'cols': 30})}
    }


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    # 指定要显示的列（字段）
    list_display = ['id', 'name', 'version', 'type', 'status', 'created_by', 'created_at']
    # 指定哪些可进入项目链接
    list_display_links = ['name']
    # 指定可过滤的列
    list_filter = ['created_at', 'type']
    # 指定可查询的列
    search_fields = ['name']
    # 内联的model
    inlines = [ProjectMemberInline, DeployEnvInline]
    # 控制字段的表单排列
    fieldsets = (
        ('基础信息', {
            'fields': (('name', 'status'), ('version', 'type'), 'created_by')
        }),
        ('扩展信息', {
            'classes': ('collapse',),
            'fields': ('description',)
        })
    )


@admin.register(ProjectMember)
class ProjectMemberAdmin(ModelAdmin):
    """
     项目成员（项目和用户之间的关系)
    """
    list_display = ['id', 'project', '__str__', 'join_date', 'role', 'status']
    list_display_links = ['__str__']
    list_filter = ['join_date', 'role', 'status']
    search_fields = ['user']


@admin.register(DeployEnv)
class DeployEnvAdmin(ModelAdmin):
    """
    部署环境
    """
    list_display = ['id', 'project', 'name', 'hostname', 'port', 'status']
    list_display_links = ['name']
    list_filter = ['status']
    search_fields = ['name', 'hostname', 'memo']


@admin.register(ApiDef)
class ApidefAdmin(ModelAdmin):
    """
    接口定义
    """
    list_display = ['id', 'project', 'protocol', 'name', 'http_schema', 'http_method', 'deploy_env', 'uri', 'status']
    list_display_links = ['name']
    list_filter = ['status', 'http_schema', 'http_method']
    search_fields = ['name', 'uri']
    inlines = [QueryParamInline, RequesHeaderInline, RequesBodyInline]

    fieldsets = (
        ('基础信息', {
            'fields': ('project', 'protocol', ('name', 'status'), 'deploy_env', 'created_by',)
        }),
        ('HTTP信息', {
            'fields': (('http_schema', 'http_method'), 'uri', ('auth_type', 'body_type'))
        }),
        ('其他信息', {
            'fields': (('db_name', 'db_username', 'db_password'),)
        }),
    )

    actions = ['run_api']

    def run_api(self, request, queryset):
        """
        接口执行
        :param request:当前的HTTP的请求信息，由Django自动提供
        :param queryset:当前页面上所选中的数据，由Django自动提供
        :return:
        """
        pass



