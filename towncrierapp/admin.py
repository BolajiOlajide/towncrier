from django.contrib import admin

# Register your models here.
from towncrierapp.models import Message, SlackUser
from django.contrib.auth.models import User


class TownCrierAdminSite(admin.AdminSite):
    site_header = 'TownCrier Administration'


class MessageAdmin(admin.ModelAdmin):
    list_display = ('message',)


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('password',)


class SlackUserAdmin(admin.ModelAdmin):
    exclude = ('password',)


admin_site = TownCrierAdminSite(name='admin')
admin_site.register(User, UserAdmin)
admin_site.register(Message, MessageAdmin)
admin_site.register(SlackUser, SlackUserAdmin)
