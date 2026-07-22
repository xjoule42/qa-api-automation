import pytest

from src.clients.json_placeholder import JSONPlaceholderClient


@pytest.fixture(scope="session")
def client():
    """
    Creates a single API client instance
    that will be reused during the test session.
    """
    return JSONPlaceholderClient()