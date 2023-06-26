import mysql.connector

from DB.connectors.abstract.SQL.sql_connector import SQLConnector


class MySqlConnector(SQLConnector):

    def connect(self):
        self._connection = mysql.connector.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )
        self._cursor = self._connection.cursor()

    def disconnect(self):
        self._cursor.close()
        self._connection.close()

    def execute(self, query: str):
        self._cursor.execute(query)

    def fetch(self, query: str):
        return self._cursor.fetchall()

    def commit(self):
        self._connection.commit()
