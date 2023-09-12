from rest_framework.exceptions import ValidationError
from rest_framework.filters import BaseFilterBackend


class VacancyFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        profession_id = request.query_params.get('profession_id')
        if not profession_id and view.action == 'list':
            raise ValidationError("Invalid request! It must have a profession_id in query params.")
        return queryset
