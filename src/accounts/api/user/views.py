from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, pagination
from accounts.api.permissins import AnonPermissionOnly
from rest_framework.response import Response


# from pos.api.serializers import CategoryInlineUserSerializer
# from pos.api.views import CategoryAPIView
from rest_api.models import Category


from .serializers import UserDetailSerializer


User = get_user_model()

class UserDetailAPIView(generics.RetrieveAPIView):
    #permission_classes  = [permissions.IsAuthenticatedOrReadOnly]
    queryset            = User.objects.all()
    serializer_class    = UserDetailSerializer
    lookup_field        = 'phone' # id

    # def get_serializer_context(self):
    #     return {'request': self.request}


# class UserCategoryAPIView(CategoryAPIView):
#     serializer_class            = CategoryInlineUserSerializer
#     def get_queryset(self, *args, **kwargs):
#         phone = self.kwargs.get("phone", None)
#         if phone is None:
#             return Category.objects.none()
#         return Category.objects.filter(user__phone=phone)

#     def post(self, request, *args, **kwargs):
#         return Response({"detail": "Not allowed here"}, status=400)
        

# class UserStatusAPIView(generics.ListAPIView):
#     serializer_class            = StatusInlineUserSerializer
#     search_fields               = ('user__username', 'content')
#     #pagination_class    = CFEAPIPagination

#     def get_queryset(self, *args, **kwargs):
#         username = self.kwargs.get("username", None)
#         if username is None:
#             return Status.objects.none()
#         return Status.objects.filter(user__username=username)





