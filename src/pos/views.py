from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import JsonResponse
from django.db.models import Sum, Count, Max
from django.utils import timezone
from django.urls import path, reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView, TemplateView
from django.utils.translation import gettext as _, get_language_bidi, get_language, get_language_info
from rest_framework.views import APIView
from rest_framework.response import Response
from dashboard.models import Payment
from rest_api.models import *
from .dashboard_mixins import *
from django.db import connection

User = get_user_model()

@login_required(login_url="accounts:login")
def get_data(request, *args, **kwargs):
    raw_data = get_net_revenue_by_month(request.user)
    # Top Six Raw
    top_six = get_top_product(request.user) # it is a list of dictionary
    theme_color = ['#f56954', '#00a65a', '#f39c12', '#00c0ef', '#3c8dbc', '#d2d6de']
    # compiled file of top six
    top_six_subtotal_name = [value['product_name'] for value in top_six['top_six_subtotal']]
    top_six_quantity_name = [value['product_name'] for value in top_six['top_six_quantity']]
    # top_six_stock = [value['stock_amount'] for value in top_six['top_six_subtotal']]
    top_six_subtotal = [value['product_subtotal'] for value in top_six['top_six_subtotal']]
    top_six_quantity = [value['sold_quantity'] for value in top_six['top_six_quantity']]
    top_six_color = [theme_color[value] for value in range(0, len(top_six_subtotal))]
    # Profit
    graph_labels = [key for key in raw_data['profit_data'].keys()]
    profit_graph_data = [value for value in raw_data['profit_data'].values()]
    # Net Revenue
    revenue_graph_data = [value for value in raw_data['revenue_data'].values()]
    # Expenses
    expense_graph_data = [value for value in raw_data['expense_data'].values()]
    data = {
        "top_six_color": top_six_color,
        "top_six_subtotal_name": top_six_subtotal_name,
        "top_six_quantity_name": top_six_quantity_name,
        # "top_six_stock": top_six_stock,
        "top_six_subtotal": top_six_subtotal,
        "top_six_quantity": top_six_quantity,
        "graph_labels": graph_labels,
        "profit_graph_data": profit_graph_data,
        "revenue_graph_data": revenue_graph_data,
        "expense_graph_data": expense_graph_data,
    }

    return JsonResponse(data)  # it is like http response


# class ChartData(APIView):
#     # this method has issues as it is rest api framework so it
#     # it requires token authentication to identify the user
#     authentication_classes = []
#     permission_classes = []

#     def get(self, request, format=None):
#         print('vlaue of user')
#         print(self.request.user)
#         raw_data = get_net_revenue_by_month(self.request.user)
#         labels = [key for key in raw_data.keys()]
#         # labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange', 'Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
#         graph_data = [value for value in raw_data.values()]
#         # graph_data = [12, 19, 3, 5, 2, 11, 12, 19, 3, 5, 2, 11]
#         data = {
#             "labels": labels,
#             "graph_data": graph_data,
#         }
#         return Response(data)

class DashboardHome(ListView):
    template_name = 'pos/user_dashboard/user_dashboard.html'
    # queryset = Product.objects.all().count() // this one is also correct

    def get_context_data(self, **kwargs):
        # it adds extra context to the list that you can access in template
        context = super().get_context_data(**kwargs)
        # context['now'] = datetime.datetime.today()
        context['today'] = datetime.today()
        context['session_no'] = get_session_no(self.request.user)
        context['order_no'] = get_monthly_order_no(self.request.user)
        context['return_no'] = get_monthly_return_no(self.request.user)
        context['monthly_net_revenue'] = get_monthly_net_revenue(
            self.request.user)
        context['monthly_expense'] = get_monthly_expense(self.request.user)
        context['daily_expense'] = get_daily_expense(self.request.user)
        context['annual_net_subtotal'] = get_annual_net_revenue(
            self.request.user)
        context['categories'] = Category.objects.filter(
            user=self.request.user).count()
        context['logs_no'] = Logs.objects.filter(
            user=self.request.user).count()
        context['notifications'] = Notification.objects.filter(
            user=self.request.user).count()
        context['invoices'] = Invoice.objects.unpaid().filter(
            user=self.request.user).count()
        return context

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user).aggregate(Count('name'))
        # return get_list_or_404(PosBackup) // it shows error when no data
        
