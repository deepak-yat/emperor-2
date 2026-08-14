from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.dependencies import get_current_user
from app.schemas.user import UserResponse
from app.database import get_db

from app.models.user import User
from app.schemas.auth import LoginRequest
from app.security.password import verify_password
from app.security.jwt import create_access_token
from app.models.employee import Employee
from app.security.password import hash_password
from app.schemas.auth import RegisterRequest
from app.models.role import Role
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.get("/me", response_model=UserResponse)
def get_me(
    current_user: User = Depends(get_current_user)
):
    return current_user

@router.post("/login")
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db)
):

    user = db.scalar(
        select(User).where(
            User.user_name == credentials.user_name
        )
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    if not verify_password(
        credentials.user_password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    if not user.is_approved:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is not approved"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive"
        )

    access_token = create_access_token(
        user.user_id
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.post("/register", status_code=201)
def register(
    user_data: RegisterRequest,
    db: Session = Depends(get_db)
):

    # 1. Find employee using email
    employee = db.scalar(
        select(Employee).where(
            Employee.email == user_data.user_email
        )
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="No employee found with this email"
        )

    # 2. Check if user already exists
    existing_user = db.scalar(
        select(User).where(
            User.employee_id == employee.id
        )
    )

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="User account already exists"
        )

    # 3. Check username
    existing_username = db.scalar(
        select(User).where(
            User.user_name == user_data.user_name
        )
    )

    if existing_username:
        raise HTTPException(
            status_code=409,
            detail="Username already exists"
        )

    # 4. Create user
    new_user = User(
        user_name=user_data.user_name,
        user_email=employee.email,
        hashed_password=hash_password(
            user_data.user_password
        ),
        employee_id=employee.id,

        # No role during registration
        role_id=None,

        # Waiting for admin
        is_approved=False,
        is_active=False
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "Registration successful. Waiting for admin approval.",
        "user_id": new_user.user_id
    }

@router.get("/me", response_model=UserResponse)
def get_me(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    role = None

    if current_user.role_id is not None:
        role = db.get(Role, current_user.role_id)

    return {
        "user_id": current_user.user_id,
        "user_name": current_user.user_name,
        "user_email": current_user.user_email,
        "employee_id": current_user.employee_id,
        "role_id": current_user.role_id,
        "role_name": role.role_name if role else None,
        "is_approved": current_user.is_approved,
        "is_active": current_user.is_active
    }