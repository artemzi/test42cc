from django import forms

from t1_contact.models import Person


class EditForm(forms.ModelForm):
    first_name = forms.CharField(label='Name', max_length=50)
    last_name = forms.CharField(label='Last name', max_length=50)
    birth_date = forms.DateField(label='Date of birth')
    bio = forms.CharField(label='Bio', widget=forms.Textarea, max_length=10000)
    email = forms.EmailField(label='Email')
    jabber = forms.EmailField(label='Jabber ID')
    skype = forms.CharField(label='Skype ID', max_length=50)
    photo = forms.ImageField(label="Photo")
    other_contacts = forms.CharField(label='Other contacts',widget=forms.Textarea, max_length=10000)

    class Meta(object):
        model = Person