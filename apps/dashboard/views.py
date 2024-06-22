from django.template.response import TemplateResponse
from django.utils import timezone


def dashboard(request):
    return TemplateResponse(request, "dashboard.html")


def refresh(request):
    context = {
        "now": timezone.now(),
    }
    return TemplateResponse(request, "refresh.html", context)
