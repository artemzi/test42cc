from django import forms

from t1_contact.models import CustomProfile


class EditForm(forms.ModelForm):
    class Meta(object):
        model = CustomProfile

    def __init__(self, *args, **kwargs):
        super (EditForm, self).__init__(*args, **kwargs)
        self.fields['estate'].queryset = EditForm.objects.filter(estate__user__exact=Estates.objects.get(self._user))