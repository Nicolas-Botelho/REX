from rex.models import klass as cls_mod
from rex.models import usecase as uc_mod
from rex.serializers import class_serializers as cls_ser
from rex.serializers import usecase_serializers as uc_ser

class JsonClassSerializer():
  def get(self):
    queryset = cls_mod.Class.objects.all()
    serializer = cls_ser.ClassSerializer(queryset, many=True)
    return list(serializer.data)

class JsonEnumSerializer():
  def get(self):
    queryset = cls_mod.Enum.objects.all()
    serializer = cls_ser.EnumSerializer(queryset, many=True)
    return list(serializer.data)

class JsonUseCaseSerializer():
  def get(self):
    queryset = uc_mod.Usecase.objects.all()
    serializer = uc_ser.UsecaseSerializer(queryset, many=True)
    return list(serializer.data)

class JsonActorSerializer():
  def get(self):
    queryset = uc_mod.Actor.objects.all()
    serializer = uc_ser.ActorSerializer(queryset, many=True)
    return list(serializer.data)
  
class JsonStepSerializer():
  def get(self):
    queryset = uc_mod.Step.objects.all()
    serializer = uc_ser.StepSerializer(queryset, many=True)
    return list(serializer.data)