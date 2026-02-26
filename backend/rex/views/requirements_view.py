from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404

from rex.models.requirements import FunctionalRequirement, NonFunctionalRequirement, BusinessRules
from rex.serializers.requirements_serializers import FunctionalRequirementSerializer, NonFunctionalRequirementSerializer, BusinessRulesSerializer

class FunctionalRequirementViewSet(ModelViewSet):
    serializer_class = FunctionalRequirementSerializer
    queryset = FunctionalRequirement.objects.all()

class NonFunctionalRequirementViewSet(ModelViewSet):
    serializer_class = NonFunctionalRequirementSerializer
    queryset = NonFunctionalRequirement.objects.all()

class BusinessRulesViewSet(ModelViewSet):
    serializer_class = BusinessRulesSerializer
    queryset = BusinessRules.objects.all()