class ClientProfile(DetailView):
    template_name = "pos/user_dashboard/client_profile.html"
    
    def get_object(self):
        return Payment.objects.filter(client=self.request.user)
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_client'] = self.request.user
        return context


class EnabledProductList(ListView):
    template_name = 'pos/product/enabled_product.html'
    # queryset = Product.objects.all()

    def get_queryset(self):
        return Product.objects.enabled().filter(user=self.request.user)


class ProductDetail(DetailView):
    template_name = 'pos/product/product_detail.html'

    def get_object(self):
        _id = self.kwargs.get('product_pk')
        return get_object_or_404(Product, product_pk=_id, user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_ = self.kwargs.get('product_pk')
        print("value of product product_pk")
        print(id_)
        context['variants'] = ProductVariantOption.objects.filter(
            product_id=id_, user=self.request.user)
        print(context['variants'])
        return context


class DisabledProductList(ListView):
    template_name = 'pos/product/disabled_product.html'
    # queryset = Product.objects.disabled()

    def get_queryset(self):
        return Product.objects.disabled().filter(user=self.request.user)


class OrderList(ListView):
    template_name = 'pos/order/order.html'
    queryset = PosOrder.objects.orders()

    def get_queryset(self):
        return PosOrder.objects.orders().filter(user=self.request.user)


class OrderDetail(DetailView):
    template_name = 'pos/order/order_detail.html'

    def get_object(self):
        id_ = self.kwargs.get('pos_order_pk')
        return get_object_or_404(PosOrder, pos_order_pk=id_, user=self.request.user)
        # return PosOrder.objects.get(pos_order_pk=id_, user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_ = self.kwargs.get('pos_order_pk')
        order_object = PosOrder.objects.get(
            user=self.request.user, pos_order_pk=id_)
        cart_id_temp = ShoppingCart.objects.get(
            user=self.request.user, shopping_cart_pk=order_object.cart_id)
        context['order_items'] = ShoppingCartProduct.objects.filter(
            user=self.request.user, shopping_cart_id=cart_id_temp.shopping_cart_pk)
        return context


class InvoiceList(ListView):
    template_name = 'pos/order/invoice.html'
    # queryset = Invoice.objects.unpaid()

    def get_queryset(self):
        return Invoice.objects.unpaid().filter(user=self.request.user)


class InvoiceDetail(DetailView):
    template_name = 'pos/order/invoice_detail.html'

    def get_object(self):
        id_ = self.kwargs.get('invoice_pk')
        return get_object_or_404(Invoice, invoice_pk=id_, user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_ = self.kwargs.get('invoice_pk')
        invoice_object = Invoice.objects.get(
            invoice_pk=id_, user=self.request.user)
        context['invoice_items'] = ShoppingCartProduct.objects.filter(
            shopping_cart_id=invoice_object.cart_id, user=self.request.user)
        context['user_info'] = self.request.user
        return context


class DailyExpenseList(ListView):
    template_name = 'pos/expense/daily_expense.html'
    # queryset = Expense.objects.daily()

    def get_queryset(self):
        return Expense.objects.daily().filter(user=self.request.user)


class MonthlyExpenseList(ListView):
    template_name = 'pos/expense/monthly_expense.html'
    # queryset = Expense.objects.monthly()

    def get_queryset(self):
        return Expense.objects.monthly().filter(user=self.request.user)


class SessionList(ListView):
    template_name = 'pos/session/all_session.html'
    # queryset = Session.objects.all()

    def get_queryset(self):
        return Session.objects.closed_session().filter(user=self.request.user)


class CurrentSession(DetailView):
    template_name = 'pos/session/current_session.html'

    def get_object(self):
        max_id = Session.objects.filter(
            user=self.request.user).aggregate(Max('session_pk'))
        return get_object_or_404(Session, session_pk=max_id['session_pk__max'], user=self.request.user)
        # return Session.objects.get(user=self.request.user, session_pk=max_id['session_pk__max'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        session_object = self.get_object()
        context['session_orders'] = PosOrder.objects.filter(
            session_id=session_object.session_pk, user=self.request.user)
        expense = Expense.objects.filter(
            expense_type="daily", session_id=session_object.session_pk, user=self.request.user).aggregate(Sum('amount'))
        if expense['amount__sum'] is None:
            context['session_daily_expense'] = 0.0
        else:
            context['session_daily_expense'] = expense['amount__sum']
        return context


class SessionDetail(DetailView):
    template_name = 'pos/session/session_detail.html'

    def get_object(self):
        _id = self.kwargs.get('session_pk')
        return get_object_or_404(Session, session_pk=_id, user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _id = self.kwargs.get('session_pk')
        context['session_orders'] = PosOrder.objects.filter(
            session_id=_id, user=self.request.user)
        expense = Expense.objects.filter(user=self.request.user, session_id=_id, expense_type="daily").aggregate(Sum('amount'))
        daily_expense = 0.0
        if expense['amount__sum']:
            daily_expense = expense['amount__sum']
        context['session_daily_expense'] = daily_expense
        return context


class MonthlyReturn(ListView):
    template_name = 'pos/return/monthly_return.html'
    # queryset = PosOrder.objects.monthly_return()

    def get_queryset(self):
        return PosOrder.objects.monthly_return().filter(user=self.request.user)


class AnnualReturn(ListView):
    template_name = 'pos/return/annual_return.html'
    # queryset = PosOrder.objects.annual_return()

    def get_queryset(self):
        return PosOrder.objects.annual_return().filter(user=self.request.user)


class ReturnDetail(DetailView):
    template_name = 'pos/return/return_detail.html'

    def get_object(self):
        _id = self.kwargs.get('pos_order_pk')
        return get_object_or_404(PosOrder, pos_order_pk=_id, user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_ = self.kwargs.get('pos_order_pk')
        order_object = PosOrder.objects.get(
            pos_order_pk=id_, user=self.request.user)
        context['return_items'] = ShoppingCartProduct.objects.filter(
            shopping_cart_id=order_object.cart_id, user=self.request.user)
        return context


class NotificationList(ListView):
    template_name = 'pos/more/notification.html'
    # queryset = Notification.objects.all()

    def get_queryset(self):
        return Notification.objects.all().filter(user=self.request.user)


class CategoryList(ListView):
    template_name = 'pos/more/category.html'
    # queryset = Category.objects.all()

    def get_queryset(self):
        return Category.objects.all().filter(user=self.request.user)


class VariantList(ListView):
    template_name = 'pos/more/variant.html'
    # queryset = Variant.objects.all()

    def get_queryset(self):
        return Variant.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['options'] = VariantOption.objects.filter(
            user=self.request.user)
        return context

class LogList(ListView):
    template_name = 'pos/logs/log_list.html'
    
    def get_queryset(self):
        return Logs.objects.filter(user=self.request.user)


class EditedProductDetail(DetailView):
    template_name = 'pos/logs/edited_product_detail.html'
    
    def get_object(self):
        _id = self.kwargs.get('log_pk')
        return get_object_or_404(Logs, log_pk=_id, user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _id = self.kwargs.get('log_pk')
        log_object = Logs.objects.filter(user=self.request.user, log_pk=_id).first()
        context['product_object'] = Product.objects.filter(user=self.request.user, product_pk=log_object.model_id)
        print('value of log_object')
        print(log_object.operation)
        context['edited_object'] = ProductLog.objects.filter(user=self.request.user, all_log_id=log_object.log_pk)
        return context
        

class DeletedProductDetail(DetailView):
    template_name = 'pos/logs/deleted_product_detail.html'
    
    def get_object(self):
        _id = self.kwargs.get('log_pk')
        return get_object_or_404(Logs, log_pk=_id, user=self.request.user)
    
    def get_context_data(self, **kwargs):
        print('i am inside the DeletedProductDetail')
        context = super().get_context_data(**kwargs)
        _id = self.kwargs.get('log_pk')
        log_object = Logs.objects.filter(user=self.request.user, log_pk=_id).first()
        print('value of log_object')
        print(log_object.operation)
        context['deleted_product'] = ProductLog.objects.filter(user=self.request.user, all_log_id=log_object.log_pk)
        return context


