from django import forms
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Payment

User = get_user_model()


class ClientForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Phone Number",
        "class": "form-control",
        "name": "phone",
    }))
    
    email = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Email",
        "class": "form-control",
        "name": "email",
    }))
    
    deal_amount = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Fee Amount",
        "class": "form-control",
        "name": "deal_amount",
    }))

    full_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Full Name",
        "class": "form-control",
        "name": "full_name",
    }))

    business = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your Business (Shop, Pharmacy...)",
        "class": "form-control",
        "name": "business",
    }))

    address = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Address",
        "class": "form-control",
        "name": "address",
    }))
    
    deal_amount = forms.CharField(required=False ,widget=forms.TextInput(attrs={
        "placeholder": "Payable Amount",
        "class": "form-control",
        "name": "deal_amount",
    }))

    start_contract_at = forms.DateField(required=False, widget=forms.DateInput(attrs={
        "class": "form-control",
        "name": "start_contract_at",
        "type": "date"
    }))

    end_contract_at = forms.DateField(required=False, widget=forms.DateInput(attrs={
        "class": "form-control",
        "name": "end_contract_at",
        "type": "date"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Password",
        "class": "form-control",
        "name": "password",
    }))

    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Repeat Password",
        "class": "form-control",
        "name": "repeat_password",
    }))

    is_active = forms.BooleanField(
        initial=False, required=False, label="Activate")

    # is_active = forms.BooleanField(initial=False, label="Activate", widget=forms.CheckboxInput(attrs={
    #     "class": "form-check-input",
    #     "name": "is_active",
    # }))

    class Meta:
        model = User
        fields = ('phone', 'full_name', 'email', 'plain_password', 'business', 'address', 'deal_amount',
                  'start_contract_at', 'end_contract_at', 'is_active')

    def clean_repeat_password(self):
             # Check that the two password entries match
        password = self.cleaned_data.get("password")
        name = self.cleaned_data.get("full_name")
        active = self.cleaned_data.get("is_active")
        repeat_password = self.cleaned_data.get("repeat_password")
        if password and repeat_password and password != repeat_password:
            raise forms.ValidationError("Passwords don't match")
        return repeat_password

    def save(self, commit=True):
        # Save the provided password in hashed format
        # print('inside the save')
        # print('////////////')
        # print(self.cleaned_data)
        user = super(ClientForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.plain_password = self.cleaned_data["password"]
        # user.is_active = True
        if commit:
            user.save()
            # print("saved ............")
        return user


class ClientUpdateForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Phone Number",
        "class": "form-control",
        "name": "phone",
    }))
    
    email = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Email",
        "class": "form-control",
        "name": "email",
    }))
    
    deal_amount = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Fee Amount",
        "class": "form-control",
        "name": "deal_amount",
    }))

    full_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Full Name",
        "class": "form-control",
        "name": "full_name",
    }))

    business = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your Business (Shop, Pharmacy...)",
        "class": "form-control",
        "name": "business",
    }))

    address = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Address",
        "class": "form-control",
        "name": "address",
    }))
    
    deal_amount = forms.CharField(required=False ,widget=forms.TextInput(attrs={
        "placeholder": "Payable Amount",
        "class": "form-control",
        "name": "deal_amount",
    }))

    start_contract_at = forms.DateField(required=False ,widget=forms.DateInput(attrs={
        "class": "form-control",
        "name": "start_contract_at",
        "type": "date"
    }))

    end_contract_at = forms.DateField(required=False ,widget=forms.DateInput(attrs={
        "class": "form-control",
        "name": "end_contract_at",
        "type": "date"
    }))
    
    is_active = forms.BooleanField(initial=False, required=False, label="Activate")


    class Meta:
        model = User
        fields = ('phone', 'email', 'full_name', 'business', 'address', 'deal_amount', 
                  'start_contract_at', 'end_contract_at', 'is_active')
    
    # def clean(self):
    #     cleaned_data = super(ClientUpdateForm, self).clean()
        # print(cleaned_data.values)
        # print(cleaned_data.get('full_name'))


class ActivateClientForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('phone','is_active')

# address = forms.CharField(widget=forms.TextInput(attrs={
#         "placeholder": "Address",
#         "class": "form-control",
#         "name": "address",
#     }))
    
class PaymentForm(forms.ModelForm):
    paid_amount = forms.CharField(required=False ,widget=forms.TextInput(attrs={
        "placeholder": "Enter Amount",
        "class": "form-control",
        "name": "paid_amount"
    }))
    
    # status = forms.BooleanField(required=False)
    # remaining = forms.CharField(required=False)
    # amount = forms.CharField(required=False)
    # paid_date = forms.DateField(required=False)
    # start_contract_date = forms.DateField(required=False)
    # end_contract_date = forms.DateField(required=False)
    
    class Meta:
        model = Payment
        fields = ('paid_amount', )

