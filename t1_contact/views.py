from django.views.generic import ListView

from .models import CustomProfile


class HomePersonListView(ListView):
    queryset = CustomProfile.objects.order_by('-first_name').all()
    template_name = "test42cc/index.html"
    context_object_name = "CustomProfile"