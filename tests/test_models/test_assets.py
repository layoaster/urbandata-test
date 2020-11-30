"""
Set of tests for the assets models on :mod:`urbandata.assets.models`.
"""


class TestAsset:
    """
    Set of tests for the methods of the :class:`urbandata.assets.models.Asset`
    model.
    """

    def test_model_repr(self, asset_factory):
        """
        Test :meth:`urbandata.assets.models.Asset.__repr__`.
        """
        asset = asset_factory()

        assert str(asset.geom_lat) in repr(asset)
        assert str(asset.geom_long) in repr(asset)
        assert asset.address in repr(asset)
        assert str(asset.area) in repr(asset)
        assert str(asset.rooms) in repr(asset)
        assert str(asset.garage) in repr(asset)
