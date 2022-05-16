from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from rest_framework import status
from rest_framework.response import Response


def exception_handler(func):
    def inner_function(request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)
        except KeyError as ex:
            return Response({ex.__str__().strip("'"): ["This Field Is Required"]}, status=status.HTTP_400_BAD_REQUEST)
        except (ObjectDoesNotExist, Http404) as ex:
            return Response({'message': ex.__str__()}, status=status.HTTP_404_NOT_FOUND)
            # return Response({'DoesNotExists': ex.__str__()}, status=status.HTTP_404_NOT_FOUND)
    return inner_function
