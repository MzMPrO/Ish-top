from rest_framework import serializers
from professions.models import ProfessionArea, Profession


class ProfessionAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionArea
        fields = "__all__"


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"
