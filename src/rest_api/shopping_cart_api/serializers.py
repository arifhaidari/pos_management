from rest_framework import serializers
from rest_api.models import ShoppingCart
from rest_framework.reverse import reverse as api_reverse


class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = [
            'id',
            'shopping_cart_pk',
            'subtotal',
            'cart_purchase_price_total',
            'total_discount',
            'cart_item_quantity',
            'timestamp',
            'checked_out',
            'on_hold',
            'return_order',
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
    #     # if you validate every parameter individually then you cannot use it again in
    #     # general validation
    #     print("value of data")
    #     print(data)
    #     # name = data.get("name", None)
    #     # print("vlaue of name")
    #     # print(name)
    #     #
    #     # if name is None:
    #     #     raise serializers.ValidationError("name is required")
    #     # # icon = data.get("category_pk", None)
    #     # if name != "Arif":
    #     #     raise serializers.ValidationError("name or category_pk is required.")
    #     return data

