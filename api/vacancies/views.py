from rest_framework import mixins, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.permissions import IsSuperUser
from vacancies.filters import VacancyFilter
from vacancies.models import Vacancy
from vacancies.serializers import VacancySerializer, ApplicationsSerializer
from rest_framework.decorators import action


class VacancyViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [IsSuperUser]
    filter_backends = [VacancyFilter]

    def get_serializer_class(self):
        if self.action == "applications":
            return ApplicationsSerializer
        return VacancySerializer

    @action(detail=True, methods=["GET"])
    def applications(self, request, *args, **kwargs):
        try:
            instance = Vacancy.objects.get(pk=kwargs.get("pk"))
            serializer = self.get_serializer(instance.applications.all(), many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Vacancy.DoesNotExist as e:
            raise NotFound(e)
