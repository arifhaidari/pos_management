from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions
from django.shortcuts import get_object_or_404
import json
from django.db.models import Max, Avg, Min, Sum
from rest_framework.authentication import SessionAuthentication

from accounts.api.permissins import IsOwnerOrReadOnly

from .serializers import CategorySerializer
from rest_api.models import Category, CategoryProduct


# def is_json(json_data):
#      try:
#           real_json = json.loads(json_data)
#           is_valid = True
#      except:
#           is_valid = False
#      return is_valid

class CategoryDetailAPIView(
      mixins.UpdateModelMixin,
      mixins.DestroyModelMixin,
      generics.RetrieveAPIView):
     permission_classes       = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
     # authentication_classes   = []
     queryset                 = Category.objects.all()
     serializer_class         = CategorySerializer
     lookup_field                = "category_pk"
     # passed_id = None
     # do update by another field as well other than id so if you
     # recieve any other field by api then find it and update
     # needs to be accordingly like which user and which version
 
     # and same scenario applies for deleting an object as well
     
     def get_queryset(self):
          user_obj = self.request.user
          qs = user_obj.category_set.all()
          return qs
     
     def put(self, request, *args, **kwargs):
          return self.update(request, *args, **kwargs)
     
     def patch(self, request, *args, **kwargs):
          return self.update(request, *args, **kwargs)

     def delete(self, request, *args, **kwargs):
          category_updation(self.request.user, kwargs)
          return self.destroy(request, *args, **kwargs)
     
     # def perform_destroy(self, instance):
     #     if instance is not None:
     #          return instance.delete()
     #      return None
     #     #return super().perform_destroy(instance)
     
     # def perform_update(self, serializer):
     #     serializer.save(updated_by_user=self.request.user)
     #     return super().perform_update(serializer)
     
     
class CategoryAPIView(
      mixins.CreateModelMixin,
      generics.ListAPIView):
     permission_classes       = [permissions.IsAuthenticatedOrReadOnly]
     # authentication_classes   = [SessionAuthentication]
     # queryset                 = Category.objects.all()
     # in queryset we do filter by user and version of backup
     # or create get_queryset function to which based on that we do search or pass our
     # backup_version
     serializer_class         = CategorySerializer
     # passed_id                = None
     # metadata_class = Category
     # def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#         "user": ser.CreateUserSerializer(user, context=self.get_serializer_context()).data,
#         # "token": AuthToken.objects.create(user)[1]
#         })

     # # generics.ListAPIView //Concrete view for listing a queryset.
     # def get(self, request, *args, **kwargs):
     #      return self.list(request, *args, **kwargs)

     # # generics.RetrieveAPIView) //Concrete view for retrieving a model instance.
     # def get(self, request, *args, **kwargs):
     #      return self.retrieve(request, *args, **kwargs)

     def get_queryset(self):
          # qs = Category.objects.filter(user__full_name__iexact="Arif Elbis")
          # qs = obj.category_set.all() #[:10] # Category.objects.filter(user=user)
          # qs = Category.objects.filter(user__id__iexact=3)
          user_obj = self.request.user
          qs = user_obj.category_set.all()
          # query = self.request.GET.get('q')
          # if query is not None:
          #      qs = qs.filter(pos_backup__id__iexact=query)
               # qs = qs.filter(name__icontains=query)
               # qs = qs.filter(name__iexact=query)
               # icontains usually used for search 
               # iexact usually used for query of foreignkeys
          return qs
     
     def post(self, request, *args, **kwargs):
          # print("values of kwargs")
          # print(kwargs) #empty
          # print(kwargs.values()) #empty
          # print(args)#empty
          # print(request.data['name'])
          return self.create(request, *args, **kwargs)
     
     def perform_create(self, serializer):
          # id_max_value = Category.objects.all().aggregate(Max('id'))
          # print(id_max_value['id__max'])
          if not Category.objects.filter(user=self.request.user, category_pk=int(self.request.data['category_pk'])).exists():
               serializer.save(user=self.request.user)
               # the other data is coming from post request and the user we add before to save it 
               # serializer.save(user=self.request.user, id=int(self.request.data['id']))

def category_updation(user, data):
     print('inside the category_updation')
     category_pk = data['category_pk']
     CategoryProduct.objects.filter(user=user, category_id=category_pk).delete()
