import json
from django.http import HttpResponse
from django.views.generic import UpdateView
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
    success_url = '.'
    
    def form_valid(self, form):
        """
        If the request is ajax, save the form and return a json response.
        Otherwise return super as expected.
        """
        if self.request.is_ajax():
            self.object = form.save()
            return HttpResponse(json.dumps("success"),
                mimetype="application/json")
        return super(CustomProfileUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        """
        We haz errors in the form. If ajax, return them as json.
        Otherwise, proceed as normal.
        """
        if self.request.is_ajax():
            return HttpResponseBadRequest(json.dumps(form.errors),
                mimetype="application/json")
        return super(CustomProfileUpdateView, self).form_invalid(form)