# REX (Requirement Extractor)

A requirement management tool with a requirement from text extraction.

## Requirements
- Python 3.12;
- Gemini API Key;
- Node 22; and
- npm.

## How to Run?

1. Clone the Repository
```bash
git clone https://github.com/Nicolas-Botelho/REX.git
```

2. Create a .env file and add the GEMINI_API_KEY.
> OBS: The Langsmith variables are optional

3. Create a virtural enviroment and install the Python requirements
```bash
python -m venv .venv
.venv/bin/activate
pip install -r requirements.txt
```

4. Build the frontend
```bash
cd frontend/rex
npm i
npm run build
```

5. Run the backend
```bash
cd backend
fastapi dev app.py
```

## Other informations
* [Architecture](./docs/architecture.md)
* [Models](./docs/models.md)
* [Json Generation Example](./example/book.json)