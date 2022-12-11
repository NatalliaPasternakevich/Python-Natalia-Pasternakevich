from django.shortcuts import render
from django.views import  generic 
from django.urls import reverse_lazy
from . import models, forms
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.

User = get_user_model()

class ShowBook(generic.ListView):
    model = models.Book
    template_name = 'product_card/list.html'


class CreateBook(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'product_card.add_book'
    model = models.Book
    form_class = forms.BookForm
    template_name = 'product_card/create.html'

    def get_success_url(self):
        return reverse_lazy('product_card:book-detail', kwargs={'pk': self.object.pk})


class ReadBook(generic.DetailView):
    model = models.Book
    template_name = 'product_card/read.html'

   
class UpdateBook(PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'product_card.change_book'
    model = models.Book
    form_class = forms.BookForm
    template_name = 'product_card/update.html'

    def get_success_url(self):
       return reverse_lazy('product_card:book-detail', kwargs={'pk': self.object.pk})


class DeleteBook(PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'product_card.delete_book'
    model = models.Book
    template_name = 'product_card/delete.html'
    success_url = reverse_lazy('product_card:book-show')

