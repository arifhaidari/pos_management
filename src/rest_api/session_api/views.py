from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions
from django.shortcuts import get_object_or_404
from datetime import datetime
import json
from rest_framework.authentication import SessionAuthentication

from accounts.api.permissins import IsOwnerOrReadOnly

from .serializers import SessionSerializer
from rest_api.models import Session


def is_json(json_data):
     try:
          real_json = json.loads(json_data)
          is_valid = True
     except:
          is_valid = False
     return is_valid


class SessionDetailAPIView(
     mixins.UpdateModelMixin,
     mixins.DestroyModelMixin,
     generics.RetrieveAPIView):
     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
     # authentication_classes   = []
     # queryset = Session.objects.all()
     serializer_class = SessionSerializer
     lookup_field = "session_pk"
     
     def get_queryset(self):
          user_obj = self.request.user
          qs = user_obj.session_set.all()
          return qs

     def put(self, request, *args, **kwargs):
          # print(self.request.user)
          # print(self.request.data) # data will be here e.g: {'product_pk': 1, 'name': 'Glass One', 'purchase': 110}
          # print(len(self.request.data)) 
          # print(kwargs) # id (product_pk) will be here 
          return self.update(request, *args, **kwargs)

     def patch(self, request, *args, **kwargs):
          return self.update(request, *args, **kwargs)

     def delete(self, request, *args, **kwargs):
          return self.destroy(request, *args, **kwargs)


class SessionAPIView(
     mixins.CreateModelMixin,
     generics.ListAPIView):
     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
     serializer_class = SessionSerializer
     passed_id = None

     def get_queryset(self):
          user_obj = self.request.user
          qs = user_obj.session_set.all()
          return qs

     def post(self, request, *args, **kwargs):
          return self.create(request, *args, **kwargs)

     def perform_create(self, serializer):
          if not Session.objects.filter(user=self.request.user, session_pk=int(self.request.data['session_pk'])).exists():
               serializer.save(user=self.request.user, opening_time=datetime.strptime(self.request.data['opening_time'], "%Y-%m-%d %H:%M:%S.%f"), closing_time=datetime.strptime(self.request.data['closing_time'], "%Y-%m-%d %H:%M:%S.%f"))
