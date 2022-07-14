from rest_framework import serializers
from rest_api.models import Session
from rest_framework.reverse import reverse as api_reverse


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = [
            'id',
            'session_pk',
            'opening_balance',
            'opening_time',
            'closing_time',
            'session_comment',
            'close_status',
            'drawer_status',
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
        

