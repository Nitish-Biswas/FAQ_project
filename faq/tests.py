# faq/tests/test_models.py
import pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from faq.models import FAQ

class TestFAQModel(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is this service?",
            answer="This is a test FAQ service."
        )
        self.client = APIClient()

    def test_faq_creation(self):
        self.assertTrue(isinstance(self.faq, FAQ))
        self.assertEqual(self.faq.__str__(), "What is this service?")

    def test_translation_fields(self):
        # Test automatic translation generation
        self.assertIsNotNone(self.faq.question_hi)
        self.assertIsNotNone(self.faq.question_bn)

    def test_get_translated_field(self):
        # Test translation retrieval
        hindi_question = self.faq.get_translated_field('question', 'hi')
        self.assertIsNotNone(hindi_question)
        self.assertNotEqual(hindi_question, self.faq.question)

class TestFAQAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.faq = FAQ.objects.create(
            question="API Test Question",
            answer="API Test Answer"
        )

    def test_list_faqs(self):
        response = self.client.get(reverse('faq-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

    def test_get_faq_with_language(self):
        response = self.client.get(f"{reverse('faq-list')}?lang=hi")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

# conftest.py
import pytest
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()