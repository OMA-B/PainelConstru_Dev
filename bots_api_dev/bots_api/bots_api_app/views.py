from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .serializers import UserSerializer

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .bots.leroy_18 import leroymerlin_spider
from .bots.madeiramadeira_64 import madeiramadeira_spider


# Create your views here.
@api_view(['POST'])
def signup(request):

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(username=request.data['username'])
        token = Token.objects.get(user=user)

        serializer = UserSerializer(user)

        data = {
            'user': serializer.data,
            'token': token.key
        }

        return Response(data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    
    data = request.data
    authenticate_user = authenticate(username=data['username'], password=data['password'])

    if authenticate_user is not None:

        user = User.objects.get(username=data['username'])
        serializer = UserSerializer(user)

        response_data = {'user': serializer.data}

        token_available, token_created = Token.objects.get_or_create(user=user)
        
        if token_available: response_data['token'] = token_available.key
        elif token_created: response_data['token'] = token_created.key

        return Response(response_data)

    return Response({'error': 'user not found: wrong password or username'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def fetch_bots_data(request):

    link = request.GET.get('link')

    if 'www.leroymerlin.com.br' in link: data = leroymerlin_spider(link=link)
    elif 'www.madeiramadeira.com.br' in link: data = madeiramadeira_spider(link=link)

    return Response({'data': data, 'url': link})

@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):

    request.user.auth_token.delete()
    
    return Response({'message': 'successfully logged out.'})