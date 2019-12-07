from django.views import View
from django.http import JsonResponse
from apps.configs.models import Application, Configuration, Setting


class ConfigView(View):

    def get(self, request, app_uuid, env):

        application = Application.objects.filter(app_id=app_uuid, active=True)
        if not application.exists():
            return JsonResponse(data={}, status=404)

        configurations = Configuration.objects.filter(
            application_id=application.first().pk,
            active=True,
            environment__name=str(env)
        )

        if not configurations.exists():
            return JsonResponse(data={}, status=404)

        settings = Setting.objects.filter(
            configuration_id=configurations.first().id
        )
        data = [
            {"key": d.key, "value": d.value} for d in settings
        ]

        return JsonResponse(data=data, safe=False, status=200)
