
import datetime

from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework.reverse import reverse as api_reverse

jwt_payload_handler             = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler              = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler    = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
expire_delta                    = api_settings.JWT_REFRESH_EXPIRATION_DELTA

User = get_user_model()


class UserPublicSerializer(serializers.ModelSerializer):
     uri             = serializers.SerializerMethodField(read_only=True)
     class Meta:
          model = User
          fields = [
               'id',
               'full_name',
               'phone',
               'uri',
          ]
     def get_uri(self, obj):
          request = self.context.get('request')
          return api_reverse("api_user:detail", kwargs={"phone": obj.phone}, request=request)


class UserRegisterSerializer(serializers.ModelSerializer):
     password2                 = serializers.CharField(style={"input_type": "password"}, write_only=True)
     token                     = serializers.SerializerMethodField(read_only=True)
     expires                   = serializers.SerializerMethodField(read_only=True)
     message                   = serializers.SerializerMethodField(read_only=True)
     class Meta:
          model = User
          fields = [
               'phone',
               'full_name',
               'password',
               'password2',
               'token',
               'expires',
               'message',
          ]
          extra_kwargs = {"password": {"write_only": True}}
         
     def get_message(self, obj):
          return "thanks for registraiton, verify your email"
     
     def get_expires(self, obj):
          # return expire_delta
          return timezone.now() + expire_delta
          # return timezone.now() + expire_delta - datetime.timedelta(seconds=200)

     def get_token(self, obj): # obj is instance of model
          user = obj
          payload = jwt_payload_handler(user)
          token = jwt_encode_handler(payload)
          return token
     
     def validate_phone(self, value):
          qs = User.objects.filter(phone__iexact=value)
          if qs.exists():
               raise serializers.ValidationError("user with this phone number already exist")
          return value
     
     def validate_full_name(self, value):
          qs = User.objects.filter(full_name__iexact=value)
          if qs.exists():
               raise serializers.ValidationError("user with this full name already exist")
          return value
          
     def validate(self, data):
          pw = data.get("password")
          pw2 = data.get("password2")
          if pw != pw2:
               raise serializers.ValidationError("Passwords must match")
          return data
     
     def create(self, validated_data):
          print("inside create method")
          print(validated_data)
          user_obj = User(phone=validated_data.get("phone"), 
                          full_name=validated_data.get("full_name"))
          user_obj.set_password(validated_data.get("password"))
          user_obj.is_active = False
          user_obj.save()
          return user_obj
