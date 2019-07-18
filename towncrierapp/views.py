from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from towncrierapp.models import SlackUser


@csrf_exempt
def bot_actions(request):
  slack_id = request.POST.get('user_id')
  action = request.POST.get('text')
  handle = request.POST.get('user_name')
  
  if not slack_id:
    return JsonResponse({'text': 'Request not verified.'})

  user_details = dict(
    slack_id=slack_id,
    handle=handle
  )

  if action == 'opt-in':
    user_details['isActive'] = True
    SlackUser.upsert(**user_details)
    message = f"""_Hello_ <@{slack_id}>,

_You've just opted in to the town crier notification system. You'll receive important company-wide information from me._

_If you wish to opt out at any point in time, feel free to use the slash command_ `/towncrier opt-out`
"""
  elif action == 'opt-out':
    user_details['isActive'] = False
    SlackUser.upsert(**user_details)
    message = f"""_Hello_ <@{slack_id}>,

_You've just opted out of the town crier notification system. You'll no longer receive important company-wide information from me._

_If you wish to opt in at any point in time, feel free to use the slash command_ `/towncrier opt-in`
"""
  else:
    message = f"""*Help:*

- `/towncrier opt-in` to opt into town crier notification
- `/towncrier opt-out` to opt out of town crier notification
- `/towncrier help` to view the help
"""

  return JsonResponse({'text': message})
