from django.shortcuts import render, redirect
from django.views.generic import FormView, View, DetailView, ListView, TemplateView, CreateView
from pos_management.mixins import NextUrlMixin, RequestFormAttachMixin
from .forms import LoginForm, RegisterForm
from django.contrib import messages


class LoginView(NextUrlMixin, RequestFormAttachMixin, FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'accounts/login_page.html'
    default_next = '/'

    def form_valid(self, form):
        next_path = self.get_next_url()
        return redirect(next_path)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register_page.html'
    success_url = '/accounts/login/'


