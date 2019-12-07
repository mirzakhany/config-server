from django.urls import path
from apps.configs.views import ConfigView

urlpatterns = [
    path('<uuid:app_uuid>/<str:env>/', ConfigView.as_view(), name="config_view"),
]
