from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import SimpleRouter
from djoser.views import UserViewSet
from ads.views import AdViewSet, CommentViewSet
from users.views import ActivateUser

users_router = SimpleRouter()
users_router.register("api/users", UserViewSet, basename="users")
ads_router = SimpleRouter()
ads_router.register('api/ads', AdViewSet)
comments_router = SimpleRouter()
comments_router.register('api/comments', CommentViewSet)

urlpatterns = [
    path("api/admin", admin.site.urls),
    path('', include('djoser.urls.jwt')),
    path('api/schema', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/users/activation/<uid>/<token>', ActivateUser.as_view({'get': 'activation'})),
]

urlpatterns += users_router.urls
urlpatterns += ads_router.urls
urlpatterns += comments_router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)