import psycopg2

from DB.connectors.abstract.SQL.sql_connector import SQLConnector


class PostgreSqlConnector(SQLConnector):

    def connect(self):
        self.connection: psycopg2.connection = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )
        self.cursor: psycopg2.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def execute(self, query: str):
        self.cursor.execute(query)

    def fetch(self, query: str):
        self.execute(query)
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()
