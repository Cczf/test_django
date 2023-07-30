from django.contrib import admin
from .models import Project
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
