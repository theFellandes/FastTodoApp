from pydantic import BaseModel, Extra


class SQLConnector(BaseModel):
    class Config:
        extra = Extra.forbid
    host: str
    port: int
    user: str
    password: str
    database: str

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        """ Connects to database """

    def disconnect(self):
        """ Disconnects from database """

    def execute(self, query: str):
        """ Executes query """

    def fetch(self, query: str):
        """ Fetches query """

    def commit(self):
        """ Commits changes """
