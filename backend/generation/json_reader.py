import os
import json

class JsonReader():
  def read(self) -> dict:
    filepath = "../out/out.json"

    if os.path.exists(filepath):
      with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)
    else:
      return {}