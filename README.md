# REX (Requirement Extractor)

A requirement management tool with a requirement from text extraction.

## How to Run?

1. Clone the Repository
```bash
git clone 
```

2. Create a virtual enviroment and install the requirements
```bash
python -m venv .venv
.venv/bin/activate

pip install -r requirements.txt
```

3. Create a .env file and add the enviroment variables

4. Run the backend

  4.1. Go to the backend folder and run
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

5. Run the frontend

  5.1 Go to the frontend folder and run
```bash
python streamlit app.py
```

## Archtecture
```mermaid
flowchart

subgraph Backend
  A[AI]
  B[Conversion Layer]
  C["SQLite (Django ORM)"]
  D[Django Management]
end

subgraph Frontend
  E[Frontend App]
end

A <--> B
B <--> D
D <--> C
D <--> E

```

### Models

#### Class Diagram
```mermaid
classDiagram

class Enum {
  iD : int
  name : String
}

class EnumAttribute {
  iD : int
  value : String
}

class Class {
  iD : int
  name : String
}

class ClassAttributePrim {
  iD : int
  name : String
  attr_type : PrimitiveTypes
}

class ClassAtributeEnum {
  iD : int
  name : String
}

class RelationClassReference {
  iD : int
  minim : int
  maxim : int
}

class Relation {
  iD : int
}

Enum "1" -- "0..*" EnumAttribute
Class "1" -- "0..*" ClassAttributePrim
Enum "1" -- "0..*" ClassAttributeEnum
Class "1" -- "0..*" ClassAttributeEnum
Class "1" -- "0..*" RelationClassReference
RelationClassReference "2" -- "0..*" Relation

note for Relation "2 relationships with RelationClassReference</br>One for Source Class and one for Target Class"
```

#### Use Case Model
```mermaid
classDiagram

class Usecase {
  iD : int
  name : String
}

class Event {
  iD : int
  name : String
}

class Step {
  iD : int
  system : boolean
  description : String
}

class Actor {
  iD : int
  name : String
  description : String
}

Usecase "1" -- "0..*" Event
Event "1" -- "0..*" Step
Event "1..*" -- "1" Actor

note for Step "system is True for a System Action and False for a Actor Action"
```