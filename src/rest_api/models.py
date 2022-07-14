from django.db import models
from django.contrib.auth import authenticate, login, get_user_model
import random
from django.urls import reverse, reverse_lazy
from django.db.models import Max, Sum
import os
from datetime import date
import time
import datetime

User = get_user_model()


# 1593093914.690711
# 1593093903.0186791
# def upload_product_image(instance, filename):
#     return "db/{user}/{filename}/".format(user=instance.user, filename=filename)


class Category(models.Model):
    category_pk = models.IntegerField()
    name = models.CharField(max_length=255)
    include_in_drawer = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)  # required
    backup_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name or ""
    # def __str__(self):
    #     if self.name==None:
    #          return "NAME IS NULL"
    #     return self.name


class Variant(models.Model):
    variant_pk = models.IntegerField()
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    backup_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name


class VariantOption(models.Model):
    variant_option_pk = models.IntegerField()
    option_name = models.CharField(max_length=255)
    variant_id = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    backup_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.option_name
    
    def variant_object(self):
        return Variant.objects.filter(variant_pk=self.variant_id, user=self.user).first()
    

class ProductQuerySet(models.query.QuerySet):
    def enabled(self):
        return self.filter(enable_product=True)
    
    def disabled(self):
        return self.filter(enable_product=False)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    
    def enabled(self):
        return self.get_queryset().all().enabled()
    
    def disabled(self):
        return self.get_queryset().disabled()


class Product(models.Model):
    product_pk = models.IntegerField()
    name = models.CharField(max_length=255, null=True, blank=True)
    alias = models.CharField(max_length=255, null=True, blank=True)
    purchase = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    picture = models.TextField(null=True, blank=True)
    barcode = models.CharField(max_length=255, null=True, blank=True)
    enable_product = models.BooleanField(default=False)
    quantity = models.IntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    has_variant = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    backup_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    objects = ProductManager()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("pos:product_detail", kwargs={"product_pk": self.product_pk})


class CategoryProduct(models.Model):
    category_product_pk = models.IntegerField()
    category_id = models.IntegerField(null=True, blank=True)
    product_id = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    backup_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return str(self.category_product_pk)


class VariantProduct(models.Model):
    variant_product_pk = models.IntegerField()
    variant_id = models.IntegerField(null=True, blank=True)
    product_id = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    backup_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return str(self.variant_product_pk)


class ProductVariantOption(models.Model):
    product_variant_option_pk = models.IntegerField()
    product_id = models.IntegerField(null=True, blank=True)
    variant_id = models.IntegerField(null=True, blank=True)
    option_id = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    backup_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.price)
    
    def variant_object(self):
        return Variant.objects.filter(variant_pk=self.variant_id, user=self.user).first()
    
    def variant_option_object(self):
        return VariantOption.objects.filter(variant_option_pk=self.option_id, user=self.user).first()

class ShoppingCart(models.Model):
    shopping_cart_pk = models.IntegerField()
    subtotal = models.FloatField(null=True, blank=True)
    cart_purchase_price_total = models.FloatField(null=True, blank=True)
    total_discount = models.FloatField(null=True, blank=True)
    cart_item_quantity = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    # timestamp = models.CharField(max_length=255, null=True, blank=True)
    checked_out = models.BooleanField(default=False)
    on_hold = models.BooleanField(default=False)
    return_order = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    backup_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.subtotal)
    
    # def casted_timestamp(self):
    #     return datetime.datetime.strptime(self.timestamp, "%Y-%m-%d %H:%M:%S.%f")

class ShoppingCartProduct(models.Model):
    shopping_cart_product_pk = models.IntegerField()
    product_quantity = models.IntegerField(null=True, blank=True)
    product_subtotal = models.FloatField(null=True, blank=True)
    product_discount = models.FloatField(null=True, blank=True)
    product_purchase_price_total = models.FloatField(null=True, blank=True)
    has_variant_option = models.BooleanField(default=False)
    product_id = models.IntegerField(null=True, blank=True)
    shopping_cart_id = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    backup_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.product_quantity)
    
    def product_object(self):
        return Product.objects.filter(user=self.user, product_pk=self.product_id).first()

class SessionQuerySet(models.query.QuerySet):
    
    def closed_session(self):
        return self.filter(close_status=True).order_by('-session_pk')

class SessionManager(models.Manager):
    def get_queryset(self):
        return SessionQuerySet(self.model, using=self._db)
        
    def closed_session(self):
        return self.get_queryset().closed_session()

