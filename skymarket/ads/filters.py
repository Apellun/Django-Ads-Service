import django_filters
from ads.models import Ad


class AdFilter(django_filters.rest_framework.FilterSet):
    """
    Shows only ads that contain query text in
    their title or description.
    """
    title = django_filters.CharFilter(lookup_expr="icontains")
    
    class Meta:
        model = Ad
        fields = ["title"]