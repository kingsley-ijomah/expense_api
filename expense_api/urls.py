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
    path(
        "registrations/",
        views.RegistrationCreateView.as_view(),
        name="registration-create",
    ),
    path("sessions/", views.SessionCreateView.as_view(), name="session-create"),
    path(
        "session/",
        views.SessionRetrieveDestroyView.as_view(),
        name="session-retrieve-destroy",
    ),
]
