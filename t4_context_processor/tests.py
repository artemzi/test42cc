from django.test import TestCase


class ContextProcessorTestCase(TestCase):
    
    def test_title_content(self):
        """
        Tests that page have title "42cc",
        title takes from setting.py file (BASE_TEMPLATE_TITLE = '42cc')
        if context_processor not work`s title don`t have "42cc"
        """
        
        response = self.client.get('/requests/')
        data_in_view = ["42cc"]