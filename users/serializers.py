from rest_framework import serializers
from users.models import TelegramUser, TelegramState


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = "__all__"


class TelegramStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramState
        fields = "__all__"
