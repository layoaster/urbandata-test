"""
Set of serializers used by Asset's views :mod:`urbandata.assets.views`.
"""
from rest_framework import serializers

from urbandata.assets import models


class AssetModelSerializer(serializers.ModelSerializer):
    """
    Serializer for the model :class:`urbandata.assets.models.Asset`.
    """

    class Meta:
        model = models.Asset
        fields = "__all__"

    #: Asset's area validation.
    area = serializers.IntegerField(min_value=0)
    #: Asset's room validation.
    rooms = serializers.IntegerField(required=False, min_value=0)
