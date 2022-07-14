# from rest_framework import serializers
# from rest_api.models import ShoppingCartProductVariant
# from rest_framework.reverse import reverse as api_reverse
#
#
# class ShoppingCartProductVariantSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ShoppingCartProductVariant
#         fields = [
#             'shopping_cart_product_variant_pk',
#             'option_extra_price',
#             'shopping_product_id',
#             'variant_id',
#             'option_id',
#             'user',
#             'backup_date',
#         ]
#
#         read_only_fields = ['user']
#
#
#     # def validate(self, data):
#     #     name = data.get("name", None)
#     #     if name == "":
#     #         content = None
#     #     icon = data.get("icon", None)
#     #     if name is None and icon is None:
#     #         raise serializers.ValidationError("name or icon is required.")
#     #     return data
#
#
#
