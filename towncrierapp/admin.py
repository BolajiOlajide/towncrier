from django.contrib import admin

# Register your models here.
from towncrierapp.models import Message
from django.contrib.auth.models import User


class TownCrierAdminSite(admin.AdminSite):
    site_header = 'TownCrier Administration'


class MessageAdmin(admin.ModelAdmin):
    list_display = ('word',)


class UserAdminSite(admin.ModelAdmin):
    readonly_fields = ('password',)


admin_site = TownCrierAdminSite(name='admin')
admin_site.register(User, UserAdminSite)
admin_site.register(Message, MessageAdmin)
