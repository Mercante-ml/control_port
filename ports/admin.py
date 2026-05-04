from django.contrib import admin
from .models import Project, Service

class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'domain')
    inlines = [ServiceInline]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'external_port', 'internal_port', 'service_type', 'is_active')
    list_filter = ('project', 'service_type', 'is_active')
    search_fields = ('name', 'project__name', 'external_port')
