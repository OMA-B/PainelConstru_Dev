from django.urls import path
from .views import whatsapp_chat


urlpatterns = [
    path('', whatsapp_chat, name='whatsapp_chat'),
]