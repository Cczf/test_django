from django.contrib import admin
from .models import Project

# 将Models注册到这里
admin.site.register(Project)