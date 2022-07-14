# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import generics, mixins, permissions
# from django.shortcuts import get_object_or_404
# import json
# from rest_framework.authentication import SessionAuthentication

# from accounts.api.permissins import IsOwnerOrReadOnly

# from .serializers import PosBackupSerializer
# from pos.models import PosBackup


# def is_json(json_data):
#      try:
#           real_json = json.loads(json_data)
#           is_valid = True
#      except:
#           is_valid = False
#      return is_valid

# class PosBackupDetailAPIView(
#       mixins.UpdateModelMixin,
#       mixins.DestroyModelMixin,
#       generics.RetrieveAPIView):
#      permission_classes       = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#      # authentication_classes   = []
#      queryset                 = PosBackup.objects.all()
#      serializer_class         = PosBackupSerializer
#      lookup_field                = "id"
     
#      def put(self, request, *args, **kwargs):
#           return self.update(request, *args, **kwargs)
     
#      def patch(self, request, *args, **kwargs):
#           return self.update(request, *args, **kwargs)
     
#      def delete(self, request, *args, **kwargs):
#           return self.destroy(request, *args, **kwargs)
     
#      # def perform_destroy(self, instance):
#      #      if instance is not None:
#      #           return instance.delete()
#      #      return None
     
#      # def perform_create(self, serializer):
#      #      serializer.save(user=self.request.user)
     
# class PosBackupAPIView(
#       mixins.CreateModelMixin,
#       generics.ListAPIView):
#      permission_classes       = [permissions.IsAuthenticatedOrReadOnly]
#      # authentication_classes   = [SessionAuthentication]
#      queryset                 = PosBackup.objects.all()
#      serializer_class         = PosBackupSerializer
#      passed_id                = None
#      # search_fields            = ('user__ phone', 'name')
#      # ordering_fields          = ('user__full_name', 'name')
     
#      def get_queryset(self):
#           # qs = Category.objects.all()
#           user_obj = self.request.user
#           qs = user_obj.posbackup_set.all()
#           query = self.request.GET.get('q')
#           if query is not None:
#                qs = qs.filter(name__icontains=query)
#           return qs
     
#      def post(self, request, *args, **kwargs):
#           return self.create(request, *args, **kwargs)
     
#      def perform_create(self, serializer):
#           serializer.save(user=self.request.user)


# class CategoryAPIView(
#       mixins.CreateModelMixin,
#       mixins.RetrieveModelMixin,
#       mixins.UpdateModelMixin,
#       mixins.DestroyModelMixin,
#       generics.ListAPIView):
#      permission_classes       = []
#      authentication_classes   = []
#      # queryset                 = Category.objects.all()
#      serializer_class         = CategorySerializer
#      passed_id                = None
     
#      def get_queryset(self):
#           qs = Category.objects.all()
#           query = self.request.GET.get('q')
#           if query is not None:
#                qs = qs.filter(name__icontains=query)
#           return qs
     
#      def get_object(self):
#           passed_id = self.request.GET.get("id", None) or self.passed_id
#           queryset = self.get_queryset()
#           obj = None
#           if passed_id is not None:
#                obj = get_object_or_404(queryset, id=passed_id)
#                self.check_object_permissions(self.request, obj)
#           return obj
     
#      def get(self, request, *args, **kwargs):
#           url_passed_id = self.request.GET.get("id", None)
#           json_data = {}
#           body_ = request.body
#           if is_json(body_):
#                json_data = json.loads(request.body)
#           new_passed_id = json_data.get("id", None)
#           passed_id = url_passed_id or new_passed_id or None
#           self.passed_id = passed_id
#           # print("inside the get method")
#           # print(request.body)
#           # print(request.)
#           if passed_id is not None:
#                return self.retrieve(request, *args, **kwargs)
#           return super().get(request, *args, **kwargs)
     
     
#      def post(self, request, *args, **kwargs):
#           url_passed_id = self.request.GET.get("id", None)
#           json_data = {}
#           body_ = request.body
#           if is_json(body_):
#                json_data = json.loads(request.body)
#           new_passed_id = json_data.get("id", None)
#           passed_id = url_passed_id or new_passed_id or None
#           self.passed_id = passed_id
#           return self.create(request, *args, **kwargs)
     
