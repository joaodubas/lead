"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from forms import ContactForm
from models import Contact


class ContactFormTest(TestCase):

    def test_simple_test_modelform(self):
        data = {
            "name": "test",
            "email": "test@test.com",
            "message": "Message test",
            "category": "OUT",
        }
        form = ContactForm(data)
        self.assertTrue(form.is_valid())

    def test_return_from_model(self):
        data = {
            "name": "test",
            "email": "test@test.com",
            "message": "Message test",
            "category": "OUT",
        }

        contact = Contact.objects.create(**data)
        self.assertEquals(data['name'], str(contact))
