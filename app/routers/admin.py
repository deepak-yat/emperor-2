from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import require_permission
from app.models.user import User


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