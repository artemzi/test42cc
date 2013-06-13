from django.views.generic import ListView

from .models import HttpRequestLog


class HttpRequestListView(ListView):
    model = HttpRequestLog
    queryset = model.objects.all().order_by('-date')[:10]
    template_name = "t3_httprequests/httprequestlogentry_list.html"
    context_object_name = "http"