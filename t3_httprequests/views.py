from django.views.generic import ListView

from .models import HttpRequestLogEntry


class HttpRequestListView(ListView):
    model = HttpRequestLogEntry
    queryset = model.objects.all().order_by('-date')[:10]
    template_name = "test42cc/request.html"
    context_object_name = "http"