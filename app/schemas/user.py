from pydantic import BaseModel, ConfigDict


class UserResponse(BaseModel):
    user_id: int
    user_name: str
    user_email: str
    employee_id: int
    role_id: int | None
    is_approved: bool
    is_active: bool

    model_config = ConfigDict(
        from_attributes=True
    )