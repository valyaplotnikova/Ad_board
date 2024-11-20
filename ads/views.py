from django_filters import OrderingFilter

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from ads.models import Ad, Review
from ads.pagination import AdPagination
from ads.serializers import AdSerializer, ReviewSerializer
from users.permissions import IsAuthor, IsAdmin


class AdListAPIView(ListAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filter_backends = [OrderingFilter]
    search_fields = ['title']
    permission_classes = (AllowAny,)


class AdCreateAPIView(CreateAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = (IsAuthenticated, IsAdmin | IsAuthor)


class AdRetrieveAPIView(RetrieveAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = (IsAuthenticated, IsAdmin | IsAuthor)


class AdUpdateAPIView(UpdateAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = (IsAuthenticated, IsAdmin | IsAuthor)


class AdDestroyAPIView(DestroyAPIView):
    queryset = Ad.objects.all()
    permission_classes = (IsAuthenticated, IsAdmin | IsAuthor)


class ReviewListAPIView(ListAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated, IsAdmin | IsAuthor)


class ReviewCreateAPIView(CreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated, IsAdmin | IsAuthor)


class ReviewRetrieveAPIView(RetrieveAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated, IsAdmin | IsAuthor)


class ReviewUpdateAPIView(UpdateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated, IsAdmin | IsAuthor)


class ReviewDestroyAPIView(DestroyAPIView):
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated, IsAdmin | IsAuthor)
