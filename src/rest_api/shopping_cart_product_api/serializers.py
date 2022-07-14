from rest_framework import serializers
from rest_api.models import ShoppingCartProduct
from rest_framework.reverse import reverse as api_reverse


class ShoppingCartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartProduct
        fields = [
            'id',
            'shopping_cart_product_pk',
            'product_quantity',
            'product_subtotal',
            'product_discount',
            'product_purchase_price_total',
            'has_variant_option',
            'product_id',
            'shopping_cart_id',
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
        


