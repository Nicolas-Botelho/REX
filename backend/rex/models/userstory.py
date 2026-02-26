from django.db import models
from polymorphic.models import PolymorphicModel

class Actor(PolymorphicModel, models.Model):
  iD = models.AutoField(primary_key=True)
  name = models.CharField()

class UserStory(PolymorphicModel, models.Model):
  iD = models.AutoField(primary_key=True)
  goal = models.TextField()
  action = models.TextField()
  performer = models.ForeignKey(Actor, related_name="actor_UserStory", on_delete=models.DO_NOTHING)

class Epic(PolymorphicModel, models.Model):
  iD = models.AutoField(primary_key=True)
  userStories = models.ForeignKey(UserStory, related_name="userStory_Epic", on_delete=models.CASCADE)