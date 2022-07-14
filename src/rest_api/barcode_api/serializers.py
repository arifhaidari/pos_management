from rest_framework import serializers
from rest_api.models import Barcode
from rest_framework.reverse import reverse as api_reverse


class BarcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barcode
        fields = [
            'id',
            'barcode_pk',
            'name',
            'product_id',
            'barcode_text',
            'user',
            'backup_date',
        ]
        
        read_only_fields = ['user']
  
    # def validate(self, data):
    #     name = data.get("name", None)
    #     if name == "":
    #         name = None
    #     icon = data.get("barcode_text", None)
    #     if name is None and icon is None:
    #         raise serializers.ValidationError("name or barcode_text is required.")
    #     return data


