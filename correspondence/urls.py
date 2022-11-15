from django.urls import path, include
from rest_framework import routers
from .views import SpecialChatViewSet, GroupChat

router = routers.DefaultRouter()
router.register(r'chat', SpecialChatViewSet)
router.register(r'groupchat', GroupChat)


urlpatterns = [
    path('', include(router.urls))
]
