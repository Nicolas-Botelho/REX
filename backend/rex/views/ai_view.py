from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from drf_yasg.utils import swagger_auto_schema

from ai_gen.graph.usecase_class_graph import full_graph
from ai_gen.models.response_model.class_response import ClassOutput
from ai_gen.models.response_model.usecase_response import UsecaseOutput
from conversion.convert_model import ClassConverter, UsecaseConverter
from conversion.save_class import ClassSaver
from conversion.save_usecases import UsecaseSaver
from rex.serializers.request_serializers import RunAllRequestSerializer
from rex.serializers.response_serializers import RunAllResponseSerializer

class AiViewSet(ViewSet):

  @swagger_auto_schema(method='post', request_body=RunAllRequestSerializer, responses={201: RunAllResponseSerializer})
  @action(detail=False, methods=['post'], url_name='run_all')
  def run_all(self, request: Request, *args, **kwargs) -> Response:

    serializer = RunAllRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    input_text = serializer.validated_data.get('input_text')

    cc = ClassConverter()
    uc = UsecaseConverter()

    clsInput = ClassOutput(classes=cc.load())
    loaded_usecases, loaded_steps = uc.load()
    ucInput = UsecaseOutput(usecases=loaded_usecases, event_steps=loaded_steps)

    result = full_graph.invoke({'InputText': input_text, 'OldUsecases': ucInput, 'OldClasses': clsInput})

    new_classes: ClassOutput = result.get('Classes')
    new_usecases: UsecaseOutput = result.get('Usecases')

    if new_classes or new_usecases:
      cs = ClassSaver()
      class_maps = cs.save_model(new_classes.classes)

      us = UsecaseSaver(class_map=class_maps.get('class_map'), attribute_map=class_maps.get('attribute_map'), relation_map=class_maps.get('relation_map'))
      us.save_model(new_usecases.usecases, new_usecases.event_steps)

    return Response({}, status=HTTP_201_CREATED)