class Session(models.Model):
    session_pk = models.IntegerField()
    opening_balance = models.FloatField(null=True, blank=True)
    opening_time = models.DateTimeField(blank=True, null=True)
    closing_time = models.DateTimeField(blank=True, null=True)
    session_comment = models.CharField(max_length=500, null=True, blank=True)
    close_status = models.BooleanField(default=False)
    drawer_status = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    backup_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    objects = SessionManager()

    def __str__(self):
        return str(self.opening_time)
    
    def closing_balance(self):
        subtotal = PosOrder.objects.filter(user=self.user, session_id=self.session_pk).aggregate(Sum('order_subtotal'))
        if subtotal['order_subtotal__sum']:
            return subtotal['order_subtotal__sum']
        else:
            return 0.0
    
    def order_no(self):
        num_order = PosOrder.objects.filter(user=self.user, session_id=self.session_pk).count()
        if num_order is not None:
            return num_order
        else:
            return 0
    
    def net_revenue(self):
        subtotal = PosOrder.objects.filter(user=self.user, session_id=self.session_pk).aggregate(Sum('order_subtotal'))
        expense = Expense.objects.filter(user=self.user, session_id=self.session_pk, expense_type="daily").aggregate(Sum('amount'))
        order_subtotal = 0.0
        daily_expense = 0.0
        if subtotal['order_subtotal__sum']:
            order_subtotal = subtotal['order_subtotal__sum']
        if expense['amount__sum']:
            daily_expense = expense['amount__sum']
        return order_subtotal - daily_expense
    
    def session_discount(self):
        discount = PosOrder.objects.filter(user=self.user, session_id=self.session_pk).aggregate(Sum('order_discount'))
        order_discount = 0.0
        if discount['order_discount__sum']:
            order_discount = discount['order_discount__sum']
        return order_discount
        
    
    def get_session_profit(self):
        subtotal = PosOrder.objects.filter(user=self.user, session_id=self.session_pk).aggregate(Sum('order_subtotal'), Sum('order_purchase_price_total'))
        expense = Expense.objects.filter(user=self.user, session_id=self.session_pk, expense_type="daily").aggregate(Sum('amount'))
        order_subtotal = 0.0
        order_purchase = 0.0
        daily_expense = 0.0
        if subtotal['order_subtotal__sum']:
            order_subtotal = subtotal['order_subtotal__sum']
        if subtotal['order_purchase_price_total__sum']:
            order_purchase = subtotal['order_purchase_price_total__sum']
        if expense['amount__sum']:
            daily_expense = expense['amount__sum']
        net_revenue_sum = order_subtotal - daily_expense
        return net_revenue_sum - order_purchase
    
    def session_daily_expense(self):
        expense = Expense.objects.filter(user=self.user, session_id=self.session_pk, expense_type="daily").aggregate(Sum('amount'))
        daily_expense = 0.0
        if expense['amount__sum']:
            daily_expense = expense['amount__sum']
        return expense
    
    def get_absolute_url(self):
        return reverse("pos:session_detail", kwargs={"session_pk": self.session_pk})
        


class PosOrderQuerySet(models.query.QuerySet):
    def orders(self):
        return self.filter(payment_completion_status=True, order_subtotal__gt=0).order_by('-pos_order_pk')
    
    def monthly_return(self):
        return self.filter(order_subtotal__lt=0).order_by('-pos_order_pk')
    
    def annual_return(self):
        return self.filter(order_subtotal__lt=0).order_by('-pos_order_pk')


class PosOrderManager(models.Manager):
    def get_queryset(self):
        return PosOrderQuerySet(self.model, using=self._db)
    
    def orders(self):
        return self.get_queryset().orders()
    
    def monthly_return(self):
        return self.get_queryset().monthly_return()
    
    def annual_return(self):
        return self.get_queryset().annual_return()

class PosOrder(models.Model):
    pos_order_pk = models.IntegerField()
    order_subtotal = models.FloatField(null=True, blank=True)
    order_purchase_price_total = models.FloatField(null=True, blank=True)
    order_discount = models.FloatField(null=True, blank=True)
    cash_collected = models.FloatField(null=True, blank=True)
    change_due = models.FloatField(null=True, blank=True)
    order_item_no = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    qr_code_string = models.CharField(max_length=255, null=True, blank=True)
    payment_completion_status = models.BooleanField(default=False)
    cart_id = models.IntegerField(null=True, blank=True)
    session_id = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    backup_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    objects = PosOrderManager()

    def __str__(self):
        return str(self.order_subtotal)
    
    def get_absolute_url(self):
        return reverse("pos:order_detail", kwargs={"pos_order_pk": self.pos_order_pk})
    
    def get_profit(self):
        if self.order_purchase_price_total is not None and self.order_subtotal is not None:
            return self.order_subtotal - self.order_purchase_price_total
        return 0.0
    
    def get_subtotal(self):
        subtotal = 0.0
        discount = 0.0
        result = 0.0
        if self.order_subtotal:
            subtotal = self.order_subtotal
        if self.order_discount:
            discount = self.order_discount
        if self.order_subtotal < 0:
            result = subtotal - discount
        else:
             result = subtotal + discount
        return result
    
    

