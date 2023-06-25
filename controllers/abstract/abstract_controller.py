from pydantic import BaseModel, Extra


class AbstractController(BaseModel):
    class Config:
        extra = Extra.forbid
