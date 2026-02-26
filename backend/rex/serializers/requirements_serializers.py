from rest_framework import serializers

from rex.models.requirements import FunctionalRequirement, NonFunctionalRequirement, BusinessRules

class FunctionalRequirementSerializer(serializers.ModelSerializer):
  class Meta:
    model = FunctionalRequirement
    exclude = ('polymorphic_ctype',)

class NonFunctionalRequirementSerializer(serializers.ModelSerializer):
  class Meta:
    model = NonFunctionalRequirement
    exclude = ('polymorphic_ctype',)

class BusinessRulesSerializer(serializers.ModelSerializer):
  class Meta:
    model = BusinessRules
    exclude = ('polymorphic_ctype',)