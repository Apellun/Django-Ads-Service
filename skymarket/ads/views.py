from rest_framework import pagination, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from ads.filters import AdFilter
from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, AdCreateSerializer, CommentSerializer, CommentCreateSerializer
from ads.permissions import AdsPermission, CommentsPermission


class AdPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter
    permission_classes = [AdsPermission]
    pagination_class = AdPagination
    queryset = Ad.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AdSerializer
        if self.action == 'create':
            return AdCreateSerializer
        return AdDetailSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [CommentsPermission]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CommentCreateSerializer
        return CommentSerializer