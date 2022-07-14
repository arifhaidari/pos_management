from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions
from django.shortcuts import get_object_or_404
from datetime import datetime
import json
from rest_framework.authentication import SessionAuthentication

from accounts.api.permissins import IsOwnerOrReadOnly

from .serializers import PosOrderSerializer
from rest_api.models import PosOrder


def is_json(json_data):
     try:
          real_json = json.loads(json_data)
          is_valid = True
     except:
          is_valid = False
     return is_valid

class PosOrderDetailAPIView(
      mixins.UpdateModelMixin,
      mixins.DestroyModelMixin,
      generics.RetrieveAPIView):
     permission_classes       = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
     # authentication_classes   = []
     queryset                 = PosOrder.objects.all()
     serializer_class         = PosOrderSerializer
     lookup_field                = "pos_order_pk"
     
     def get_queryset(self):
          user_obj = self.request.user
          qs = user_obj.posorder_set.all()
          return qs
     
     def put(self, request, *args, **kwargs):
          return self.update(request, *args, **kwargs)
     
     def patch(self, request, *args, **kwargs):
          return self.update(request, *args, **kwargs)
     
     def delete(self, request, *args, **kwargs):
          return self.destroy(request, *args, **kwargs)
     
     
class PosOrderAPIView(
      mixins.CreateModelMixin,
      generics.ListAPIView):
     permission_classes       = [permissions.IsAuthenticatedOrReadOnly]
     serializer_class         = PosOrderSerializer
     passed_id                = None
     
     def get_queryset(self):
          user_obj = self.request.user
          qs = user_obj.posorder_set.all()
          return qs
     
     def post(self, request, *args, **kwargs):
          return self.create(request, *args, **kwargs)
     
     def perform_create(self, serializer):
          if not PosOrder.objects.filter(user=self.request.user, pos_order_pk=int(self.request.data['pos_order_pk'])).exists():
               serializer.save(user=self.request.user, timestamp=datetime.strptime(self.request.data['timestamp'], "%Y-%m-%d %H:%M:%S.%f"))

