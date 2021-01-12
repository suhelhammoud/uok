from django.contrib import admin
from .models.core_models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

admin.site.site_header = 'UOK site administration'


class FacultyResource(resources.ModelResource):
    class Meta:
        model = Faculty


class FacultyAdmin(ImportExportModelAdmin):
    resource_class = FacultyResource
    list_display = ('id', 'name', 'caption',)
    # list_filter = ('faculty',)


admin.site.register(Faculty, FacultyAdmin)


class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department


# class DepartmentAdmin(admin.ModelAdmin):
class DepartmentAdmin(ImportExportModelAdmin):
    resource_class = DepartmentResource
    list_display = ('name', 'caption', 'faculty')
    list_filter = ('faculty',)


admin.site.register(Department, DepartmentAdmin)


class PlanResource(resources.ModelResource):
    class Meta:
        model = Plan


class PlanAdmin(ImportExportModelAdmin):
    resource_class = PlanResource
    list_display = ('name', 'department',)
    list_filter = ('department',)


admin.site.register(Plan, PlanAdmin)


class ModuleResource(resources.ModelResource):
    class Meta:
        model = Module


class ModuleAdmin(ImportExportModelAdmin):
    list_display = ('code', 'name', 'credit', 'department')
    list_filter = ('department', 'plan',)
    resource_class = ModuleResource


admin.site.register(Module, ModuleAdmin)


class DependencyResource(resources.ModelResource):
    class Meta:
        model = Dependency


class DependencyAdmin(ImportExportModelAdmin):
    resource_class = DependencyResource
    list_display = ('pre_module', 'post_module',)
    list_filter = ('pre_module', 'post_module',)


admin.site.register(Dependency, DependencyAdmin)
