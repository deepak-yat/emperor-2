from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import require_permission
from app.models.user import User
from app.models.role import Role
from app.schemas.auth import ApproveUserRequest



router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/pending-users")
def get_pending_users(
    db: Session = Depends(get_db),
    current_user=Depends(
        require_permission(
            "/admin/pending-users",
            "GET"
        )
    )
):

    users = db.scalars(
        select(User).where(
            User.is_approved == False
        )
    ).all()

    return users

@router.put("/users/{user_id}/approve")
def approve_user(
    user_id: int,
    approval: ApproveUserRequest,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_permission(
            "/admin/users/{user_id}/approve",
            "PUT"
        )
    )
):
    user = db.get(User, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if user.is_approved:
        raise HTTPException(
            status_code=400,
            detail="User is already approved"
        )

    role = db.get(Role, approval.role_id)

    if role is None:
        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    user.role_id = role.role_id
    user.is_approved = True
    user.is_active = True

    db.commit()
    db.refresh(user)

    return {
        "message": "User approved successfully",
        "user_id": user.user_id,
        "role_id": user.role_id,
        "is_approved": user.is_approved,
        "is_active": user.is_active
    }