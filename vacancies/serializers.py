from rest_framework import serializers
from vacancies.models import Vacancy, Application


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = "__all__"


class ApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"
