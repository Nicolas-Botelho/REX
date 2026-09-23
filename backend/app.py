from models.response_model.class_response import ClassOutput, HumanClassOutput
from models.response_model.usecase_response import UsecaseOutput
from models.response_model.requirement_response import RequirementOutput
from models.response_model.narrative_response import NarrativeOutput
from generation.json_generator import JsonGenerator

from views.class_view import class_router
from views.usecase_view import usecase_router
from views.requirement_view import requirement_router
from views.narrative_view import narrative_router
from views.ai_view import gen_router
from views.actor_view import actor_router
from views.document_view import doc_router
from views.project_view import project_router

from fastapi import FastAPI, APIRouter, status, Response
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()

if not os.environ.get("BACKEND_URL"):
  os.environ["BACKEND_URL"] = "http://localhost"
if not os.environ.get("BACKEND_PORT"):
  os.environ["BACKEND_PORT"] = "8000"
if not os.environ.get("PROJECT_DIR"):
  os.environ["PROJECT_DIR"] = "../out/"

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    # "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/project/{project_id}/manual_update/")
def mu_view(project_id: int, json_input: dict, response: Response, overwrite: bool = False) -> dict:
  try:
    if json_input.get('narrative_models') or json_input.get('requirement_models') or json_input.get('usecase_models') or json_input.get('class_models') or json_input.get('actors'):
      jg = JsonGenerator(project_id)
      jg.write_json(json_input, write_new=not overwrite)
  except Exception as e:
    response.status_code = status.HTTP_400_BAD_REQUEST

  return {}

@app.get("/project/{project_id}/json/")
def get_json(project_id: int) -> dict:
  jg = JsonGenerator(project_id)
  data = jg.return_data()
  
  return {"data": data}

app.include_router(project_router, tags=["Project"])
app.include_router(gen_router, tags=["AI"])
app.include_router(class_router, tags=["Class"])
app.include_router(usecase_router, tags=["Usecase"])
app.include_router(requirement_router, tags=["Requirement"])
app.include_router(narrative_router, tags=["Narrative"])
app.include_router(actor_router, tags=["Actor"])
app.include_router(doc_router, tags=["Documents"])

try:
  app.frontend("/", directory="../frontend/rex/dist")
except Exception as e:
  print(f"ERROR: No frontend build found ({e})")

@app.get("/make_coffee/", responses={200: {"status": 200, "data": "OK"}, 418: {"status": 418, "data": "I'm a Teapot"}})
def make_coffee(response: Response):
  response.status_code = status.HTTP_418_IM_A_TEAPOT
  return {"status": 418, "data": "I'm a Teapot"}