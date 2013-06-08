from django.views.generic import ListView

from .models import Person


class HomePersonListView(ListView):
    queryset = Person.objects.order_by('-first_name').all()
    template_name = "test42cc/index.html"
    context_object_name = "person"