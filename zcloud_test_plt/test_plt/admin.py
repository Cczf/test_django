from django.contrib import admin
from .models import Project, ProjectMember, DeployEnv
from django.contrib.admin import ModelAdmin


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
