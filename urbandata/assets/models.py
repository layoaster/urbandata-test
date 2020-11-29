"""
Real State Assets related models.
"""
from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models


class Asset(models.Model):
    """
    Data of a real state asset.
    """

    #: Geometric latitude.
    geom_lat = models.DecimalField(max_digits=9, decimal_places=6)
    #: Geometric longitude.
    geom_long = models.DecimalField(max_digits=9, decimal_places=6)
    #: Asset's location.
    address = models.CharField(blank=True, max_length=256)
    #: Asset's geometric area.
    area = models.IntegerField()
    #: Asset's number of rooms (if applicable).
    rooms = models.IntegerField(null=True)
    #: Asset's garage flag (if applicable).
    garage = models.BooleanField(null=True)
    #: Asset's extra data that is JSON serializable.
    other = JSONField(encoder=DjangoJSONEncoder, default=dict)

    class Meta:
        db_table = "assets_asset"
        verbose_name = "asset"
        verbose_name_plural = "assets"

    def __repr__(self) -> str:
        """
        Model's human-readable string representation.

        :return: Model string representation.
        """
        return (
            f"<Asset: geom='({self.geom_lat}, {self.geom_long})', address='{self.address}', "
            f"area='{self.area}', rooms='{self.rooms}', garage='{self.garage}'>"
        )
