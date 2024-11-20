from django.urls import path

from ads.apps import AdsConfig
from ads.views import AdListAPIView, AdCreateAPIView, AdRetrieveAPIView, AdUpdateAPIView, AdDestroyAPIView

app_name = AdsConfig.name

urlpatterns = [
    path('ads/', AdListAPIView.as_view(), name='ad_list'),
    path('ads/create/', AdCreateAPIView.as_view(), name='ad_create'),
    path('ads/get/<int:pk>/', AdRetrieveAPIView.as_view(), name='ad_get'),
    path('ads/update/<int:pk>/', AdUpdateAPIView.as_view(), name='ad_update'),
    path('ads/delete/<int:pk>/', AdDestroyAPIView.as_view(), name='ad_delete'),
]
