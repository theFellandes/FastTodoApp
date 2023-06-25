from connectors.abstract.sql_connector import SQLConnector


class PostgreSqlConnector(SQLConnector):

    def connect(self):
        ...

    def disconnect(self):
        ...

    def execute(self, query: str):
        ...

    def fetch(self, query: str):
        ...

    def commit(self):
        ...
