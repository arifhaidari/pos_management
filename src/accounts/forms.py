from django import forms
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

User = get_user_model()

# from .models import EmailActivation, GuestEmail


# class ReactivateEmailForm(forms.Form):
#     email = forms.EmailField()
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         qs = EmailActivation.objects.email_exists(email)
#         if not qs.exists():
#             register_link = reverse("register")
#             msg = """This email does not exists, would you like to <a href="{link}">register</a>?
#             """.format(link=register_link)
#             raise forms.ValidationError(mark_safe(msg))
#         return email


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name', 'phone',) 

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserDetailChangeForm(forms.ModelForm):
    full_name = forms.CharField(label=_('Name'), required=False, widget=forms.TextInput(attrs={"class": 'form-control'}))

    class Meta:
        model = User
        fields = ['full_name']


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('full_name', 'phone', 'password', 'is_active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


# class GuestForm(forms.ModelForm):
#     # email    = forms.EmailField()
#     class Meta:
#         model = GuestEmail
#         fields = [
#             'email'
#         ]
#
#     def __init__(self, request, *args, **kwargs):
#         self.request = request
#         super(GuestForm, self).__init__(*args, **kwargs)
#
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         obj = super(GuestForm, self).save(commit=False)
#         if commit:
#             obj.save()
#             request = self.request
#             request.session['guest_email_id'] = obj.id
#         return obj


class LoginForm(forms.Form):
    phone = forms.CharField(label='Phone', widget=forms.TextInput(attrs={
        "placeholder": _("Username"),
        "class": "input100",
        "name": "phone",

    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": _("Password"),
        "class": "input100",
        "name": "password",
    }))

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        request = self.request
        data = self.cleaned_data
        phone = data.get("phone")
        password = data.get("password")
        qs = User.objects.filter(phone=phone)
        if qs.exists():
            # user phone is registered, check active/
            not_active = qs.filter(is_active=False)
            if not_active.exists():
                raise forms.ValidationError("This user is inactive.")
        user = authenticate(request, username=phone, password=password)
        if user is None:
            raise forms.ValidationError("Invalid credentials")
        login(request, user)
        self.user = user
        return data


class RegisterForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": _("Phone Number"),
        "class": "input100",
        "name": "phone",
    }))

    full_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": _("Full Name"),
        "class": "input100",
        "name": "full_name",
    }))

    business = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": _("Your Business (Shop, Supermarket...)"),
        "class": "input100",
        "name": "business",
    }))

    address = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": _("Address"),
        "class": "input100",
        "name": "address",
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": _("Password"),
        "class": "input100",
        "name": "password",
    }))

    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": _("Repeat Password"),
        "class": "input100",
        "name": "repeat_password",
    }))

    class Meta:
        model = User
        fields = ('phone', 'full_name', 'business', 'address',)

    def clean_repeat_password(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        repeat_password = self.cleaned_data.get("repeat_password")
        print(password)
        print(repeat_password)
        if password and repeat_password and password != repeat_password:
            raise forms.ValidationError("Passwords don't match")
        return repeat_password

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.plain_password = self.cleaned_data["password"]
        user.set_password(self.cleaned_data["password"])
        user.is_active = False
        if commit:
            user.save()
        return user


