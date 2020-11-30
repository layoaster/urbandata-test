"""
Set of factories for the Assets models :mod:`urbandata.assets.models`
"""
import factory
from factory.django import DjangoModelFactory


class AssetFactory(DjangoModelFactory):
    """
    Asset factory.
    """

    class Meta:
        model = "assets.Asset"
        exclude = ("id",)

    geom_lat = factory.Faker("pydecimal", right_digits=6, min_value=-90, max_value=90)
    geom_long = factory.Faker("pydecimal", right_digits=6, min_value=-180, max_value=180)
    address = factory.Faker("address")
    area = factory.Faker("pyint", min_value=5, max_value=200)
    rooms = factory.Faker("pyint", min_value=1, max_value=20)
    garage = factory.Faker("pybool")
