from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR
from drf_yasg.utils import swagger_auto_schema

from generation.json_generator import JsonGenerator

class JsonGeneratorViewSet(ViewSet):

  @swagger_auto_schema(method='get')
  @action(detail=False, methods=['get'], url_name='json_generator')
  def json_generator(self, request, *args, **kwargs):
    jg = JsonGenerator()
    if jg.create():
      return Response(status=HTTP_201_CREATED)
    else:
      return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)