from django.test import TestCase
from django.core.management import call_command
from StringIO import StringIO


class T9CountObjectsTest(TestCase):
    def test_can_call_countobjects(self):
        """
        Tests that countobjects command can be called.
        """
        # http://www.soyoucode.com/2011/capture-output-django-command
        content = StringIO()
        call_command("countobjects", stdout=content, stderr=content)