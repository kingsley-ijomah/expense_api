from django.urls import path

from . import views

urlpatterns = [
    path(
        "expenses/", views.ExpenseListCreateView.as_view(), name="expense-list-create"
    ),
    path(
        "expenses/<str:pk>",
        views.ExpenseRetrieveUpdateDestroyView.as_view(),
        name="expense-retrieve-update-destroy",
    ),
]
