from rest_framework import serializers
from rest_api.models import CategoryProduct
from rest_framework.reverse import reverse as api_reverse


class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        fields = [
            'id',
            'category_product_pk',
            'category_id',
            'product_id',
            'user',
            'backup_date',
        ]
        
        read_only_fields = ['user']
        
    # def validate(self, data):
    #     name = data.get("category_product_pk", None)
    #     if name == "":
    #         content = None
    #     if name is None:
    #         raise serializers.ValidationError("category_product_pk is required.")
    #     return data


