from django.urls import path

from ads.apps import AdsConfig
from ads.views import AdListAPIView, AdCreateAPIView, AdRetrieveAPIView, AdUpdateAPIView, AdDestroyAPIView, \
    ReviewListAPIView, ReviewCreateAPIView, ReviewRetrieveAPIView, ReviewUpdateAPIView, ReviewDestroyAPIView

app_name = AdsConfig.name

urlpatterns = [
    path('ads/', AdListAPIView.as_view(), name='ad_list'),
    path('ads/create/', AdCreateAPIView.as_view(), name='ad_create'),
    path('ads/get/<int:pk>/', AdRetrieveAPIView.as_view(), name='ad_get'),
    path('ads/update/<int:pk>/', AdUpdateAPIView.as_view(), name='ad_update'),
    path('ads/delete/<int:pk>/', AdDestroyAPIView.as_view(), name='ad_delete'),
    path('review/', ReviewListAPIView.as_view(), name='review_list'),
    path('review/create/', ReviewCreateAPIView.as_view(), name='review_create'),
    path('review/get/<int:pk>/', ReviewRetrieveAPIView.as_view(), name='review_get'),
    path('review/update/<int:pk>/', ReviewUpdateAPIView.as_view(), name='review_update'),
    path('review/delete/<int:pk>/', ReviewDestroyAPIView.as_view(), name='review_delete'),
]
