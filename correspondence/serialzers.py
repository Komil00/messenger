from rest_framework.serializers import ModelSerializer

from customusers.models import CustomUser
from .models import Correspondence, GroupCorrespondence, Group


class AuthorSerialiszer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username']


class ChatListSerializers(ModelSerializer):
    from_author = AuthorSerialiszer()
    to_author = AuthorSerialiszer()

    class Meta:
        model = Correspondence
        fields = '__all__'


class ChatPostSerializers(ModelSerializer):
    class Meta:
        model = Correspondence
        fields = '__all__'


class GroupListSerializers(ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class GroupCorrespondenceListSerializers(ModelSerializer):
    from_user = AuthorSerialiszer()
    group = GroupListSerializers()

    class Meta:
        model = GroupCorrespondence
        fields = '__all__'


class GroupCorrespondencePostSerializers(ModelSerializer):
    class Meta:
        model = GroupCorrespondence
        fields = '__all__'


class GroupUserPutSerializers(ModelSerializer):
    class Meta:
        model = GroupCorrespondence
        fields = '__all__'
