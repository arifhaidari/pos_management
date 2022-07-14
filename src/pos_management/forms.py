from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

User = get_user_model()


class ContactForm(forms.Form):
    name = forms.CharField(
            widget=forms.TextInput(
                    attrs={
                        "placeholder": _("Enter Your Name"),
                        "class": "form-control",
                        "name": "name",
                        "id": "name",
                        "onblur": "this.placeholder = 'Enter Your Name'",
                        "onfocus": "this.placeholder = ''",
                    }
                    )
            )

    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": _("Enter Subject"),
                "class": "form-control",
                "name": "subject",
                "id": "subject",
                "onblur": "this.placeholder = 'Enter Subject'",
                "onfocus": "this.placeholder = ''",
            }
        )
    )

    email    = forms.EmailField(
            widget=forms.EmailInput(
                    attrs={
                        "placeholder": _("Enter Email Address"),
                        "class": "form-control",
                        "name": "email",
                        "id": "email",
                        "onblur": "this.placeholder = 'Enter Email Address'",
                        "onfocus": "this.placeholder = ''",
                    }
                    )
            )
    message  = forms.CharField(
            widget=forms.Textarea(
                attrs={
                    "placeholder": _("Enter Message"),
                    "class": "form-control w-100",
                    "name": "message",
                    "id": "message",
                    "cols": "30",
                    "rows": "9",
                    "onblur": "this.placeholder = 'Enter Message'",
                    "onfocus": "this.placeholder = ''",

                    }
                )
            )

