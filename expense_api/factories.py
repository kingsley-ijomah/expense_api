import random

import factory

from . import models


class ExpenseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Expense

    amount = round(random.uniform(5.0, 95.5), 2)
    merchant = factory.Faker("company")
    description = factory.Faker("paragraph")
