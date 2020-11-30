"""
Set of URLs relative to the endpoint `/api/urbandata/asset/`
"""
from django.urls import path

from urbandata.assets import views


urlpatterns = [
    path("", views.AssetListView.as_view(), name="asset_list"),
    path("/<int:id>", views.AssetDetailView.as_view(), name="asset_detail"),
]
