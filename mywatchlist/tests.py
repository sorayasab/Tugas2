from django.test import TestCase
from django.test import Client
import sys

class testing(TestCase):
    def test_json(self):
        response = self.client.get("/mywatchlist/json/",{}, True)
        sys.stderr.write(repr(response) + '\n')
        self.assertEqual(response.status_code, 200)
    
    def test_xml(self):
        response = self.client.get("/mywatchlist/xml",{}, True)
        sys.stderr.write(repr(response) + '\n')
        self.assertEqual(response.status_code, 200)
        
    def test_html(self):
        response = self.client.get("/mywatchlist/html/",{}, True)
        sys.stderr.write(repr(response) + '\n')
        self.assertEqual(response.status_code, 200)
    