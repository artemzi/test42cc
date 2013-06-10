from django.views.generic import UpdateView
from django.http import HttpResponseRedirect
from braces.views import LoginRequiredMixin, CsrfExemptMixin

from t1_contact.models import CustomProfile
from t5_editform.form import EditForm


class CustomProfileUpdateView(LoginRequiredMixin, CsrfExemptMixin, UpdateView):
    """
    You must login to see template edit_person

    """
    model = CustomProfile
    form = EditForm
    template_name = "t5_editform/editform.html"
    success_url = '/'
    