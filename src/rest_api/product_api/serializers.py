from rest_framework import serializers
from rest_api.models import Product
from rest_framework.reverse import reverse as api_reverse


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'product_pk',
            'name',
            'alias',
            'purchase',
            'price',
            'picture',
            'barcode',
            'enable_product',
            'quantity',
            'weight',
            'has_variant',
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
        
