from django.contrib import admin
from django.contrib.auth.models import User

from towncrierapp.models import Message, SlackUser
from towncrierapp.utils import send_slack_message, save_activity


class TownCrierAdminSite(admin.AdminSite):
    site_header = 'TownCrier Administration'


class MessageAdmin(admin.ModelAdmin):
    actions = ['publish_message']
    list_display = ('message', 'published')
    readonly_fields = ('published',)

    def publish_message(self, request, queryset):
        message = send_slack_message(queryset)
        save_activity(request, message)
        queryset.update(published=True)
    publish_message.short_description = 'Publish message via TownCrier'


class UserAdmin(admin.ModelAdmin):
    exclude = ('password',)
    readonly_fields = ('password',)
    list_display = ('username', 'email', 'is_superuser')


class SlackUserAdmin(admin.ModelAdmin):
    list_display = ('slack_id', 'handle', 'isActive')


admin_site = TownCrierAdminSite(name='admin')
admin_site.register(User, UserAdmin)
admin_site.register(Message, MessageAdmin)
admin_site.register(SlackUser, SlackUserAdmin)
