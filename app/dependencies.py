from fastapi import Depends, HTTPException, status

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.security.jwt import decode_access_token
from fastapi import Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.permission import Permission
from app.models.role_permission import RolePermission
from fastapi.security import HTTPBearer

oauth2_scheme = HTTPBearer()

def get_current_user(
    credentials = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={
            "WWW-Authenticate": "Bearer"
        }
    )

    token = credentials.credentials

    try:
        payload = decode_access_token(token)

        user_id = payload.get("sub")

        if user_id is None:
            raise credentials_exception

        user_id = int(user_id)

    except Exception:
        raise credentials_exception

    user = db.get(User, user_id)

    if user is None:
        raise credentials_exception

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

    return user

def require_permission(
    endpoint: str,
    method: str
):
    def permission_checker(
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
    ):

        if current_user.role_id is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User does not have a role"
            )

        permission = db.scalar(
            select(Permission)
            .join(
                RolePermission,
                RolePermission.permission_id
                == Permission.permission_id
            )
            .where(
                RolePermission.role_id == current_user.role_id,
                Permission.endpoint == endpoint,
                Permission.method == method
            )
        )

        if permission is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to access this endpoint"
            )

        return current_user

    return permission_checker