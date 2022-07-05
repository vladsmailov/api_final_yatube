"""Urls for api app."""

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from django.urls import include, path

from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet
from posts.models import Follow


router = DefaultRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)
router.register('follow', FollowViewSet, basename=Follow)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
