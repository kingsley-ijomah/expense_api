import random

from django.contrib.auth.models import User

import factory

from . import models


class ExpenseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Expense

    amount = round(random.uniform(5.0, 95.5), 2)
    merchant = factory.Faker("company")
    description = factory.Faker("paragraph")


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.Faker("word")
    email = factory.Faker("email")
    is_active = True
    password = factory.PostGenerationMethodCall("set_password", "password123")
