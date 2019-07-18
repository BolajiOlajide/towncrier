from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def send_message(request):
  pass


@csrf_exempt
def bot_actions(request):
  user_id = request.POST.get('user_id')
  action = request.POST.get('text')
  print(request.POST)
  

  if not user_id:
    return JsonResponse({'text': 'Request not verified.'})

  if action == 'opt-in':
    message = f"""Hello <@{user_id}>,

You've just opted in to the town crier notification system. You'll receive important company
wide information from me.

If you wish to opt out at any point in time, feel free to use the slash command `/towncrier opt-out`
"""
  elif action == 'opt-out':
    message = f"""Hello <@{user_id}>,

You've just opted out of the town crier notification system. You'll no longer receive important company
wide information from me.

If you wish to opt in at any point in time, feel free to use the slash command `/towncrier opt-in`
"""
  else:
    message = f"""*Help:*

- `/towncrier opt-in` to opt into town crier notification
- `/towncrier opt-out` to opt out of town crier notification
- `/towncrier help` to view the help
"""
  return JsonResponse({'text': message})
