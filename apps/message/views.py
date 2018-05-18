from django.shortcuts import render
from message.models import UserMessage


# Create your views here.


def getform(request):
    message = None
    all_message = UserMessage.objects.filter(name="shen")
    if all_message:
        message = all_message[0]
    return render(request, 'message_form.html',{
        "my_message":message
    })

