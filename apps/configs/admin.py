from django.contrib import admin
from apps.configs.models import Environment
from apps.configs.models import Application
from apps.configs.models import Setting
from apps.configs.models import Configuration
from reversion.admin import VersionAdmin


class EnvironmentAdmin(admin.ModelAdmin):
    pass


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'app_id', 'active', )


class SettingAdmin(VersionAdmin):
    list_display = ('key', 'value', 'configuration', )
    search_fields = ['key', 'value', 'configuration']
    list_filter = ('configuration', 'key', )


class InlineSettings(admin.TabularInline):
    model = Setting
    extra = 0


class ConfigurationAdmin(admin.ModelAdmin):
    inlines = (InlineSettings, )
    search_fields = ['application', 'environment']
    list_display = ('application', 'environment',)
    list_filter=('application', 'environment', )


admin.site.register(Environment, EnvironmentAdmin)
admin.site.register(Application, ApplicationAdmin)    
admin.site.register(Setting, SettingAdmin)    
admin.site.register(Configuration, ConfigurationAdmin)
