from django.conf.urls import url
from map import views

urlpatterns = [
    url(r'^$', views.MapView.as_view(), name='map-view'),
]
