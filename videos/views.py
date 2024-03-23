from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Video
from .serializers import VideoSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.order_by('-published_at')
    serializer_class = VideoSerializer
    pagination_class = StandardResultsSetPagination