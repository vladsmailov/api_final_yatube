"""Serializers for api."""
from rest_framework import serializers

from posts.models import Comment, Group, Post, Follow, User
from rest_framework.validators import UniqueTogetherValidator
from .validators import UniqueValueValidator


class PostSerializer(serializers.ModelSerializer):
    """Serializer for Post."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        """Meta definition for PostSerializer."""

        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for Group."""

    class Meta:
        """Meta for GroupSerializer."""

        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for group."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        """Meta for CommentSerializer."""

        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    """Serializer for followings."""

    user = serializers.SlugRelatedField(
        slug_field='username',
        default=serializers.CurrentUserDefault(),
        read_only=True,
    )

    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    class Meta:
        """Meta for FollowSerializer."""

        model = Follow
        fields = '__all__'
        validators = [
            UniqueValueValidator('user', 'following'),
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following']
            ),
        ]
