from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from users.models import TelegramUser, TelegramState
from users.permissions import IsSuperUser
from users.serializers import TelegramUserSerializer, TelegramStateSerializer


class TelegramUserViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer
    permission_classes = [IsSuperUser]


class TelegramStateViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    queryset = TelegramState.objects.all()
    serializer_class = TelegramStateSerializer
    permission_classes = [IsSuperUser]

