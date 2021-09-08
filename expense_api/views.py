from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Expense
from .serializers import ExpenseSerializer


class ExpenseListCreateView(APIView):
    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ExpenseRetrieveUpdateDestroyView(APIView):
    def get(self, request, pk):
        expense = get_object_or_404(Expense, pk=pk)
        serializer = ExpenseSerializer(expense, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        expense = get_object_or_404(Expense, id=pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        expense = get_object_or_404(Expense, id=pk)
        serializer = ExpenseSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

