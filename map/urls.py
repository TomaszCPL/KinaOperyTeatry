from django.conf.urls import url
from map.views import Map


app_name = 'map'

urlpatterns = [
    url(r'', Map.as_view(), name='map'),
]