from rest_framework import serializers
from rest_api.models import Expense
from rest_framework.reverse import reverse as api_reverse


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            'id',
            'expense_pk',
            'expense_type',
            'reason',
            'amount',
            'timestamp',
            'session_id',
            'user',
            'backup_date',
        ]
        
        read_only_fields = ['user']

    # def validate(self, data):
    #     expense_pk = data.get("expense_pk", None)
    #     if expense_pk == "":
    #         expense_pk = None
    #     expense_type = data.get("expense_type", None)
    #     if expense_pk is None and expense_type is None:
    #         raise serializers.ValidationError("expense_pk or expense_type is required.")
    #     return data
        
