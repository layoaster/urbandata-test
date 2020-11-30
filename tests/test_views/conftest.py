"""
Set of fixtures shared across view tests.
"""
import pytest

from rest_framework.test import APIClient


@pytest.fixture
def authless_api_client(db):
    """
    DjangoRestFramework test client without authentication.
    """
    return APIClient()
