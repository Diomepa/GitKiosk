from rest_framework import filters
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from core import models, serializers
from core.permissions import IsReadOnlyOrOwner


class ProjectEntryPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"


class ProjectEntryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsReadOnlyOrOwner]
    pagination_class = ProjectEntryPagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)

    serializer_class = serializers.ProjectEntrySerializer
    queryset = models.ProjectEntry.objects.select_related("owner").all()
