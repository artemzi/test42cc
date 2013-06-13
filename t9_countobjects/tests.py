from django.test import TestCase
from django.core.management import call_command
from StringIO import StringIO


class CountModelsTest(TestCase):
    def test_can_call_countmodels(self):
        """
        Tests that countmodels command can be called.
        """
        # http://www.soyoucode.com/2011/capture-output-django-command
        content = StringIO()
        call_command("countmodels", stdout=content, stderr=content)