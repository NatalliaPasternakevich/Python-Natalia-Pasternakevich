from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView, UpdateView, TemplateView
from django.contrib.auth.models import Group
from product_card.models import Book
# Create your views here.


class Homepage(TemplateView):
    template_name = 'home_page/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        books = Book.objects.all().order_by('-updated')[:10]
        context['object_list'] = books
        return context



   