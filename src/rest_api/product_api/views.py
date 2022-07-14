from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions
from django.shortcuts import get_object_or_404
import json
from rest_framework.authentication import SessionAuthentication

from accounts.api.permissins import IsOwnerOrReadOnly

from .serializers import ProductSerializer
from rest_api.models import (
     Product, CategoryProduct, VariantProduct, 
     ProductVariantOption, Barcode,
)

def is_json(json_data):
     try:
          real_json = json.loads(json_data)
          is_valid = True
     except:
          is_valid = False
     return is_valid

class ProductDetailAPIView(
      mixins.UpdateModelMixin,
      mixins.DestroyModelMixin,
      generics.RetrieveAPIView):
     permission_classes       = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
     serializer_class         = ProductSerializer
     lookup_field                = "product_pk"
     
     def get_queryset(self): 
          user_obj = self.request.user
          qs = user_obj.product_set.all()
          return qs
     
     def put(self, request, *args, **kwargs):
          # print(self.request.user)
          # print(self.request.data) # data will be here e.g: {'product_pk': 1, 'name': 'Glass One', 'purchase': 110}
          # print(len(self.request.data)) 
          # print(kwargs) # id (product_pk) will be here 
          if len(self.request.data) > 2:
               product_updation(self.request.user, kwargs)
          return self.update(request, *args, **kwargs)
     
     def patch(self, request, *args, **kwargs):
          return self.update(request, *args, **kwargs)
     
     def delete(self, request, *args, **kwargs):
          product_updation(self.request.user, kwargs)
          return self.destroy(request, *args, **kwargs)
     
     
class ProductAPIView(
      mixins.CreateModelMixin,
      generics.ListAPIView):
     permission_classes       = [permissions.IsAuthenticatedOrReadOnly]
     serializer_class         = ProductSerializer
     
     def get_queryset(self):
          user_obj = self.request.user
          qs = user_obj.product_set.all()
          return qs
     
     
     def post(self, request, *args, **kwargs):
          return self.create(request, *args, **kwargs)
     
     def perform_create(self, serializer):
          if not Product.objects.filter(user=self.request.user, product_pk=int(self.request.data['product_pk'])).exists():
               serializer.save(user=self.request.user)


def product_updation(user, data):
     product_pk = data['product_pk']
     VariantProduct.objects.filter(user=user, product_id=product_pk).delete()
     ProductVariantOption.objects.filter(user=user, product_id=product_pk).delete()
     CategoryProduct.objects.filter(user=user, product_id=product_pk).delete()
     Barcode.objects.filter(user=user, product_id=product_pk).delete()


