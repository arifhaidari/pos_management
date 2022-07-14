from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
import datetime
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import path, reverse_lazy, reverse
from .forms import ClientForm, ClientUpdateForm, ActivateClientForm, PaymentForm
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView, TemplateView
from .models import Payment
from django.shortcuts import HttpResponseRedirect
from datetime import date
from django.utils.translation import gettext as _


User = get_user_model()

class DashboardMenue(TemplateView):
    template_name = 'dashboard/dashboard_home.html'
  

class ClientDetail(DetailView):
    template_name = 'dashboard/client_detail.html'
    
    def get_object(self):
        #check if user contract is date is expired 
        #or equal or greater than current date then create 
        # a payment record for it 
        # Also extend the using of app by one week if goes further 
        # then deactive the user automaticatlly by system 
        id_ = self.kwargs.get("id")
        return get_object_or_404(User, id=id_)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # user = self.get_object()
        user = self.kwargs.get('id')
        context['payment_object_list'] = Payment.objects.filter(client__id=user)
        context['payment_form'] = PaymentForm
        context['current_client'] = User.objects.get(id=user)
        return context

class CreateClient(CreateView):
    template_name = 'dashboard/add_client.html'
    form_class = ClientForm
    success_url = reverse_lazy('dashboard:list')
    
    def form_valid(self, form):
        # print("inside the create class")
        # print(form.cleaned_data.get('full_name'))
        # print(self.request)
        # print('///////////////')
        # print(self.request.user)
        messages.success(self.request, "successfully added")
        return super().form_valid(form)
    
    # def get_success_url(self):
    #     return reverse_lazy('pos:pos_home')


class ClientList(ListView):
    model = User
    template_name = 'dashboard/client_list.html'
    paginate_by = 9
    # queryset = User.objects.all()
    
    def get_queryset(self):
        # return User.objects.all().order_by("-timestamp")
        return User.objects.exclude(admin=True).order_by("-timestamp")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.datetime.today()
        return context
    

class UpdateClient(UpdateView):
    template_name = 'dashboard/update_client.html'
    form_class = ClientUpdateForm
    # success_url = reverse_lazy('dashboard:list')
    model = User
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(User, id=id_)
    
    def form_valid(self, form):
        client = User.objects.get(id = self.kwargs.get('id'))
        model = form.save(commit=False)
        if not form.cleaned_data.get('start_contract_at'):
            model.start_contract_at = client.start_contract_at
        if form.cleaned_data.get('end_contract_at') == None:
            model.end_contract_at = client.end_contract_at
        model.save()
        messages.success(self.request, "Successfully Upadated") 
        return super().form_valid(form)
    
    def get_success_url(self):
        id_ = self.kwargs.get('id')
        return f'/dashboard/detail/{id_}'
    

class ActivateClient(UpdateView):
    template_name = 'dashboard/activate_client.html'
    form_class = ActivateClientForm
    # success_url = reverse_lazy('dashboard:list')
    model = User
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        print('inside the getting object')
        return get_object_or_404(User, id=id_)
    
    def form_valid(self, form):
        print('inside form valid')
        client = User.objects.get(id = self.kwargs.get('id'))
        model = form.save(commit=False)
        if client.is_active == False:
            model.is_active = True
        if client.is_active:
            model.is_active = False
        model.save()
        if client.is_active:
            messages.success(self.request, "Successfully Deactivated")
        if not client.is_active:
            messages.success(self.request, "Successfully Activated")
        return super().form_valid(form)
    
    def get_success_url(self):
        id_ = self.kwargs.get('id')
        return f'/dashboard/detail/{id_}'
        # return HttpResponseRedirect(client.get_absolute_url)


class DeleteClient(DeleteView):
    template_name = 'dashboard/delete_client.html'
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(User, id=id_)
    
    def get_success_url(self):
        messages.success(self.request, "Successfully Deleted")
        return reverse('dashboard:list')

################## Payment Part #######

class PaymentList(ListView):
    template_name = 'dashboard/payment/payment_list.html'
    queryset = Payment.objects.filter(status=True).order_by("-id")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['complete_payment_no'] = Payment.objects.filter(status=True).count()
        context['incomplete_payment_no'] = Payment.objects.filter(status=False).count()
        context['deactivated_user'] = User.objects.filter(is_active=False).count()
        context['activated_user'] = User.objects.filter(is_active=True).count()
        context['incomplete'] = Payment.objects.filter(status=False).order_by("-id")
        return context
        


class UpdatePayment(UpdateView):
    template_name = 'dashboard/payment/update_payment.html'
    form_class = PaymentForm
    model = Payment
    success_url = reverse_lazy("dashboard:list")
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Payment, id=id_)
    
    def form_valid(self, form):
        # print("inside the form valid")
        payment_object = Payment.objects.get(id=self.kwargs.get("id"))
        # print("payment_object value")
        # print(payment_object.client)
        # print(payment_object.amount)
        entered_amount = form.cleaned_data.get("paid_amount")
        print(entered_amount)
        model = form.save(commit=False)
        if float(entered_amount) >= payment_object.amount:
            print("inside the if")
            model.status = True
            model.paid_amount = float(entered_amount)
            # model.paid_date = date.today()
        else:
            # print("insid the else")
            model.status = False
            model.paid_amount = float(entered_amount)
        model.save()
        # payment_object.save()
        return super().form_valid(form)

    
class DeletePayment(DeleteView):
    template_name = 'dashboard/payment/delete_payment.html'
    # success_url = reverse_lazy("dashboard:list")
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Payment, id=id_)
    
    def get_success_url(self):
        return reverse_lazy("dashboard:list")
    
@login_required(login_url="accounts:login")
def payment_form_organizer(request):
    current_client_id = ''
    if request.method == "POST":
        paid_amount = request.POST.get('paid_amount')
        current_client_id = request.POST.get('current_client_id')
        client_object = User.objects.get(id=current_client_id)
        payment_status = False
        if float(paid_amount) >= float(client_object.deal_amount):
            payment_status = True
        
        payment_object = Payment.objects.create(
            client = client_object, paid_amount=float(paid_amount),
            amount=client_object.deal_amount, status=payment_status, start_contract_date=client_object.start_contract_at, 
            end_contract_date=client_object.end_contract_at, paid_date=date.today())
        # print(date)
        # print(paid_amount)
        payment_object.save()
        # print(current_client_id)
        return redirect(f'/dashboard/detail/{current_client_id}')
    else:
        return redirect(f'/dashboard/')

    return render(request, 'dashboard/client_detail.html', {})



