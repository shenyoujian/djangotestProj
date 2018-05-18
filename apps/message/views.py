from django.shortcuts import render
from message.models import UserMessage


# Create your views here.


def getform(request):
    all_message = UserMessage.objects.filter(name="shenyoujian2")
    all_message.delete()
    for message in all_message:
        message.delete()
    if request.method == 'POST':
        name = request.POST.get('name','')
        message = request.POST.get('message','')
        address = request.POST.get('address','')
        email = request.POST.get('email','')

        user_message = UserMessage()
        user_message.name = name
        user_message.message = message
        user_message.address = address
        user_message.email = email
        user_message.object_id = 'lss'
        user_message.save()
    return render(request, 'message_form.html')

