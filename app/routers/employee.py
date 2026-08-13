from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import require_permission
from app.models.employee import Employee
from app.models.user import User
from app.schemas.employee import EmployeeCreate, EmployeeResponse
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeResponse
)
from app.dependencies import get_db, get_current_user
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

@router.get(
    "",
    response_model=list[EmployeeResponse]
)
def get_employees(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_permission(
            "/employees",
            "GET"
        )
    )
):
    return db.scalars(
        select(Employee)
    ).all()


@router.put(
    "/{employee_id}",
    response_model=EmployeeResponse
)
def update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_permission(
            "/employees/{employee_id}",
            "PUT"
        )
    )
):
    db_employee = db.get(Employee, employee_id)

    if db_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    db_employee.name = employee.name
    db_employee.email = employee.email
    db_employee.salary = employee.salary
    db_employee.department_id = employee.department_id

    db.commit()
    db.refresh(db_employee)

    return db_employee

@router.get(
    "/me",
    response_model=EmployeeResponse
)
def view_employee(
    db:Session=Depends(get_db),
    current_user: User=Depends(get_current_user)
):
    employee=db.get(Employee,current_user.employee_id)

    if employee == None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

 

    return employee