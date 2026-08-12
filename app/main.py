from fastapi import FastAPI

from app.routers.auth import router as auth_router
from app.routers.employee import router as employee_router
from app.routers.admin import router as admin_router
app = FastAPI(
    title="Company Management API"
)


app.include_router(auth_router)
app.include_router(employee_router)
app.include_router(admin_router)
@app.get("/")
def root():
    return {
        "message": "Company Management API is running"
    }