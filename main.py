"""
FastAPI app demonstrating Python 3.13 and FastAPI features.
"""
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import mock_data
from routers.items import router as items_router

app = FastAPI(title="Python 3.13 & FastAPI Demo", description="Showcases key features.")

# Register the items router
app.include_router(items_router)
# Middleware example: CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency and models are now in routers/items.py
# Exception handler example
@app.exception_handler(HTTPException)
def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail, "custom": True})

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Python 3.12 & FastAPI demo! Routers are used for /items endpoints."}
