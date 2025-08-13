# FastAPI Python 3.13 Demo

This project demonstrates key features of Python 3.13 and FastAPI, using a modular structure and a mocked data source.

## Features
- FastAPI APIRouter for modular endpoints
- Python 3.13 features (match statement, dataclass, type hints)
- Dependency injection, background tasks, middleware, exception handling
- Mocked in-memory data source

## Prerequisites
- Python 3.13+

## Setup Instructions

1. **Clone the repository** (if not already):
   ```bash
   git clone <your-repo-url>
   cd py
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI app:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Open your browser to view the API docs:**
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Project Structure
```
py/
├── main.py           # FastAPI app entry point
├── models.py         # Shared models and dependencies
├── mock_data.py      # Mocked data source
├── routers/
│   └── items.py      # APIRouter for item endpoints
├── requirements.txt  # Python dependencies
└── README.md         # Setup and usage instructions
```

## Example Endpoints
- `GET /items/` — List all items
- `POST /items/` — Create a new item
- `PUT /items/{item_id}` — Update an item
- `DELETE /items/{item_id}` — Delete an item
- `GET /items/{item_id}/action?action=do_view` — Demonstrates Python 3.12 match statement

### Example Request
```bash
# Create a new item
curl -X 'POST' \
  'http://localhost:8000/items/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 0,
  "name": "New Item",
  "description": "A sample item"
}'
```

---
Feel free to extend the app with more routers and features!
