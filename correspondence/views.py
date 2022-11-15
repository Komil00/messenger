from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Correspondence, CustomUser, GroupCorrespondence, Group
from .serialzers import ChatListSerializers, ChatPostSerializers, GroupCorrespondenceListSerializers, \
    GroupCorrespondencePostSerializers, GroupUserPutSerializers


class SpecialChatViewSet(ModelViewSet):
    queryset = Correspondence.objects.order_by('-send_data')
    serializer_class = ChatListSerializers
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['list']:
            return ChatListSerializers
        return ChatPostSerializers

    def get_queryset(self):
        return self.queryset.filter(Q(from_author=self.request.user) | Q(to_author=self.request.user))


#

class GroupChat(ModelViewSet):
    queryset = GroupCorrespondence.objects.all()
    serializer_class = GroupCorrespondenceListSerializers
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action in ['list']:
            return GroupCorrespondenceListSerializers
        return GroupCorrespondencePostSerializers

    def get_queryset(self):
        return self.queryset.filter(Q(group__groupuser=self.request.user))

    def update(self, request, pk=None, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        user = request.user
        if instance.from_user == user:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            return Response('error: sizga ruxsat yoq', status=status.HTTP_403_FORBIDDEN)
