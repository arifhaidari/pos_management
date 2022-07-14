from rest_framework import serializers
from rest_api.models import PosOrder
from rest_framework.reverse import reverse as api_reverse


class PosOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PosOrder
        fields = [
            'id',
            'pos_order_pk',
            'order_subtotal',
            'order_purchase_price_total',
            'order_discount',
            'cash_collected',
            'change_due',
            'order_item_no',
            'timestamp',
            'qr_code_string',
            'payment_completion_status',
            'cart_id',
            'session_id',
            'user',
            'backup_date',
        ]
        
        read_only_fields = ['user']
        
        
    # def validate(self, data):
    #     name = data.get("name", None)
    #     if name == "":
    #         content = None
    #     icon = data.get("icon", None)
    #     if name is None and icon is None:
    #         raise serializers.ValidationError("name or icon is required.")
    #     return data
        
