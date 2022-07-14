from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from rest_framework import permissions, generics
from django.db.models import Q
from rest_framework_jwt.settings import api_settings
from .serializers import UserRegisterSerializer
from .permissins import AnonPermissionOnly
import datetime

jwt_payload_handler           = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler            = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler  = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User = get_user_model()


class AuthAPIView(APIView):
     # authentication_classes        = []
     permission_classes            = [permissions.AllowAny]
     def post(self, request, *args, **kwargs):
          if request.user.is_authenticated:
               return Response({"detail": "you are already logged in bro"}, status=400)
          data = request.data
          username = data.get("phone")
          password = data.get("password")
          # user = authenticate(username=username, password=password)
          qs = User.objects.filter(
               Q(phone__iexact=username) |
                 Q(full_name__iexact=username)
                 ).distinct()
          if qs.count() == 1:
               user_obj = qs.first()
               if user_obj.is_active == False:
                    return Response({"detail": "User is not activated"}, status=401)
               if user_obj.end_contract_at < datetime.date.today():
                    return Response({"detail": "Your Contract Is Expired"}, status=401)
               if user_obj.check_password(password):
                    user = user_obj
                    payload = jwt_payload_handler(user)
                    token = jwt_encode_handler(payload)
                    response = jwt_response_payload_handler(token, user, request=request)
                    # dic = {
                    #      "response": response,
                    #      "helooo": "hello John",
                    # }
                    return Response(response)
          return Response({"detail": "Invalid Credentials"}, status=401)

class ValidateUserAPIView(APIView):
     permission_classes            = [permissions.AllowAny]
     def post(self, request, *args, **kwargs):
          data = request.data
          print(data)
          phone = data.get("phone")
          access_code = data.get("access_code")
          password = data.get("password")
          repeat_password = data.get("repeat_password")
          if password != repeat_password:
               return Response({"detail": "Password doesn't match"}, status=401)
          qs = User.objects.filter(
               Q(phone__iexact=phone) &
                 Q(access_code__iexact=access_code)
                 ).distinct()
          if qs.count() == 1:
               user_obj = qs.first()
               if user_obj.is_active == False:
                    return Response({"detail": "User is not activated"}, status=401)
               if user_obj.end_contract_at < datetime.date.today():
                    return Response({"detail": "Your Contract Is Expired"}, status=401)
               if user_obj.check_password(password):
                    response = {
                         "full_name": user_obj.full_name,
                         "phone": user_obj.phone,
                         "business": user_obj.business,
                         "address": user_obj.address,
                         "password": user_obj.plain_password,
                         "access_code": user_obj.access_code,
                         "email": user_obj.email,
                         "start_contract_at": user_obj.start_contract_at,
                         "end_contract_at": user_obj.end_contract_at,
                    }

                    return Response(response)
          return Response({"detail": "Invalid Credentials"}, status=401)


class RegisterAPIView(generics.CreateAPIView):
     queryset                 = User.objects.all()
     serializer_class         = UserRegisterSerializer
     permission_classes       = [AnonPermissionOnly]
     
     def get_serializer_context(self, *args, **kwargs):
          return {"request": self.request}

# class RegisterAPIView(APIView):
#      # authentication_classes        = []
#      permission_classes            = [permissions.AllowAny]
#      def post(self, request, *args, **kwargs):
#           if request.user.is_authenticated:
#                return Response({"detail": "you are already logged in and registered"}, status=400)
#           data = request.data
#           phone = data.get("phone")
#           name = data.get("full_name")
#           password = data.get("password")
#           password2 = data.get("password2")
#           qs = User.objects.filter(
#                Q(phone__iexact=phone) |
#                  Q(full_name__iexact=name)
#                  )
#           if password != password2:
#                return Response({"detail": "Passwords must match"}, status=401)
#           if qs.exists():
#                return Response({"detail": "This user is already exist"}, status=401)
#           else:
#                user = User.objects.create(phone=phone, full_name=name)
#                user.set_password(password)
#                user.save()
#                # payload = jwt_payload_handler(user)
#                # token = jwt_encode_handler(payload)
#                # response = jwt_response_payload_handler(token, user, request=request)
#                # return Response(response, status=201)
#                return Response({"detail": "thanks for regsitration, Verify your phone number"}, status=201)
#           return Response({"detail": "Invalid Request"}, status=401)


