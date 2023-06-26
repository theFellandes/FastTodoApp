import mysql.connector

from DB.connectors.abstract.SQL.sql_connector import SQLConnector


class MySqlConnector(SQLConnector):

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def execute(self, query: str):
        self.cursor.execute(query)

    def fetch(self, query: str):
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()
