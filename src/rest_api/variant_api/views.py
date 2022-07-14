from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions
from django.shortcuts import get_object_or_404
import json
from rest_framework.authentication import SessionAuthentication

from accounts.api.permissins import IsOwnerOrReadOnly

from .serializers import VariantSerializer
from rest_api.models import Variant, VariantOption, VariantProduct, ProductVariantOption


def is_json(json_data):
     try:
          real_json = json.loads(json_data)
          is_valid = True
     except:
          is_valid = False
     return is_valid

class VariantDetailAPIView(
      mixins.UpdateModelMixin,
      mixins.DestroyModelMixin,
      generics.RetrieveAPIView):
     permission_classes       = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
     # authentication_classes   = []
     queryset                 = Variant.objects.all()
     serializer_class         = VariantSerializer
     lookup_field                = "variant_pk"
     
     def get_queryset(self):
          user_obj = self.request.user
          qs = user_obj.variant_set.all()
          return qs
     
     def put(self, request, *args, **kwargs):
          variant_updation(self.request.user, kwargs)
          return self.update(request, *args, **kwargs)
     
     def patch(self, request, *args, **kwargs):
          return self.update(request, *args, **kwargs)
     
     def delete(self, request, *args, **kwargs):
          variant_updation(self.request.user, kwargs)
          return self.destroy(request, *args, **kwargs)
     
     
class VariantAPIView(
      mixins.CreateModelMixin,
      generics.ListAPIView):
     permission_classes       = [permissions.IsAuthenticatedOrReadOnly]
     serializer_class         = VariantSerializer
     passed_id                = None
     
     def get_queryset(self):
          user_obj = self.request.user
          qs = user_obj.variant_set.all()
          return qs
     
     
     def post(self, request, *args, **kwargs):
          return self.create(request, *args, **kwargs)
     
     def perform_create(self, serializer):
          if not Variant.objects.filter(user=self.request.user, variant_pk=int(self.request.data['variant_pk'])).exists():
               serializer.save(user=self.request.user)


def variant_updation(user, data):
     variant_pk = data['variant_pk']
     VariantOption.objects.filter(user=user, variant_id=variant_pk).delete()
     VariantProduct.objects.filter(user=user, variant_id=variant_pk).delete()
     ProductVariantOption.objects.filter(user=user, variant_id=variant_pk).delete()
     
     