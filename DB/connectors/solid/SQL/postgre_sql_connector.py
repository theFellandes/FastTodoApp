import psycopg2

from DB.connectors.abstract.SQL.sql_connector import SQLConnector


class PostgreSqlConnector(SQLConnector):

    def connect(self):
        self._connection: psycopg2.connection = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )
        self._cursor: psycopg2.cursor = self._connection.cursor()

    def disconnect(self):
        self._cursor.close()
        self._connection.close()

    def execute(self, query: str):
        self._cursor.execute(query)

    def fetch(self, query: str):
        return self._cursor.fetchall()

    def commit(self):
        self._connection.commit()
