from django.shortcuts import render
from django.http import HttpResponse
from django.views import  generic 

# Create your views here.
from . import models, forms

class ShowAuthors(generic.ListView):
    model = models.Author
    template_name = 'reference_book/list.html'


class ShowAuthor(generic.DetailView):
    model = models.Author
    template_name = 'reference_book/deteil.html'

class CreateAuthor(generic.CreateView):
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'reference_book/create.html'
   
class UpdateAuthor(generic.UpdateView):
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'reference_book/update.html'


class DeleteAuthor(generic.DeleteView):
    model = models.Author
    template_name = 'reference_book/delete.html'
