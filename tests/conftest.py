"""
Fixtures meant to be session-wide or commonly use in test at lower levels
so they have to be globally accessible.
"""
import pytest

from tests.factories import assets


############### Factories ############### noqa
# ASSETS
@pytest.fixture
def asset_factory(db):
    """InsuranceUser factory as fixture."""
    return assets.AssetFactory
