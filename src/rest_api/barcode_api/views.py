from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions
from django.shortcuts import get_object_or_404
import json
from rest_framework.authentication import SessionAuthentication

from accounts.api.permissins import IsOwnerOrReadOnly

from .serializers import BarcodeSerializer
from rest_api.models import Barcode


def is_json(json_data):
     try:
          real_json = json.loads(json_data)
          is_valid = True
     except:
          is_valid = False
     return is_valid

class BarcodeDetailAPIView(
      mixins.UpdateModelMixin,
      mixins.DestroyModelMixin,
      generics.RetrieveAPIView):
     permission_classes       = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
     # authentication_classes   = []
     # queryset                 = Barcode.objects.all()
     serializer_class         = BarcodeSerializer
     lookup_field                = "barcode_pk"
     
     def get_queryset(self):
          user_obj = self.request.user
          qs = user_obj.barcode_set.all()
          return qs
     
     def put(self, request, *args, **kwargs):
          return self.update(request, *args, **kwargs)
     
     def patch(self, request, *args, **kwargs):
          return self.update(request, *args, **kwargs)
     
     def delete(self, request, *args, **kwargs):
          # barcode_updation(self.request.user, kwargs)
          return self.destroy(request, *args, **kwargs)
     
     
class BarcodeAPIView(
      mixins.CreateModelMixin,
      generics.ListAPIView):
     permission_classes       = [permissions.IsAuthenticatedOrReadOnly]
     # authentication_classes   = [SessionAuthentication]
     # queryset                 = Barcode.objects.all()
     serializer_class         = BarcodeSerializer
     # passed_id                = None
     
     def get_queryset(self):
          user_obj = self.request.user
          qs = user_obj.barcode_set.all()
          return qs
     
     def post(self, request, *args, **kwargs):
          return self.create(request, *args, **kwargs)
     
     def perform_create(self, serializer):
          if not Barcode.objects.filter(user=self.request.user, barcode_pk=int(self.request.data['barcode_pk'])).exists():
               serializer.save(user=self.request.user)
               # serializer.save(user=self.request.user, id=int(self.request.data['id']))

