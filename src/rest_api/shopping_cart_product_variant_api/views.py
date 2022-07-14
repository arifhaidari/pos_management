# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import generics, mixins, permissions
# from django.shortcuts import get_object_or_404
# import json
# from rest_framework.authentication import SessionAuthentication
#
# from accounts.api.permissins import IsOwnerOrReadOnly
#
# from .serializers import ShoppingCartProductVariantSerializer
# from rest_api.models import ShoppingCartProductVariant
#
#
# def is_json(json_data):
#      try:
#           real_json = json.loads(json_data)
#           is_valid = True
#      except:
#           is_valid = False
#      return is_valid
#
# class ShoppingCartProductVariantDetailAPIView(
#       mixins.UpdateModelMixin,
#       mixins.DestroyModelMixin,
#       generics.RetrieveAPIView):
#      permission_classes       = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#      # authentication_classes   = []
#      queryset                 = ShoppingCartProductVariant.objects.all()
#      serializer_class         = ShoppingCartProductVariantSerializer
#      lookup_field                = "id"
#
#      def put(self, request, *args, **kwargs):
#           return self.update(request, *args, **kwargs)
#
#      def patch(self, request, *args, **kwargs):
#           return self.update(request, *args, **kwargs)
#
#      def delete(self, request, *args, **kwargs):
#           return self.destroy(request, *args, **kwargs)
#
#
# class ShoppingCartProductVariantAPIView(
#       mixins.CreateModelMixin,
#       generics.ListAPIView):
#      permission_classes       = [permissions.IsAuthenticatedOrReadOnly]
#      # authentication_classes   = [SessionAuthentication]
#      # queryset                 = ShoppingCartProductVariant.objects.all()
#      serializer_class         = ShoppingCartProductVariantSerializer
#      passed_id                = None
#
#      def get_queryset(self):
#           user_obj = self.request.user
#           qs = user_obj.shoppingcartproductvariant_set.all()
#           query = self.request.GET.get('q')
#           if query is not None:
#                qs = qs.filter(pos_backup__id__iexact=query)
#           return qs
#
#
#      def post(self, request, *args, **kwargs):
#           return self.create(request, *args, **kwargs)
#
#      def perform_create(self, serializer):
#           serializer.save(user=self.request.user)
#
