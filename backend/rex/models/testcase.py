from django.db import models
from polymorphic.models import PolymorphicModel

class TestCase(PolymorphicModel, models.Model):
  iD = models.AutoField(primary_key=True)
  description = models.TextField()