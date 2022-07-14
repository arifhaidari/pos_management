from rest_framework import serializers
from rest_api.models import ProductLog
from rest_framework.reverse import reverse as api_reverse


class ProductLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLog
        fields = [
            'id',
            'product_log_pk',
            'name',
            'purchase',
            'price',
            'barcode',
            'enable_product',
            'quantity',
            'weight',
            'all_log_id',
            'has_variant',
            'user',
            'backup_date',
        ]

        read_only_fields = ['user']





# from rest_framework import serializers
# from rest_api.models import Session
# from rest_framework.reverse import reverse as api_reverse
#
#
# class SessionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Session
#         fields = [
#             'id',
#             'opening_balance',
#             'closing_balance',
#             'order_no',
#             'opening_time',
#             'closing_time',
#             'close_status',
#             'session_purchase_price_total',
#             'net_revenue',
#             'session_discount',
#             'user',
#             'backup_date',
#         ]
#
#         read_only_fields = ['user']
#
        
    # def validate(self, data):
    #     print('inside the validate')
    #     print(data)
    #     # name = data.get("name", None)
    #     # if name == "":
    #     #     content = None
    #     # icon = data.get("icon", None)
    #     # if name is None and icon is None:
    #     #     raise serializers.ValidationError("name or icon is required.")
    #     return data
        

