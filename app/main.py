from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.routers.auth import router as auth_router
from app.routers.employee import router as employee_router
from app.routers.admin import router as admin_router


app = FastAPI(
    title="Company Management API"
)


# -------------------------
# API routers
# -------------------------

app.include_router(auth_router)
app.include_router(employee_router)
app.include_router(admin_router)


# -------------------------
# Frontend
# -------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"


app.mount(
    "/static",
    StaticFiles(directory=FRONTEND_DIR),
    name="static"
)


@app.get("/", include_in_schema=False)
def home():
    return FileResponse(
        FRONTEND_DIR / "index.html"
    )


@app.get("/login", include_in_schema=False)
def login_page():
    return FileResponse(
        FRONTEND_DIR / "pages" / "login.html"
    )


@app.get("/register", include_in_schema=False)
def register_page():
    return FileResponse(
        FRONTEND_DIR / "pages" / "register.html"
    )

@app.get("/dashboard", include_in_schema=False)
def dashboard_page():
    return FileResponse(
        FRONTEND_DIR / "pages" / "dashboards" / "admin.html"
    )

@app.get("/dashboard/admin", include_in_schema=False)
def admin_dashboard_page():
    return FileResponse(
        FRONTEND_DIR / "pages" / "dashboards" / "admin.html"
    )

@app.get("/dashboard/hr", include_in_schema=False)
def hr_dashboard_page():
    return FileResponse(
        FRONTEND_DIR / "pages" / "dashboards" / "hr.html"
    )

@app.get("/employees", include_in_schema=False)
def employees_page():
    return FileResponse(
        FRONTEND_DIR / "pages" / "employees.html"
    )

@app.get("/dashboard/manager", include_in_schema=False)
def manager_dashboard_page():
    return FileResponse(
        FRONTEND_DIR / "pages" / "dashboards" / "manager.html"
    )

@app.get("/employees/create-page", include_in_schema=False)
def create_employee_page():
    return FileResponse(
        FRONTEND_DIR / "pages" / "create-employee.html"
    )

@app.get("/employee-list", include_in_schema=False)
def employee_list_page():
    return FileResponse(
        FRONTEND_DIR / "pages" / "employee-list.html"
    )