from django.shortcuts import render
from django.views.generic import CreateView, View, DetailView, ListView, TemplateView

# def blog_home(request):
#     return render(request, "blog/blog_home.html", {})



class BlogView(TemplateView):
    template_name = 'blog/blog_home.html'

