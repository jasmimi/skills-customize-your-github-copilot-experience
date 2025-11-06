# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a small REST API using the FastAPI framework. Students will practice designing endpoints, using Pydantic models for validation, and running a development server.

## 📝 Tasks

### 🛠️	Core REST API

#### Description
Create a small REST API in Python using FastAPI that supports basic CRUD operations for a simple resource (for example, "items"). The API should include request validation, clear responses, and basic error handling.

#### Requirements
Completed program should:

- Provide endpoints to Create, Read (single + list), Update, and Delete an "item" resource.
- Use Pydantic models for request validation and response models.
- Return appropriate HTTP status codes (201 for created, 404 for not found, 200/204 for success, etc.).
- Validate input and return helpful error messages for invalid data.
- Include clear README instructions for starting the app locally with Uvicorn.

Example quick endpoints:

- GET /items — list items
- GET /items/{id} — retrieve an item
- POST /items — create an item
- PUT /items/{id} — update an item
- DELETE /items/{id} — delete an item

### 🛠️	Optional Enhancements

#### Description
Add one or more optional features to improve the API or the developer experience.

#### Requirements
Completed enhancement examples (pick any):

- Add simple in-memory persistence with startup sample data, or use SQLite via SQLModel/SQLAlchemy.
- Implement query parameters for filtering, sorting, or pagination on list endpoints.
- Add automated tests for core handlers (pytest + httpx/Starlette test client).
- Add OpenAPI metadata (tags, descriptions) and example request/response bodies.
- Add basic authentication (API key or simple token) for protected endpoints.

## 📎 Starter code

Starter files included in this assignment:

- `main.py` — minimal FastAPI app with example CRUD endpoints.
- `requirements.txt` — pinned dependencies to run the app.

Run the starter app locally:

```bash
# create a virtualenv (recommended)
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# run the app
uvicorn main:app --reload --port 8000
```

Open the interactive API docs at: http://127.0.0.1:8000/docs

## ✅ Submission

Include:

- `main.py` — your completed API (or a clear README describing how to run if you split code into modules).
- Optional: tests (e.g., `tests/test_api.py`) and `requirements.txt` if you changed dependencies.

Good luck building your API!
