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
> OBS: The other variables are optional (see optional .env variables)

3. Create a virtural enviroment and install the Python requirements
```bash
python -m venv .venv
. .venv/bin/activate
pip install -r backend/requirements.txt
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
uvicorn --host 127.0.0.1 --port 8000 app:app
```

6. Optional `.env` variables

| Variable | Meaning | Standard Value |
| -------- | ------- | -------------- |
| LANGSMITH_API_KEY | API key for LangSmith tracing | <none set> |
| LANGSMITH_TRACING | boolean for using tracing | <none set> |
| LANGSMITH_PROJECT | LangSmith project's name | <none set> |
| BACKEND_URL | Used URL in `--host` uvicorn tag | 127.0.0.1 |
| BARCKEND_PORT | Used port in `--port` uvicorn tag | 8000 |
| PROJECT_DIR | Target directory for the JSON files | ../out/ |

## Other informations
* [Architecture](./docs/architecture.md)
* [Models](./docs/models.md)
* [Generation Examples](./example/examples.md)