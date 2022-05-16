import json
import logging
import random
import jwt
import requests
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from base.exceptions import UnprocessableEntity
from base.helpers.decorators import exception_handler
from user.helpers import create_tokens
from user.models import User
from user.serializers import UserSerializer, UserTokenSerializer
from user.utils import delete_cache, get_cache, set_cache



@api_view(['POST'])
@permission_classes([AllowAny])
@exception_handler
def registration(request: Request) -> Response:
    username = request.data.get('username')
    try:
        User.objects.get(username=username)
        raise UnprocessableEntity(
            detail='username already exists', code=status.HTTP_406_NOT_ACCEPTABLE)
    except User.DoesNotExist:
        user = User()
        user.username = username
        user.set_password(raw_password=request.data.get('password'))
        user.verified = False
        user.profile_pic_url = request.data.get('profile_pic_url')
        user.address = request.data.get('address')
        user.gender = request.data.get('gender', 'male')
        user.is_staff = request.data.get('is_staff', False)
        user.first_name = request.data.get('first_name')
        user.last_name = request.data.get('last_name')
        user.email = request.data['email']
        user.save()
        return Response(data={'data': UserSerializer(user).data}, status=status.HTTP_201_CREATED)



@api_view(['POST'])
@permission_classes([AllowAny])
def login(request: Request) -> Response:
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        raise ValidationError(
            detail='username and password if required', code=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(username__exact=username)
        if not user.check_password(raw_password=password):
            raise ValidationError(detail='invalid password', code=status.HTTP_400_BAD_REQUEST)
        access_token, refresh_token = create_tokens(user=user)
        data = {
            'access_token': access_token,
            'refresh_token': refresh_token,
        }
        return Response(data=data, status=status.HTTP_201_CREATED)
    except User.DoesNotExist:
        raise ValidationError(detail='user not found', code=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
@permission_classes([AllowAny])
def refreshed_token(request: Request) -> Response:
    refreshed_token = request.data.get('refresh_token')
    try:
        payload = jwt.decode(jwt=refreshed_token, key=settings.SECRET_KEY, algorithms='HS256', verify=True)
        if payload['token_type'] != 'refresh':
            return JsonResponse(data={
                'message': 'no refresh token provided',
                'success': False
            }, status=400)
        user_name = payload.get('username')
        user_obj = get_object_or_404(User, username=user_name)
        if not user_obj.is_active:
            raise ValidationError(detail='user is not active', code=status.HTTP_401_UNAUTHORIZED)
        access_token, refresh_token = create_tokens(user=user_obj)
        data = {
            'access_token': access_token,
            'refresh_token': refresh_token,
        }
        return Response(data=data, status=status.HTTP_201_CREATED)
    except Exception as err:
        return JsonResponse(data={
            'message': f'{str(err)}',
            'success': False,
        }, status=401)


