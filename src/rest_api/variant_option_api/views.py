from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions
from django.shortcuts import get_object_or_404
import json
from rest_framework.authentication import SessionAuthentication

from accounts.api.permissins import IsOwnerOrReadOnly

from .serializers import VariantOptionSerializer
from rest_api.models import VariantOption


def is_json(json_data):
     try:
          real_json = json.loads(json_data)
          is_valid = True
     except:
          is_valid = False
     return is_valid

class VariantOptionDetailAPIView(
      mixins.UpdateModelMixin,
      mixins.DestroyModelMixin,
      generics.RetrieveAPIView):
     permission_classes       = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
     # authentication_classes   = []
     queryset                 = VariantOption.objects.all()
     serializer_class         = VariantOptionSerializer
     lookup_field                = "variant_option_pk"
     
     def get_queryset(self):
          user_obj = self.request.user
          qs = user_obj.variantoption_set.all()
          return qs
     
     def put(self, request, *args, **kwargs):
          return self.update(request, *args, **kwargs)
     
     def patch(self, request, *args, **kwargs):
          return self.update(request, *args, **kwargs)
     
     def delete(self, request, *args, **kwargs):
          return self.destroy(request, *args, **kwargs)
     
     
class VariantOptionAPIView(
      mixins.CreateModelMixin,
      generics.ListAPIView):
     permission_classes       = [permissions.IsAuthenticatedOrReadOnly]
     serializer_class         = VariantOptionSerializer
     # passed_id                = None
     
     def get_queryset(self):
          user_obj = self.request.user
          qs = user_obj.variantoption_set.all()
          return qs
     
     
     def post(self, request, *args, **kwargs):
          return self.create(request, *args, **kwargs)
     
     def perform_create(self, serializer):
          if not VariantOption.objects.filter(user=self.request.user, variant_option_pk=int(self.request.data['variant_option_pk'])).exists():
               serializer.save(user=self.request.user)

