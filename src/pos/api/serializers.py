# from rest_framework import serializers
# from pos.models import PosBackup
# from rest_framework.reverse import reverse as api_reverse


# class PosBackupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PosBackup
#         fields = [
#             'id',
#             'version_name',
#             'user',
#             'backup_date',
#         ]
        
#         read_only_fields = ['user']
    
    
    # def validate_version_name(self, value):
    #     # qs = User.objects.filter(phone__iexact=value)
    #     user_obj = self.context['request'].user
    #     print("value of value: " + value)
    #     if value == "":
    #         # create random number and check if it is not available in the system
    #         # and then store it as a version name
    #         raise serializers.ValidationError("the version name value is empty")
    #     # qs = user_obj.posbackup_set.filter(version_name__iexact=value)
    #     qs = PosBackup.objects.get(id=2)
    #     print("count of qs:")
    #     # print(qs.count())
    #     print(qs)
    #     # if qs.exists():
    #     if qs.exists() == 1:
    #         # if exist create a new one
    #         raise serializers.ValidationError("version name is already existed")
    #     return value
    
    # def validate(self, data):
    #     print("value of data")
    #     print(data)
        # user_obj = self.user.request
        # version_name = data.get("version_name", None)
        # if name == "":
        #     # create random number and check if it is not available in the system
        #     # and then store it as a version name
        #     content = None
        # if name is None:
        #     raise serializers.ValidationError("name or icon is required.")
        # return data
        

