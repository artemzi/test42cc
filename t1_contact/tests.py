from django.test import TestCase
from django.conf import settings
 
from .models import CustomProfile, Update
 
from t3_httprequests.models import HttpRequestLogEntry


class SignalsTestCase(TestCase):
    
    def test_custom_profile_update(self):
        profile = CustomProfile.objects.get(pk=1)
        profile.first_name = "New Name"
        profile.save()
        updates = Update.objects.filter(update_type='U').filter(model_name='CustomProfile')
        self.assertTrue(len(updates) > 0)


    def test_custom_profile_delete(self):
        person = CustomProfile.objects.get(pk=1)
        person.delete()
        updates = Update.objects.filter(update_type='D').filter(model_name='CustomProfile')
        self.assertTrue(len(updates) > 0)


    def test_http_request_log_entry_create(self):
        self.client.get('/')
        updates = Update.objects.filter(model_name='HttpRequestLogEntry').filter(update_type='C')
        self.assertTrue(len(updates) > 0)


    def test_http_request_log_entry_delete(self):
        self.client.get('/')
        r = HttpRequestLogEntry.objects.all()[0]
        r.delete()
        updates = Update.objects.filter(model_name='HttpRequestLogEntry').filter(update_type='D')
        self.assertTrue(len(updates) > 0)