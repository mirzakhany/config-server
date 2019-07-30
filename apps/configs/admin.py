from django.contrib import admin
from apps.configs.models import Enviorment
from apps.configs.models import Application
from apps.configs.models import Setting
from apps.configs.models import Configuration
# Register your models here. 

class EnviormentAdmin(admin.ModelAdmin):
    pass


class ApplicationAdmin(admin.ModelAdmin):
    pass


class SettingAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'configuration', )
    search_fields = ['key', 'value', 'configuration']
    list_filter=('configuration', 'key', ) 


class InlineSettings(admin.TabularInline):
    model = Setting
    extra = 0


class ConfigurationAdmin(admin.ModelAdmin):
    inlines = (InlineSettings, )
    search_fields = ['application', 'enviorment']
    list_display = ('application', 'enviorment',)
    list_filter=('application', 'enviorment', )        


admin.site.register(Enviorment, EnviormentAdmin)    
admin.site.register(Application, ApplicationAdmin)    
admin.site.register(Setting, SettingAdmin)    
admin.site.register(Configuration, ConfigurationAdmin)    