from django.urls import path
from djoser.views import UserViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserAdViewSet

app_name = UsersConfig.name

router = routers.DefaultRouter()
router.register(r'', UserAdViewSet, basename='users')

urlpatterns = [
                  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('reset_password/', UserViewSet.reset_password, name='reset_password'),
                  path('reset_password_confirm/', UserViewSet.reset_password_confirm, name='reset_password_confirm')
] + router.urls
