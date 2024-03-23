from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Video
from .serializers import VideoSerializer


class StandardResultsSetPagination(PageNumberPagination):
    """
    Pagination class for the Video API.
    """
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class VideoViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Video model.

    Provides CRUD operations for the Video model through a RESTful API.
    Supports pagination, filtering, and sorting.
    """
    queryset = Video.objects.order_by("-published_at")
    serializer_class = VideoSerializer
    pagination_class = StandardResultsSetPagination