#      def put(self, request, *args, **kwargs):
#           url_passed_id = self.request.GET.get("id", None)
#           json_data = {}
#           body_ = request.body
#           if is_json(body_):
#                json_data = json.loads(request.body)
#           new_passed_id = json_data.get("id", None)
#           passed_id = url_passed_id or new_passed_id or None
#           self.passed_id = passed_id
#           return self.update(request, *args, **kwargs)
     
#      def patch(self, request, *args, **kwargs):
#           url_passed_id = self.request.GET.get("id", None)
#           json_data = {}
#           body_ = request.body
#           if is_json(body_):
#                json_data = json.loads(request.body)
#           new_passed_id = json_data.get("id", None)
#           passed_id = url_passed_id or new_passed_id or None
#           self.passed_id = passed_id
#           return self.update(request, *args, **kwargs)
     
#      def perform_destroy(self, instance):
#           if instance is not None:
#                return instance.delete()
#           return None
     
#      def delete(self, request, *args, **kwargs):
#           url_passed_id = self.request.GET.get("id", None)
#           json_data = {}
#           body_ = request.body
#           if is_json(body_):
#                json_data = json.loads(request.body)
#           new_passed_id = json_data.get("id", None)
#           passed_id = url_passed_id or new_passed_id or None
#           self.passed_id = passed_id
#           return self.destroy(request, *args, **kwargs)
     
#      # def perform_create(self, serializer):
#      #      serializer.save(user=self.request.user)



# class CategoryAPIView(mixins.CreateModelMixin, generics.ListAPIView):
#      permission_classes       = []
#      authentication_classes   = []
#      # queryset                 = Category.objects.all()
#      serializer_class         = CategorySerializer
     
#      def get_queryset(self):
#           qs = Category.objects.all()
#           query = self.request.GET.get('q')
#           if query is not None:
#                qs = qs.filter(name__icontains=query)
#           return qs
     
#      def post(self, request, *args, **kwargs):
#           return self.create(request, *args, **kwargs)
     
#      # def perform_create(self, serializer):
#      #      serializer.save(user=self.request.user)


# class CategoryDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
#      permission_classes       = []
#      authentication_classes   = []
#      queryset                 = Category.objects.all()
#      serializer_class         = CategorySerializer
#      # lookup_field             = "id"
     
#      def put(self, request, *args, **kwargs):
#           return self.update(request, *args, **kwargs)
     
#      def delete(self, request, *args, **kwargs):
#           return self.destroy(request, *args, **kwargs)
     
     # def get_object(self, *args, **kwargs):
     #      id_ = self.kwargs.get("pk")
     #      print("this id of get_object")
     #      print(id_)
     #      return Category.objects.get(pk = id_)
    
# class CategoryUpdateAPIView(generics.UpdateAPIView):
#      permission_classes       = []
#      authentication_classes   = []
#      queryset                 = Category.objects.all()
#      serializer_class         = CategorySerializer


# class CategoryDeleteAPIView(generics.DestroyAPIView):
#      permission_classes       = []
#      authentication_classes   = []
#      queryset                 = Category.objects.all()
#      serializer_class         = CategorySerializer




# class CategoryCreateAPIView(generics.CreateAPIView):
#      permission_classes       = []
#      authentication_classes   = []
#      queryset                 = Category.objects.all()
#      serializer_class         = CategorySerializer

# class CategoryListSearchAPIView(APIView):
#      permission_classes       = []
#      authentication_classes   = []
     
#      def get(self, request, format=None):
#           qs = Category.objects.all()
#           serialized_data = CategorySerializer(qs, many=True)
#           return Response(serialized_data.data)
     
#      def post(self, request, format=None):
#           qs = Category.objects.all()
#           serialized_data = CategorySerializer(qs, many=True)
#           return Response(serialized_data.data)