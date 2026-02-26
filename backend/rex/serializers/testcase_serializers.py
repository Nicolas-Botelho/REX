from rest_framework import serializers

from rex.models.testcase import TestCase

class TestCaseSerializer(serializers.Serializer):
  iD = serializers.IntegerField(read_only=True)
  description = serializers.CharField()

  class Meta:
    model = TestCase
    exclude = ('polymorphic_ctype',)
