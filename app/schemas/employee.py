from pydantic import BaseModel, ConfigDict


class EmployeeCreate(BaseModel):
    name: str
    email: str
    salary: float
    department_id: int


class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: str
    salary: float
    department_id: int

    model_config = ConfigDict(
        from_attributes=True
    )

class EmployeeUpdate(BaseModel):
    name: str
    email: str
    salary: float
    department_id: int