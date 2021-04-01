from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Project)

admin.site.register(models.Skill)
admin.site.register(models.SkillType)
admin.site.register(models.Role)