class ExpenseManager(models.Manager):
    def daily(self):
        return self.get_queryset().filter(expense_type="daily")
    
    def monthly(self):
        return self.get_queryset().filter(expense_type="monthly")

class Expense(models.Model):
    expense_pk = models.IntegerField()
    expense_type = models.CharField(max_length=255, null=True, blank=True)
    reason = models.CharField(max_length=255, null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    session_id = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    backup_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    objects = ExpenseManager()

    def __str__(self):
        return str(self.expense_type)


class SelectedProductVariant(models.Model):
    selected_product_variant_pk = models.IntegerField()
    option_name = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    product_variant_option_id = models.IntegerField(null=True, blank=True)
    option_id = models.IntegerField(null=True, blank=True)
    variant_id = models.IntegerField(null=True, blank=True)
    product_id = models.IntegerField(null=True, blank=True)
    shopping_cart_id = models.IntegerField(null=True, blank=True)
    shopping_cart_product_id = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    backup_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.option_name)


class Barcode(models.Model):
    barcode_pk = models.IntegerField()
    name = models.CharField(max_length=255, null=True, blank=True)
    product_id = models.IntegerField(null=True, blank=True)
    barcode_text = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    backup_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.name)


class QrCode(models.Model):
    qr_code_pk = models.IntegerField()
    name = models.CharField(max_length=255, null=True, blank=True)
    qr_data = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    backup_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.name)

class InvoiceManager(models.Manager):
    def unpaid(self):
        return self.get_queryset().filter(invoice_paid_status=False).order_by('-invoice_pk')

class Invoice(models.Model):
    invoice_pk = models.IntegerField()
    invoice_subtotal = models.FloatField(null=True, blank=True)
    invoice_discount = models.FloatField(null=True, blank=True)
    invoice_paid_amount = models.FloatField(null=True, blank=True)
    invoice_payable_amount = models.FloatField(null=True, blank=True)
    invoice_item_no = models.IntegerField(null=True, blank=True)
    customer_name = models.CharField(null=True, blank=True, max_length=255)
    customer_address = models.CharField(null=True, blank=True, max_length=255)
    customer_phone = models.CharField(null=True, blank=True, max_length=255)
    customer_email = models.CharField(null=True, blank=True, max_length=255)
    qr_code_string = models.CharField(max_length=255)
    invoice_number = models.CharField(max_length=255)
    invoice_issue_date = models.CharField(max_length=255, null=True, blank=True)
    invoice_due_date = models.CharField(max_length=255, null=True, blank=True)
    # invoice_due_date = models.DateTimeField(blank=True, null=True)
    invoice_paid_status = models.BooleanField(default=False)
    cart_id = models.IntegerField(null=True, blank=True)
    session_id = models.IntegerField(null=True, blank=True)
    order_id = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    backup_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    objects = InvoiceManager()

    def __str__(self):
        return str(self.invoice_subtotal)
    
    def get_absolute_url(self):
        return reverse("pos:invoice_detail", kwargs={"invoice_pk": self.invoice_pk})


class Notification(models.Model):
    notification_pk = models.IntegerField()
    subject = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    detail_id = models.CharField(max_length=255, null=True, blank=True)
    note_type = models.CharField(max_length=255, null=True, blank=True)
    seen_status = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    backup_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.subject)


class Logs(models.Model):
    log_pk = models.IntegerField()
    operation = models.CharField(max_length=255, null=True, blank=True)
    detail = models.CharField(max_length=255, null=True, blank=True)
    model_id = models.IntegerField(null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    backup_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.detail)


class ProductLog(models.Model):
    product_log_pk = models.IntegerField()
    name = models.CharField(max_length=255, null=True, blank=True)
    purchase = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    barcode = models.CharField(max_length=255, null=True, blank=True)
    enable_product = models.BooleanField(default=False)
    quantity = models.IntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    all_log_id = models.IntegerField(null=True, blank=True)
    has_variant = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    backup_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.name)

    



