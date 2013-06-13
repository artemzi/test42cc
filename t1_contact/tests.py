from django.test import TestCase
from django.conf import settings
 
from .models import Update
 
from t3_httprequests.models import HttpRequestLog


class SignalsTestCase(TestCase):
    
    def test_http_request_log_entry_create(self):
        self.client.get('/')
        updates = Update.objects.filter(model_name='HttpRequestLog').filter(update_type='C')
        self.assertTrue(len(updates) > 0)


    def test_http_request_log_entry_delete(self):
        self.client.get('/')
        r = HttpRequestLog.objects.all()[0]
        r.delete()
        updates = Update.objects.filter(model_name='HttpRequestLog').filter(update_type='D')
        self.assertTrue(len(updates) > 0)