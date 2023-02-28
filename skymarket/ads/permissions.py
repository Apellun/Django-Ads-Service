from rest_framework import permissions
from django.http import Http404

from ads.models import Ad, Comment


class AdsPermission(permissions.BasePermission):
    """
    Allows anyone to view ads, allows users to create,
    delete and change their ads. Allows admins create their ads,
    delete and change all ads.
    """
    message = 'You can only manage your own ads'
    def has_permission(self, request, view) -> bool:
        if view.action not in ('list', 'retrieve'):
            if view.action in ('update', 'partial_update', 'destroy'):
                try:
                    entity = Ad.objects.get(pk=view.kwargs["pk"])
                except Ad.DoesNotExist:
                    raise Http404

                if request.user.is_staff or entity.author.id == request.user.id:
                    return True
                return False
            
            else:
                return request.user.is_authenticated
        
        return True



class CommentsPermission(permissions.BasePermission):
    message = 'You can only manage your own comments'

    def has_permission(self, request, view):
        """
        Allows users to view all comments.
        Allows users to create, delete and change their comments.
        Allows admins create comments, delete and change all comments.
        """
        if view.action in ['update', 'partial_update', 'destroy']:
            try:
                entity = Ad.objects.get(pk=view.kwargs["pk"])
            except Ad.DoesNotExist:
                raise Http404

            if entity.author.id == request.user.id or request.user.is_staff:
                return True
            return False

        return request.user.is_authenticated