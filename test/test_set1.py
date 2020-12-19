
import sys
import os
# to import the app.py file we need to specify the path
# the following three line of code does that for us
this_dir = os.path.dirname(os.path.abspath(__file__)) + '/'
main_dir = this_dir + '../'

sys.path.insert(1, main_dir)

from app import app
from numpy.testing import assert_allclose, assert_raises, assert_raises_regex
from numpy.testing import assert_almost_equal, assert_equal, assert_string_equal
import numpy as np
import unittest
from flask import jsonify
import json

class Tests(unittest.TestCase):
    """
        Using setUp method of unittest.TestCase
        Setting up a configuration options  
    """
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.tester = app.test_client()


    # Ensure that flask was set up correctly
    def test_page_test(self):
        response = self.tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    # Ensure that flask was set up correctly
    def test_page_test_loads(self):
        response = self.tester.get('/', content_type='html/text')

        self.assertTrue(b'Hello world! 3' in response.data)


    # Ensure that demo_page loads with GET request
    def test_demo_page(self):
        response = self.tester.get('/demo1', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    # Ensure that demo_page loads with valid response for GET request.
    def test_demo_page_loads(self):
        response = self.tester.get('/demo1', content_type='html/text')
        self.assertTrue(b'Creative Recommendation Engine' in response.data)


    # Ensure that demo_page loads with POST request

    def test_demo_page_post(self):
        response = self.tester.post('/demo1', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that demo_page loads with valid response for POST request.
    def test_demo_page_loads_post(self):
        response = self.tester.post('/demo1', content_type='html/text')
        self.assertTrue(b'Creative Recommendation Engine' in response.data)

    # Ensure that make_recommendation loads data correctly
    """
    GIVEN a form data with region and season specified model
    WHEN a post request is sent to /recommend_sort_games endpoint
    THEN check if it hit the endpoint and returns withou error
    """
    def test_make_recomendation(self):
        response = self.tester.post('/recommend_sort_games',data=json.dumps({'region': ['Americas'], 'season': ['Summer']},separators=(',', ':')))
        self.assertEqual(response.status, "200 OK")

    # Ensure that get_engine_output loads data correctly
    def test_get_engine_output(self):
        response = self.tester.get('/get_data_dump')
        self.assertEqual(response.status, "200 OK")


    def test_get_feature_output(self):
        response = self.tester.get('/get_feature_dump')
        self.assertEqual(response.status, '200 OK')

if __name__ == "__main__":
    unittest.main()
