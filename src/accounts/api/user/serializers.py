import datetime

from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

# from pos.api.serializers import CategoryInlineUserSerializer

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    uri             = serializers.SerializerMethodField(read_only=True)
    # category          = serializers.SerializerMethodField(read_only=True)
    # statuses        = serializers.HyperlinkedRelatedField(
    #                         source = 'status_set', # Status.objects.filter(user=user)
    #                         many=True,
    #                         read_only=True,
    #                         lookup_field ='id',
    #                         view_name='api-status:detail',
    #                     )
    #statuses        = StatusInlineUserSerializer(source='status_set', many=True, read_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'full_name',
            'phone',
            'uri',
            'business', 
            'address', 
            'email',
            # 'is_active',
            'deal_amount',
            'timestamp', 
        ]

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse("api_user:detail", kwargs={"phone": obj.phone}, request=request)

    # def get_category(self, obj):
    #     request = self.context.get('request')
    #     limit = 10
    #     if request:
    #         limit_query = request.GET.get('limit')
    #         try:
    #             limit = int(limit_query)
    #         except:
    #             pass
    #     qs = obj.category_set.all() #[:10] # Category.objects.filter(user=user)
    #     data = {
    #         'uri': self.get_uri(obj) + "list/",
    #         'last': CategoryInlineUserSerializer(qs.first(), context={'request': request}).data,
    #         'recent': CategoryInlineUserSerializer(qs[:limit], many=True, context={'request': request}).data
    #     }
        # return data



