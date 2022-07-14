from django.shortcuts import render
from django.views.generic import CreateView, View, DetailView, ListView, TemplateView


class PricingView(TemplateView):
    template_name = 'pricing/pricing_page.html'

