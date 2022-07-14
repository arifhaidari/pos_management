from rest_framework import serializers
from rest_api.models import SelectedProductVariant
from rest_framework.reverse import reverse as api_reverse


class SelectedProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedProductVariant
        fields = [
            'id',
            'selected_product_variant_pk',
            'option_name',
            'price',
            'product_variant_option_id',
            'option_id',
            'variant_id',
            'product_id',
            'shopping_cart_id',
            'shopping_cart_product_id',
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
        

