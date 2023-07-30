from django.contrib import admin
from .models import Project, ProjectMember, DeployEnv
from django.contrib.admin import ModelAdmin


class ProjectAdmin(ModelAdmin):
    # 指定要显示的列（字段）
    list_display = ['id', 'name', 'version', 'type', 'status', 'created_by', 'created_at']
    # 指定哪些可进入项目链接
    list_display_links = ['name']
    # 指定可过滤的列
    list_filter = ['created_at', 'type']
    # 指定可查询的列
    search_fields = ['name']


# 将Models注册到这里
admin.site.register(Project, ProjectAdmin)


class ProjectMemberAdmin(ModelAdmin):
    """
     项目成员（项目和用户之间的关系)
    """
    list_display = ['id', 'project', '__str__', 'join_date', 'role', 'status']
    list_display_links = ['__str__']
    list_filter = ['join_date', 'role', 'status']
    search_fields = ['user']


admin.site.register(ProjectMember, ProjectMemberAdmin)


class DeployEnvAdmin(ModelAdmin):
    """
    部署环境
    """
    list_display = ['id', 'project', 'name', 'hostname', 'port', 'status']
    list_display_links = ['name']
    list_filter = ['status']
    search_fields = ['name', 'hostname', 'memo']


admin.site.register(DeployEnv, DeployEnvAdmin)
