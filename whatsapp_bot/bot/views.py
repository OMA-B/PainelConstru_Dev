from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv('IGOR_ACCOUNT_SID')
auth_token = os.getenv('IGOR_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# Create your views here.
@csrf_exempt
def whatsapp_chat(requests):
    message = requests.POST['Body']
    sender_num = requests.POST['From']
    sender_name = requests.POST['ProfileName']
    print(message)
    print(sender_name)
    print(sender_num)
    
    if message in ('hello', 'hi', 'hey'):
        client.messages.create(
            from_='whatsapp:+14155238886',
            body=f'hey there {sender_name}.' if message == 'hello' else f'hey there {sender_name}. how are you doing today?',
            to=sender_num
        )
        print(f'{sender_name} said {message}')

    
    return HttpResponse(content='Success!')