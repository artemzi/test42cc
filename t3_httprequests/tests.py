from django.test import TestCase
 
from t3_httprequests.models import HttpRequestLog
 
class HttpRequestLogEntryTest(TestCase):

    def test_request_is_saved(self):
        self.client.get('/')
        self.assertTrue(len(HttpRequestLog.objects.all()) > 0)

    def test_no_more_than_ten(self):
        number_of_requests = 11
        for i in range(number_of_requests):
            response = self.client.get('/requests/')
        # each request is in <tr> in template, first tr is thead
        self.assertTrue(response.content.count('<tr>') < 12)
