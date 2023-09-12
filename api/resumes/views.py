from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from resumes.models import Resume
from resumes.serializers import ResumeSerializer
from users.permissions import IsSuperUser


class ResumeViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()
    permission_classes = [IsSuperUser]
