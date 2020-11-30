"""
Set of tests of the Assets views :mod:`urbandata.assets.views`.
"""
import pytest

from django.urls import reverse


############################### Fixtures ############################### noqa
@pytest.fixture
def assets_set(asset_factory):
    """
    Fixed set of assets to test resource retrieval.
    """
    return asset_factory.create_batch(3)


################################ Tests ############################### noqa
class TestAssetListView:
    """
    Test the :class:`urbandata.assets.views.AssetListView` view.
    """

    def test_post(self, authless_api_client):
        """
        Test valid POST request.
        """
        payload = {
            "geom_lat": "50.456743",
            "geom_long": "-3.567895",
            "address": "",
            "area": 35,
            "rooms": 2,
        }

        resp = authless_api_client.post(reverse("asset:asset_list"), payload)
        assert resp.status_code == 201

    def test_post_with_invalid_params(self, authless_api_client):
        """
        Test POST request with invalid parameters (missing a mandatory field).
        """
        payload = {
            "geom_lat": "50.456743",
            "geom_long": "-3.567895",
            "address": "",
            "rooms": 2,
            "garage": "false",
        }

        resp = authless_api_client.post(reverse("asset:asset_list"), payload)
        assert resp.status_code == 400
        assert "This field is required" in resp.json()["area"][0]

    def test_get(self, authless_api_client, assets_set):
        """
        Test GET request returns all the existent assets.
        """
        resp = authless_api_client.get(reverse("asset:asset_list"))
        resp_json = resp.json()

        assert resp.status_code == 200
        assert len(resp_json) == 3


class TestAssetDetailView:
    """
    Test the :class:`urbandata.assets.views.AssetDetailView` view.
    """

    def test_get(self, authless_api_client, assets_set):
        """
        Test that a GET request returns the corresponding asset.
        """
        asset = assets_set[1]

        resp = authless_api_client.get(reverse("asset:asset_detail", kwargs={"id": asset.id}))
        resp_json = resp.json()

        assert resp.status_code == 200
        assert resp_json["id"] == asset.id

    def test_get_with_invalid_asset_id(self, authless_api_client, assets_set):
        """
        Test that a GET request returns the corresponding asset.
        """
        resp = authless_api_client.get(reverse("asset:asset_detail", kwargs={"id": 200}))

        assert resp.status_code == 404
