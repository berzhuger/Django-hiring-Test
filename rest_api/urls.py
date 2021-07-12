from django.urls import path
from rest_api.views import LocationList, LocationDetail

app_name = 'rest_api'

urlpatterns = [
    path('weather/', LocationList.as_view(), name='weather'),
    path('weather/<int:pk>', LocationDetail.as_view(), name='weather_detail'),
]
