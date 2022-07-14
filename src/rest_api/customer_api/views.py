# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import generics, mixins, permissions
# from django.shortcuts import get_object_or_404
# import json
# from rest_framework.authentication import SessionAuthentication
#
# from accounts.api.permissins import IsOwnerOrReadOnly
#
# from .serializers import CustomerSerializer
# from rest_api.models import Customer
#
#
# def is_json(json_data):
#     try:
#         real_json = json.loads(json_data)
#         is_valid = True
#     except:
#         is_valid = False
#     return is_valid
#
#
# class CustomerDetailAPIView(
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     # authentication_classes   = []
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#     # lookup_field                = "id"
#     lookup_field = "id"
#     # passed_id = None
#
#     # do update by another field as well other than id so if you
#     # recieve any other field by api then find it and update
#     # needs to be accordingly like which user and which version
#
#     # and same scenario applies for deleting an object as well
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#
# class CustomerAPIView(
#     mixins.CreateModelMixin,
#     generics.ListAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     # authentication_classes   = [SessionAuthentication]
#     # queryset                 = Category.objects.all()
#     # in queryset we do filter by user and version of backup
#     # or create get_queryset function to which based on that we do search or pass our
#     # backup_version
#     serializer_class = CustomerSerializer
#     passed_id = None
#
#     def get_queryset(self):
#         # qs = Category.objects.filter(user__full_name__iexact="Arif Elbis")
#         # qs = obj.category_set.all() #[:10] # Category.objects.filter(user=user)
#         # qs = Category.objects.filter(user__id__iexact=3)
#         user_obj = self.request.user
#         qs = user_obj.customer_set.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(pos_backup__id__iexact=query)
#             # qs = qs.filter(name__icontains=query)
#             # qs = qs.filter(name__iexact=query)
#             # icontains usually used for search
#             # iexact usually used for query of foreignkeys
#         return qs
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
