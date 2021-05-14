from pydantic import BaseModel


class BaseDTO(BaseModel):
    class Config:
        arbitrary_types_allowed = True
