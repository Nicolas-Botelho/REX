from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from ai_gen.graph.usecase_class_graph import full_graph, usecase_graph, class_graph
from conversion.convert_class import ClassConverter
from conversion.convert_usecase import UsecaseConverter
# from rex.models.klass import Class
# from rex.models.usecase import Usecase
from rex.serializers.request_serializers import RunAllRequestSerializer
from rex.serializers.response_serializers import RunAllResponseSerializer

class AiViewSet(ViewSet):

  @swagger_auto_schema(method='post', request_body=RunAllRequestSerializer, responses={201: RunAllResponseSerializer})
  @action(detail=False, methods=['post'], url_name='run_all')
  def run_all(self, request: Request, *args, **kwargs) -> RunAllResponseSerializer:

    serializer = RunAllRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    input_text = serializer.validated_data.get('input_text')
    
    cc = ClassConverter()
    uc = UsecaseConverter()

    clsInput = cc.load()
    ucInput = uc.load()

    result = full_graph.invoke({'InputText': input_text, 'OldUsecases': ucInput, 'OldClasses': clsInput})

    new_classes = result.get('Classes')
    new_usecases = result.get('Usecases')
    if new_classes:
      cc.save(new_classes)
    if new_usecases:
      uc.save(new_usecases)

    responseSerializer = RunAllResponseSerializer({'classes' : result.get('Classes'), 'usecases' : result.get('Usecases')})
    # responseSerializer.is_valid(raise_exception=True)

    return Response(responseSerializer.data, status=HTTP_201_CREATED)

  def run_usecase(self, request, *args, **kwargs) -> Response:
    pass

  def run_class(self, request, *args, **kwargs) -> Response:
    pass