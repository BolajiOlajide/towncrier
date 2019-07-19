from django.conf import settings
from slacker import Slacker

from towncrierapp.models import SlackUser, ActivityLog
from towncrierapp.enums import PUBLISH_MESSAGE


slack_client = Slacker(settings.SLACK_BOT_TOKEN)

def send_slack_message(message_queryset):
    message_instance = message_queryset.first()
    if message_instance.published:
        raise Exception('Can\'t publish a previous message :lol:')

    message = message_instance.message
    active_users = SlackUser.objects.filter(isActive=True).all()

    for user in active_users:
        slack_client.chat.post_message(user.slack_id, message, as_user=True)

    return message_instance


def save_activity(request, message):
    return ActivityLog(
        operation=PUBLISH_MESSAGE,
        user=request.user,
        message=message
    ).save()
