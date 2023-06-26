from settings import settings
from DB.connectors.connector_factory import ConnectorFactory


def test_connector():
    config_data = settings.read_config(settings.get_config_file())
    connector_factory = ConnectorFactory(
        host=config_data.get('db').get('host'),
        port=config_data.get('db').get('port'),
        user=config_data.get('db').get('user'),
        password=config_data.get('db').get('password'),
        database=config_data.get('db').get('database'),
        engine_name=config_data.get('db').get('engine')
    )
    sql_connector = connector_factory.get_sql_connector()
    with sql_connector:
        sql_connector.fetch('SELECT * FROM tasks;')


if __name__ == '__main__':
    test_connector()
