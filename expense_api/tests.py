from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class ExpenseTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_expense(self):
        url = reverse("expense_api:expense-list-create")
        payload = {
            "amount": 60.0,
            "merchant": "Amazon",
            "description": "Django Rest Framework Book",
        }

        res = self.client.post(url, payload, format="json")
        json_resp = res.json()

        self.assertEqual(status.HTTP_201_CREATED, res.status_code)
        self.assertEqual(payload["amount"], json_resp["amount"])
        self.assertEqual(payload["merchant"], json_resp["merchant"])
        self.assertEqual(payload["description"], json_resp["description"])
        self.assertIsInstance(json_resp["id"], int)
