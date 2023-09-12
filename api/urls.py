from rest_framework.routers import DefaultRouter
from api.users.views import (
    TelegramUserViewSet,
    TelegramStateViewSet
)
from api.professions.views import (
    ProfessionAreaViewSet,
    ProfessionViewSet
)
from api.resumes.views import ResumeViewSet
from api.vacancies.views import VacancyViewSet


router = DefaultRouter()
router.register("telegram_users", TelegramUserViewSet, basename="telegram_users")
router.register("telegram_states", TelegramStateViewSet, basename="telegram_states")
router.register("profession_areas", ProfessionAreaViewSet, basename="profession_areas")
router.register("professions", ProfessionViewSet, basename="professions")
router.register("resumes", ResumeViewSet, basename="resumes")
router.register("vacancies", VacancyViewSet, basename="vacancies")

urlpatterns = router.urls
