from django.test import TestCase

from .models import HttpRequestLogEntry
 
 
class HttpRequestLogEntryTest(TestCase):

    def test_request_has_default_priority(self):
        pass