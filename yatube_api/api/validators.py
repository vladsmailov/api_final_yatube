"""Validators for api."""
from rest_framework import serializers


class FollowValidator:
    """FollowSerializer validator."""

    def __init__(self, user='user', following='following'):
        """__init__ for FollowValidator."""
        self.user = user
        self.following = following

    def __call__(self, values):
        """Values validation."""
        if values[self.user] == values[self.following]:
            raise serializers.ValidationError('Self-following error!')
