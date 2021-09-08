from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_api_key.models import APIKey

from .factories import ExpenseFactory
from .models import Expense


class ExpenseTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        api_key, key = APIKey.objects.create_key(name="expense-service")
        self.client.credentials(HTTP_AUTHORIZATION=f"Api-Key {key}")

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

    def test_list_expenses(self):
        expense = ExpenseFactory()

        url = reverse("expense_api:expense-list-create")
        res = self.client.get(url, format="json")

        json_resp = res.json()

        self.assertEqual(status.HTTP_200_OK, res.status_code)
        self.assertEqual(expense.amount, json_resp[0]["amount"])
        self.assertEqual(expense.merchant, json_resp[0]["merchant"])
        self.assertEqual(expense.description, json_resp[0]["description"])

    def test_retrieve_expense(self):
        expense = ExpenseFactory()

        url = reverse("expense_api:expense-retrieve-update-destroy", args=[expense.id])

        res = self.client.get(url, format="json")
        json_resp = res.json()

        self.assertEqual(status.HTTP_200_OK, res.status_code)
        self.assertEqual(expense.amount, json_resp["amount"])
        self.assertEqual(expense.merchant, json_resp["merchant"])
        self.assertEqual(expense.description, json_resp["description"])

    def test_delete_expense(self):
        expense = ExpenseFactory()

        url = reverse("expense_api:expense-retrieve-update-destroy", args=[expense.id])

        res = self.client.delete(url, format="json")

        self.assertEqual(status.HTTP_204_NO_CONTENT, res.status_code)
        self.assertFalse(Expense.objects.filter(id=expense.id))

    def test_update_expense(self):
        expense = ExpenseFactory()

        url = reverse("expense_api:expense-retrieve-update-destroy", args=[expense.id])
        payload = {
            "amount": 60.0,
            "merchant": "Amazon",
            "description": "Django Rest Framework",
        }

        res = self.client.put(url, payload, format="json")

        updated_expense = Expense.objects.get(id=expense.id)

        self.assertEqual(status.HTTP_200_OK, res.status_code)
        self.assertEqual(updated_expense.amount, payload["amount"])
        self.assertEqual(updated_expense.merchant, payload["merchant"])
        self.assertEqual(updated_expense.description, payload["description"])

    def test_unsuccessful_expense_update(self):
        expense = ExpenseFactory()

        url = reverse("expense_api:expense-retrieve-update-destroy", args=[expense.id])
        payload = {}

        res = self.client.put(url, payload, format="json")
        json_resp = res.json()

        self.assertEqual(status.HTTP_400_BAD_REQUEST, res.status_code)
        self.assertEqual(json_resp["amount"], ["This field is required."])
        self.assertEqual(json_resp["merchant"], ["This field is required."])
