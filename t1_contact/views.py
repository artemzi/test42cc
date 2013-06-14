from django.views.generic import DetailView

from .models import CustomProfile


class HomePersonListView(DetailView):
    model = CustomProfile
    queryset = CustomProfile.objects.order_by('-first_name').all()
    template_name = "test42cc/index.html"
    context_object_name = "CustomProfile"


    def get_context_data(self, **kwargs):
        context = super(HomePersonListView, self).get_context_data(**kwargs)
        context['pk'] = CustomProfile.objects.get(pk=1)
        return context
