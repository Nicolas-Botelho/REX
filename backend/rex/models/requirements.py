from django.db import models
from polymorphic.models import PolymorphicModel

from rex.models.testcase import TestCase
from rex.models.userstory import Epic

class Requirement(PolymorphicModel, models.Model):
  iD = models.AutoField(primary_key=True)
  description = models.TextField()

class FunctionalRequirement(Requirement):
  testCase = models.ForeignKey(TestCase, related_name="testCase_FunctionalRequirement", on_delete=models.DO_NOTHING)
  epics = models.ForeignKey(Epic, related_name="epic_FunctionalRequirement", on_delete=models.DO_NOTHING)

class NonFunctionalRequirement(Requirement):
  frs = models.ForeignKey(FunctionalRequirement, related_name="functionalRequirement_NonFunctionalRequirement", on_delete=models.DO_NOTHING)

class BusinessRules(Requirement):
  frs = models.ForeignKey(FunctionalRequirement, related_name="functionalRequirement_BusinessRules", on_delete=models.DO_NOTHING)