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

        entity = Ad()

        if 'title' not in data.keys():
            return Response("Title can't be empty")
        entity.title = data['title']

        if 'price' not in data.keys():
            return Response("Price can't be empty")

        try:
            entity.price = float(data['price'])
        except:
            return Response("Price should be a number")

        if 'description' in data.keys():
            entity.description = data['description']

        if 'image' in data.keys():
            entity.image = request.FILES['image']

        entity.author = User.objects.get(id=request.user.id)

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

        entity = Comment()

        if 'text' not in data.keys():
            return Response("Comment can't be empty")
        entity.text = data['text']

        entity.author = User.objects.get(id=request.user.id)

        if not request.query_params["ad"]:
            return Response ('Ad is not specified')
        
        ad_id = request.query_params["ad"]
        
        entity.ad = get_object_or_404(Ad, id=ad_id)

        entity.is_valid()
        entity.save()

        headers = mixins.CreateModelMixin.get_success_headers(self, data=data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)