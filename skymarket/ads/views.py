from rest_framework import pagination, viewsets, status, mixins
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from ads.filters import AdFilter
from ads.models import Ad, Comment
from users.models import User
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
        """
        Returns a proper serializer depending on the view action.
        """
        if self.action == 'list':
            return AdSerializer
        if self.action == 'create':
            return AdCreateSerializer
        return AdDetailSerializer

    def create(self, request, *args, **kwargs):
        """
        Creates and AD with an automatically tied user instance.
        "Title" and "price" fields are required, other fields
        are optional.
        """ 
        data = request.data

        if 'title' not in data.keys():
            return Response("Title can't be empty", status=status.HTTP_400_BAD_REQUEST)
        elif 'price' not in data.keys():
            return Response("Price can't be empty", status=status.HTTP_400_BAD_REQUEST)
        elif not type(data['price']) in (float, int):
            return Response("Price should be a number", status=status.HTTP_400_BAD_REQUEST)

        entity = Ad()
        entity.title = data['title']
        entity.price = data['price']
        entity.author = User.objects.get(id=request.user.id)
        
        if 'description' in data.keys():
            entity.description = data['description']
        if 'image' in data.keys():
            entity.image = request.FILES['image']
            
        entity.is_valid()
        entity.save()

        headers = mixins.CreateModelMixin.get_success_headers(self, data=data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [CommentsPermission]
    
    def get_serializer_class(self):
        """
        Returns a proper serializer depending on the action.
        """
        if self.action == 'create':
            return CommentCreateSerializer
        return CommentSerializer

    def create(self, request, *args, **kwargs):      
        """
        Creates a comment with an automatically tied user instance.
        Also gets the ad's id from a query parameter.
        """ 
        data = request.data

        if 'text' not in data.keys():
            return Response("A comment can't be empty", status=status.HTTP_400_BAD_REQUEST)
        try:
            ad_id = request.query_params["ad"]
        except:
            return Response('Ad is not specified', status=status.HTTP_400_BAD_REQUEST)
        try:
            ad = Ad.objects.get(id=ad_id)
        except:
            return Response("Ad doesn't exist", status=status.HTTP_400_BAD_REQUEST)
        
        entity = Comment()
        entity.text = data['text']
        entity.author = User.objects.get(id=request.user.id)
        entity.ad = ad
        entity.is_valid()
        entity.save()

        headers = mixins.CreateModelMixin.get_success_headers(self, data=data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)