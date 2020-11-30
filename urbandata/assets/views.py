"""
Set of views for the Assets API related operations.

Endpoints:
* `/asset`
* `/asset/{Id}`
"""
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from urbandata.assets.models import Asset
from urbandata.assets.serializers import AssetModelSerializer


class AssetListView(ListCreateAPIView):
    """
    Creation and collection-retrieval of assets.

    Endpoint: `/asset`
    """

    permission_classes = (permissions.AllowAny,)
    queryset = Asset.objects.all()
    serializer_class = AssetModelSerializer


class AssetDetailView(RetrieveAPIView):
    """
    Retrieval of assets.

    Endpoint: `/asset/{Id}`
    """

    permission_classes = (permissions.AllowAny,)
    queryset = Asset.objects.all()
    serializer_class = AssetModelSerializer
    lookup_field = "id"
