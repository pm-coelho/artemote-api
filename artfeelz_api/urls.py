"""
URL configuration for artfeelz_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

from users.api.views import MeViewSet
from users.api.urls import users_router
from artworks.api.urls import artworks_router
from events.api.urls import events_router

from .redoc import schema_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "docs/redoc", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path("api/auth/token", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("api/auth/token/refresh", TokenRefreshView.as_view(), name="token-refresh"),
    path("api/auth/me", MeViewSet.as_view(), name="me"),
    path(r"api/", include(users_router.urls)),
    path(r"api/", include(artworks_router.urls)),
    path(r"api/", include(events_router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
