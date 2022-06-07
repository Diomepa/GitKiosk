from rest_framework.routers import DefaultRouter
from core.views import ProjectEntryViewSet

router = DefaultRouter()
router.register(
    r"project-entries",
    viewset=ProjectEntryViewSet,
    basename="project-entry",
)

urlpatterns = router.urls
