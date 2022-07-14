from django.shortcuts import redirect, render
from .forms import ContactForm
from django.views.generic import FormView, View, DetailView, ListView, TemplateView, CreateView
from django.utils import translation
from django.urls import path, reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
# from django.contrib import sessions


def home_page(request):
    return render(request, "home_page.html", {})


def feature_page(request):
    return render(request, "feature_page.html", {})

def change_language(request, *args, **kwargs):
    if request.method == "GET":
        # if translation.LANGUAGE_SESSION_KEY in request.session:
        #     del request.session[translation.LANGUAGE_SESSION_KEY]
        print('value of kwargs')
        print(kwargs.get('code'))
        lang_code = 'en-us'
        if kwargs.get('code') == 'en':
            lang_code = 'en-us'
        else:
            lang_code = kwargs.get('code')
        translation.activate(lang_code)
        request.session[translation.LANGUAGE_SESSION_KEY] = lang_code
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')



# def contact_page(request):
#     return render(request, "contact_page.html", {})


# def contact_page(request):
#     form = ContactForm(request.POST or None)
#     if request.method == "POST":
#         # name = request.POST.get('name')
#         # subject = request.POST.get('subject')
#         # email = request.POST.get('email')
#         # message = request.POST.get('content')
#
#         name = form.cleaned_data.get('name')
#         subject = form.cleaned_data.get('subject')
#         email = form.cleaned_data.get('email')
#         message = form.cleaned_data.get('content')
#
#         print(name)
#         print(subject)
#         print(email)
#         print(message)
#     else:
#         form = ContactForm()
#
#     return render(request, "contact_page.html", {'form': form})


class ContactView(View):
    template_name = 'contact_page.html'

    def get(self, request):
        form = ContactForm()
        data = {
            "form": form
        }
        return render(request, self.template_name, data)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            data = {
                "form": form
            }
            return render(request, self.template_name, data)


