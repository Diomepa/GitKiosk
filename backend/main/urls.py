from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("api/v1/", include("core.urls")),
    # obtain token endpoint
    path("api/v1/get-token", obtain_auth_token, name="get-token"),
    # Swagger docs
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/v1/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("", lambda request: redirect("swagger-ui")),
]
