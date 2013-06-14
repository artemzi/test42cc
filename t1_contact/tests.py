from django.test import TestCase
from django.conf import settings
 
from .models import Update
 
from t3_httprequests.models import HttpRequestLogEntry

class HomePersonTestCase(TestCase):
    
    def test_index_content(self):
        """
        Tests that data exists in the view.
        """
        response = self.client.get('/')
        field_names_in_view = [
                "Contacts",
                "Email",
                "Jabber",
                "Skype",
                "Other Contacts",
                ]
        data_in_view = [
                "Artem",
                "Zinoviev",
                "1983",
                "gmail.com",
                "zinovievartem",
                "mobile"
                ]

                
class SignalsTestCase(TestCase):
    
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