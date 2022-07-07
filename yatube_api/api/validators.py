"""Validators for api."""
from rest_framework import serializers


class UniqueValueValidator:
    """UniqueValue validator."""

    def __init__(self, *fields):
        """Keys for values dict."""
        self.fields = fields

    def __call__(self, values):
        """Values validation."""
        for first_key in self.fields:
            for second_key in self.fields:
                if (
                    first_key != second_key
                    and values[first_key] == values[second_key]
                ):
                    raise serializers.ValidationError('Self-following error!')
