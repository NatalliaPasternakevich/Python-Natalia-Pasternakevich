from django.shortcuts import render
from django.views import  generic 
from django.urls import reverse_lazy
from . import models, forms
from product_card import models
# Create your views here.

class HomePage(generic.TemplateView):
    template_name = 'home_page/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['hp_img'] = models.Book.objects.get() 
        return context





    # model = models.HomePage
    # form_class = forms.HomePageForm
    # template_name = 'reference_book/all_read.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['refb_name'] = 'seria'
    #     context['refb_name_tab'] = 'Seria'
    #     context['refb_url'] = 'reference_book:seria-show'
    #     return context