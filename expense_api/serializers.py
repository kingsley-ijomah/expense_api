from rest_framework import serializers

from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    amount = serializers.FloatField(required=True)
    merchant = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Expense
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
