from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from professions.serializers import ProfessionAreaSerializer, ProfessionSerializer
from professions.models import ProfessionArea, Profession
from users.permissions import IsSuperUser


class ProfessionAreaViewSet(
    mixins.ListModelMixin,
    GenericViewSet
):
    serializer_class = ProfessionAreaSerializer
    queryset = ProfessionArea.objects.all()
    permission_classes = [IsSuperUser]


class ProfessionViewSet(
    mixins.ListModelMixin,
    GenericViewSet
):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()
    permission_classes = [IsSuperUser]
