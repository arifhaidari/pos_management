from rest_framework import serializers
from rest_api.models import Invoice
from rest_framework.reverse import reverse as api_reverse


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = [
            'id',
            'invoice_pk',
            'invoice_subtotal',
            'invoice_discount',
            'invoice_paid_amount',
            'invoice_payable_amount',
            'invoice_item_no',
            'customer_name',
            'customer_address',
            'customer_phone',
            'customer_email',
            'qr_code_string',
            'invoice_number',
            'invoice_issue_date',
            'invoice_due_date',
            'invoice_paid_status',
            'cart_id',
            'session_id',
            'order_id',
            'user',
            'backup_date',
        ]

        read_only_fields = ['user']

    # def validate_category_pk(self, value):
    #     print("value of category_pk")
    #     print(value)
    #     if value == None:
    #         raise serializers.ValidationError("category_pk is required")
    #     return value
    #
    # #
    # def validate_name(self, value):
    #     print("value of name")
    #     print(value)
    #     # if value != "Arif":
    #     #     raise serializers.ValidationError("Name is not Arif")
    #     if value is None:
    #         raise serializers.ValidationError("name is required")
    #     return value
    #
    # #
    # def validate_pos_backup(self, value):
    #     print("value of pos_backup")
    #     print(value)
    #     # if value is None or value == None:
    #     if value is None:
    #         raise serializers.ValidationError("pos_backup is required ")
    #     return value
    # def validate(self, data):
    #     print("value of data")
    #     print(data)
    #     return data



