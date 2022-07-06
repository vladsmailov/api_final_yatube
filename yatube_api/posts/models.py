"""Models for posts."""
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint, CheckConstraint, F, Q

User = get_user_model()


class Group(models.Model):
    """Group model definition."""

    title = models.CharField(
        max_length=200,
        verbose_name="Название",
        help_text="Укажите название группы",
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Группы")
    description = models.TextField(
        verbose_name="Описание группы",
        help_text="Напишите описание группы"
    )

    def __str__(self):
        """__str__ method for Group."""
        return self.title


class Post(models.Model):
    """Post model definition."""

    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="posts",
    )
    image = models.ImageField(
        "Картинка",
        upload_to="posts/",
        blank=True,
        null=True
    )

    class Meta:
        """Meta for Post."""

        ordering = ("pub_date",)

    def __str__(self):
        """__str__ for Post."""
        return self.text[:15]


class Comment(models.Model):
    """Comment model definition."""

    post = models.ForeignKey(
        Post,
        null=False,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    text = models.TextField(
        verbose_name="Текст",
        help_text="Текст нового комментария"
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta for Comment."""

        ordering = ("-created",)

    def __str__(self):
        """__str__ for Comment."""
        return self.text


class Follow(models.Model):
    """Follow model definition."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="followings",
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="followers"
    )

    class Meta:
        """Meta for Follow model."""

        constraints = [
            UniqueConstraint(fields=["user", "following"],
                             name="unique_relationships"),
            CheckConstraint(check=~Q(user=F("following")),
                            name="prevent_self_follow"),
        ]
