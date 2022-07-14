# from rest_framework import serializers
# from rest_api.models import Customer
# from rest_framework.reverse import reverse as api_reverse
#
#
# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = [
#             # 'id',
#             'customer_pk',
#             'name',
#             'address',
#             'phone',
#             'email',
#             'user',
#             'backup_date',
#         ]
#
#         read_only_fields = ['user']
#
#     # def validate_category_pk(self, value):
#     #     print("value of category_pk")
#     #     print(value)
#     #     if value == None:
#     #         raise serializers.ValidationError("category_pk is required")
#     #     return value
#     #
#     # #
#     # def validate_name(self, value):
#     #     print("value of name")
#     #     print(value)
#     #     # if value != "Arif":
#     #     #     raise serializers.ValidationError("Name is not Arif")
#     #     if value is None:
#     #         raise serializers.ValidationError("name is required")
#     #     return value
#     #
#     # #
#     # def validate_pos_backup(self, value):
#     #     print("value of pos_backup")
#     #     print(value)
#     #     # if value is None or value == None:
#     #     if value is None:
#     #         raise serializers.ValidationError("pos_backup is required ")
#     #     return value
#
#
