from pydantic import BaseModel


class LoginRequest(BaseModel):
    user_name: str
    user_password: str

class RegisterRequest(BaseModel):
    user_name: str
    user_email: str
    user_password: str