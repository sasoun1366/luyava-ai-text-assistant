# LUYAVA AI Task API

A small REST API created as a test project for the LUYAVA Engineering Agent workflow.

## Run

Windows:
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

API: http://127.0.0.1:8080

## Test

```bash
pytest -q
```

## Endpoints

- GET /health
- GET /api/tasks
- POST /api/tasks
- PATCH /api/tasks/:id
- DELETE /api/tasks/:id

## Agency challenge

Use the Engineering agents to review and improve this project.

Expected workflow:

Architecture review -> Code review -> Security review -> Tests -> DevOps/CI -> Pull Request.

Do not modify main directly. Work on a feature branch and open a PR.
