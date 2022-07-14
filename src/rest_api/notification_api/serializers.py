from rest_framework import serializers
from rest_api.models import Notification
from rest_framework.reverse import reverse as api_reverse


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'id',
            'notification_pk',
            'subject',
            'timestamp',
            'detail_id',
            'seen_status',
            'user',
            'backup_date',
        ]
        
        read_only_fields = ['user']
        
        


        