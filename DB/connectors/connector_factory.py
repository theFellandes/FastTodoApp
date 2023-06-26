from pydantic import BaseModel, Extra

from DB.connectors.abstract.SQL.sql_connector import SQLConnector
from DB.connectors.solid.SQL.mysql_connector import MySqlConnector
from DB.connectors.solid.SQL.postgre_sql_connector import PostgreSqlConnector


class ConnectorFactory(BaseModel):
    class Config:
        extra = Extra.forbid
    _host: str
    _port: str
    _user: str
    _password: str
    _database: str
    _engine_name: str

    # TODO: Add validation for attributes. Also add validation for engine_name

    def get_sql_connector(self) -> SQLConnector:
        """ Returns a SQLConnector """
        match self._engine_name:
            case 'postgresql':
                return PostgreSqlConnector(
                    host=self._host,
                    port=self._port,
                    user=self._user,
                    password=self._password,
                    database=self._database
                )
            case 'mysql':
                return MySqlConnector(
                    host=self._host,
                    port=self._port,
                    user=self._user,
                    password=self._password,
                    database=self._database
                )
            case _:
                raise UnsupportedDatabaseException('Unsupported database entered.')


class UnsupportedDatabaseException(Exception):
    """ Raised when an unsupported database is requested """
    message: str = 'Unsupported database'
