from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404

from rex.models.testcase import TestCase
from rex.serializers.testcase_serializers import TestCaseSerializer

class TestCaseViewSet(ModelViewSet):
    serializer_class = TestCaseSerializer
    queryset = TestCase.objects.all()