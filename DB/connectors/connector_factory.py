from pydantic import BaseModel, Extra

from DB.connectors.abstract.SQL.sql_connector import SQLConnector
from DB.connectors.solid.SQL.mysql_connector import MySqlConnector
from DB.connectors.solid.SQL.postgre_sql_connector import PostgreSqlConnector


class ConnectorFactory(BaseModel):
    class Config:
        extra = Extra.forbid
    host: str
    port: str
    user: str
    password: str
    database: str
    engine_name: str

    # TODO: Add validation for attributes. Also add validation for engine_name

    def get_sql_connector(self) -> SQLConnector:
        """ Returns a SQLConnector """
        match self.engine_name:
            case 'postgresql':
                return PostgreSqlConnector(
                    host=self.host,
                    port=self.port,
                    user=self.user,
                    password=self.password,
                    database=self.database
                )
            case 'mysql':
                return MySqlConnector(
                    host=self.host,
                    port=self.port,
                    user=self.user,
                    password=self.password,
                    database=self.database
                )
            case _:
                raise UnsupportedDatabaseException('Unsupported database entered.')


class UnsupportedDatabaseException(Exception):
    """ Raised when an unsupported database is requested """
    message: str = 'Unsupported database'
