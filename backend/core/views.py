import datetime
import random
import time

from rest_framework import filters
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core import models, serializers
from core.permissions import IsReadOnlyOrOwner


class ProjectEntryPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"


class LinkEntryViewSet(viewsets.ModelViewSet):
    # Abstract
    permission_classes = [IsAuthenticated, IsReadOnlyOrOwner]
    pagination_class = ProjectEntryPagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    search_fields = ("name", "link")


class ProjectEntryViewSet(LinkEntryViewSet):
    serializer_class = serializers.ProjectEntrySerializer
    queryset = models.ProjectEntry.objects.select_related("owner").all()


class ProjectEntryWebHookViewSet(LinkEntryViewSet):
    serializer_class = serializers.ProjectEntryWebHookSerializer
    queryset = models.ProjectEntryWebHook.objects.select_related("owner").all()


@api_view(["POST"])
def testhook(request):
    r = random.randint(1, 5)
    time.sleep(r)
    return Response(
        {
            "message": f" {datetime.datetime.now()}: Got some data! Waited for {r}  seconds",
            "data": request.data,
        }
    )
