"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class EditFormTest(TestCase):
    def test_that_login_exists(self):
        """
        when you try go to editpage.html in response 
        you have login form
        """
        response = self.client.get('/update/1')
        field_names_in_view = ["Username", "Password"]
