from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from .views import PlacesViewSet

app_name = 'API'
router = DefaultRouter()
router.register('places', PlacesViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]