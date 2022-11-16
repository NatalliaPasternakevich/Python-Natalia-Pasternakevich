from django.shortcuts import render
from django.views import  generic 
from django.urls import reverse_lazy
from . import models, forms
# Create your views here.

class ShowBook(generic.ListView):
    model = models.Book
    template_name = 'product_card/list.html'


class CreateBook(generic.CreateView):
    model = models.Book
    form_class = forms.BookForm
    template_name = 'product_card/create.html'

    def get_success_url(self):
        return reverse_lazy('product_card:book-detail', kwargs={'pk': self.object.pk})


class ReadBook(generic.DetailView):
    model = models.Book
    template_name = 'product_card/read.html'
   
class UpdateBook(generic.UpdateView):
    model = models.Book
    form_class = forms.BookForm
    template_name = 'product_card/update.html'

    def get_success_url(self):
       return reverse_lazy('product_card:book-detail', kwargs={'pk': self.object.pk})


class DeleteBook(generic.DeleteView):
    model = models.Book
    template_name = 'product_card/delete.html'
    success_url = reverse_lazy('product_card:book-show')

