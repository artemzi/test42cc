from django.views.generic import UpdateView

from braces.views import LoginRequiredMixin, CsrfExemptMixin

from t1_contact.models import Person


class UpdatePersonView(LoginRequiredMixin, CsrfExemptMixin, UpdateView):
    """
    You must login to see template edit_person

    """
    model = Person
    template_name = "t5_editform/editform.html"