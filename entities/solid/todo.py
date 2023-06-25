from entities.abstract.task import Task


class TodoTask(Task):
    def create_task(self):
        ...

    def delete_task(self, id_: int):
        ...

    def update_task(self, id_: int):
        ...

    def get_task(self, id_: int):
        ...
