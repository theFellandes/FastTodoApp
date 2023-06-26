import os
import pytest

from settings import settings


@pytest.fixture
def config_file():
    return settings.get_config_file()


def test_config_file_path(config_file):
    actual_path = settings.get_settings_path()
    if 'dev' in os.environ:
        actual_path = os.path.join(actual_path, 'config_dev.yaml')
    else:
        actual_path = os.path.join(actual_path, 'config.yaml')
    assert config_file == actual_path


def test_config_file_contents(config_file):
    # TODO: Cover this test case.
    settings.read_config(config_file)
