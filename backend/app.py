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

from fastapi import FastAPI, APIRouter, status, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",  # Your Vite/React/Vue frontend
    "http://127.0/.0.1:5173", # Good to add as well
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.post("/manual_update/")
def mu_view(json_input: dict, response: Response, overwrite: bool = False) -> dict:
  try:
    new_classes = HumanClassOutput.model_validate(json_input.get('class_models'))
    new_usecases = UsecaseOutput.model_validate(json_input.get('usecase_models'))
    new_requirements = RequirementOutput.model_validate(json_input.get('requirement_models'))
    new_narrative = NarrativeOutput.model_validate(json_input.get('narrative_models'))

    if new_classes or new_usecases or new_requirements or new_narrative:
      jg = JsonGenerator()
      jg.write_json(new_classes.classes, new_classes.associations, new_classes.inheritances, new_classes.questions,
      new_usecases.usecases, new_usecases.questions,
      new_requirements.requirements, new_requirements.questions,
      new_narrative.domain_narrative, new_narrative.questions, write_new=not overwrite)
  except:
    response.status_code = status.HTTP_400_BAD_REQUEST

  return {}

@app.get("/json/")
def get_json() -> dict:
  jg = JsonGenerator()
  data = jg.return_data()
  
  return {"data": data}

app.include_router(gen_router, tags=["AI"])
app.include_router(class_router, tags=["Class"])
app.include_router(usecase_router, tags=["Usecase"])
app.include_router(requirement_router, tags=["Requirement"])
app.include_router(narrative_router, tags=["Narrative"])