from rest_framework.routers import DefaultRouter
from core.views import ProjectEntryViewSet, ProjectEntryWebHookViewSet, testhook
from django.urls import path

router = DefaultRouter()
router.register(
    r"project-entries",
    viewset=ProjectEntryViewSet,
    basename="project-entry",
)
router.register(
    r"project-entry-web-hooks",
    viewset=ProjectEntryWebHookViewSet,
    basename="project-entry-web-hook",
)

urlpatterns = router.urls

urlpatterns += [path("testhook/", testhook)]
