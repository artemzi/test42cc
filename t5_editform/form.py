from django import forms

from t1_contact.models import CustomProfile


class EditForm(forms.ModelForm):
    class Meta(object):
        model = CustomProfile