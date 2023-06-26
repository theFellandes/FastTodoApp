import pytest

from settings import settings
from DB.connectors.connector_factory import ConnectorFactory
from DB.connectors.solid.SQL.postgre_sql_connector import PostgreSqlConnector


class TestConnectors:

    @pytest.fixture
    def config_data(self):
        return settings.read_config(settings.get_config_file())

    @pytest.fixture
    def connector_factory(self, config_data):
        return ConnectorFactory(
            host=config_data.get('db').get('host'),
            port=config_data.get('db').get('port'),
            user=config_data.get('db').get('user'),
            password=config_data.get('db').get('password'),
            database=config_data.get('db').get('database'),
            engine_name=config_data.get('db').get('engine')
        )

    def test_data_from_config(self, config_data):
        connector = config_data.get('db').get('engine')
        assert connector == 'postgresql'

    def test_connector(self, config_data):
        connector_factory = ConnectorFactory(
            host=config_data.get('db').get('host'),
            port=config_data.get('db').get('port'),
            user=config_data.get('db').get('user'),
            password=config_data.get('db').get('password'),
            database=config_data.get('db').get('database'),
            engine_name=config_data.get('db').get('engine')
        )
        sql_connector = connector_factory.get_sql_connector()
        assert isinstance(sql_connector, PostgreSqlConnector)
