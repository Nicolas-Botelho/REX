from typing import List
from pydantic import BaseModel

class Actor(BaseModel):
  iD = int
  name = str

class UserStory(BaseModel):
  iD = int
  goal = str
  action = str
  performer = List[Actor]

class Epic(BaseModel):
  iD = int
  userStories = List[UserStory]