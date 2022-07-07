"""Mixins for api."""
from rest_framework import viewsets
from rest_framework import mixins


class CreateListViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """Custom ViewSet based on Create-, List-, mixins."""

    pass
