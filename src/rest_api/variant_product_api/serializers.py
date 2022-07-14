from rest_framework import serializers
from rest_api.models import VariantProduct
from rest_framework.reverse import reverse as api_reverse


class VariantProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariantProduct
        fields = [
            'id',
            'variant_product_pk',
            'variant_id',
            'product_id',
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
        



