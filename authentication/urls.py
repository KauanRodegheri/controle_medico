from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(), name='token_createview'),
    path('refresh/token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('verify/token/', TokenVerifyView.as_view(), name='verify_view')
]