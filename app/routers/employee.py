from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import require_permission
from app.models.employee import Employee
from app.models.user import User
from app.schemas.employee import EmployeeCreate, EmployeeResponse


router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post(
    "",
    response_model=EmployeeResponse
)
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
    require_permission(
        "/employees",
        "POST"
    )
)
):

    existing_employee = db.scalar(
        select(Employee).where(
            Employee.email == employee.email
        )
    )

    if existing_employee:
        raise HTTPException(
            status_code=409,
            detail="Employee with this email already exists"
        )

    new_employee = Employee(
        name=employee.name,
        email=employee.email,
        salary=employee.salary,
        department_id=employee.department_id
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee