from django.urls import path, include
from accounts.views import ChangePasswordView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password_reset/', include('django_rest_passwordreset.urls')),
    path('api-token-auth/', obtain_jwt_token, name="obtain-jwt-token"),
]
