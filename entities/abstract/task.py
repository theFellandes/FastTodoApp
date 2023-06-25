from pydantic import BaseModel, Extra


class Task(BaseModel):
    class Config:
        extra = Extra.forbid
    id_: str
    name: str
    description: str

    def create_task(self):
        """ Creates task for given attributes """

    def delete_task(self, id_: int):
        """ Deletes task for given id """

    def update_task(self, id_: int):
        """ Updates task for given id """

    def get_task(self, id_: int):
        """ Gets task for given id """
