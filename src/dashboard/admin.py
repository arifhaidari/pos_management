from django.contrib import admin
from .models import Payment

class AdminPayment(admin.ModelAdmin):
     model = Payment
     list_display = ('client', 'amount', 'paid_amount', 'paid_date', 'start_contract_date', 'end_contract_date')
     search_fields = ('end_contract_date', 'paid_date', 'client')


admin.site.register(Payment, AdminPayment)
