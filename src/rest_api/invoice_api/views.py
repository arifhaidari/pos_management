from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions
from django.shortcuts import get_object_or_404
from datetime import datetime
import json
from rest_framework.authentication import SessionAuthentication

from accounts.api.permissins import IsOwnerOrReadOnly

from .serializers import InvoiceSerializer
from rest_api.models import Invoice


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except:
        is_valid = False
    return is_valid


class InvoiceDetailAPIView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # authentication_classes   = []
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    # lookup_field                = "id"
    lookup_field = "invoice_pk"
    # passed_id = None
    
    def get_queryset(self):
        user_obj = self.request.user
        qs = user_obj.invoice_set.all()
        return qs

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class InvoiceAPIView(
    mixins.CreateModelMixin,
    generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = InvoiceSerializer
    passed_id = None

    def get_queryset(self):
        user_obj = self.request.user
        qs = user_obj.invoice_set.all()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        if not Invoice.objects.filter(user=self.request.user, invoice_pk=int(self.request.data['invoice_pk'])).exists():
            serializer.save(user=self.request.user)
            # serializer.save(user=self.request.user,
            #                 invoice_issue_date=datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f"),
            #                 invoice_due_date=datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f"))




