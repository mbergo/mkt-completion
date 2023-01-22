import os
import json
from unittest import TestCase
from flask import Flask
from flask_testing import TestCase as FlaskTestCase
from your_app import app

class TestApp(FlaskTestCase):
    def create_app(self):
        return app

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Enter a text to complete:", response.data)
    
    def test_post_text(self):
        response = self.client.post("/", data=dict(text="Hello, I'm interested in "))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello, I'm interested in buying your product", response.data)

