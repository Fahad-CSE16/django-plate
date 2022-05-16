import uuid
import mimetypes

from django.conf import settings
from django.apps import apps
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from base.helpers.decorators import exception_handler
from base.helpers.func import get_model_from_any_app
from user.permissions import IsSuperUser, IsStaff



@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request: Request) -> Response:
    data = {
        'message': 'searchlight api service',
        'method': request.method
    }
    return Response(data={'message': data}, status=status.HTTP_200_OK)
