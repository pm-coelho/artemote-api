from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="artfeelz API",
        default_version="v1",
        description="This is the core BE API for the artfeelz project",
    ),
    public=True,
    permission_classes=[permissions.IsAuthenticated],
)
