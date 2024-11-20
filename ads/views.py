from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from ads.models import Ad
from ads.pagination import AdPagination
from ads.serializers import AdSerializer


class AdListAPIView(ListAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    pagination_class = AdPagination


class AdCreateAPIView(CreateAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()


class AdRetrieveAPIView(RetrieveAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()


class AdUpdateAPIView(UpdateAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()


class AdDestroyAPIView(DestroyAPIView):
    queryset = Ad.objects.all()
