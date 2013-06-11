from django import forms
from .widgets import AdvancedFileInput

from t1_contact.models import CustomProfile


class PhotoField(forms.ImageField):
    widget = AdvancedFileInput


class EditForm(forms.ModelForm):
    class Meta(object):
        model = CustomProfile
        photo = PhotoField(label=u"Photo")
        
    def __init__(self, *args, **kwargs):
        super (EditForm, self).__init__(*args, **kwargs)
        self.fields['estate'].queryset = EditForm.objects.filter(estate__user__exact=Estates.objects.get(self._user))