from django.shortcuts import render
from django.http import HttpResponse
from django.views import  generic 
from django.urls import reverse_lazy
from . import models, forms
# Create your views here.



# Авторы
class ShowAuthors(generic.ListView):
    model = models.Author
    template_name = 'reference_book/list.html'

   


class CreateAuthor(generic.CreateView):
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'reference_book/create.html'

    def get_success_url(self):
        return reverse_lazy('reference_book:author-detail', kwargs={'pk': self.object.pk})


class ReadAuthor(generic.DetailView):
    model = models.Author
    template_name = 'reference_book/read.html'
   
class UpdateAuthor(generic.UpdateView):
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'reference_book/update.html'

    def get_success_url(self):
       return reverse_lazy('reference_book:author-detail', kwargs={'pk': self.object.pk})


class DeleteAuthor(generic.DeleteView):
    model = models.Author
    template_name = 'reference_book/delete.html'
    success_url = reverse_lazy('reference_book:author-show')


# Серия 
class ShowSeria(generic.ListView):
    model = models.Seria
    template_name = 'reference_book/all_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['refb_name'] = 'seria'
        context['refb_url_update'] = 'reference_book:seria-update'
        context['refb_url_delete'] = 'reference_book:seria-delete'
        context['refb_url_create'] = 'reference_book:seria-create'
        return context


class CreateSeria(generic.CreateView):
    model = models.Seria
    form_class = forms.SeriaForm
    template_name = 'reference_book/all_create.html'

    def get_success_url(self):
        return reverse_lazy('reference_book:seria-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['refb_name'] = 'seria'
        return context

class ReadSeria(generic.DetailView):
    model = models.Seria
    template_name = 'reference_book/all_read.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['refb_name'] = 'seria'
        context['refb_name_tab'] = 'Seria'
        context['refb_url'] = 'reference_book:seria-show'
        return context

   
class UpdateSeria(generic.UpdateView):
    model = models.Seria
    form_class = forms.SeriaForm
    template_name = 'reference_book/all_update.html'

    def get_success_url(self):
        return reverse_lazy('reference_book:seria-detail', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['refb_name'] = 'seria'
        return context

class DeleteSeria(generic.DeleteView):
    model = models.Seria
    template_name = 'reference_book/all_delete.html'
    success_url = reverse_lazy('reference_book:seria-show')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['refb_name'] = 'seria'
        context['refb_name_tab'] = 'Seria'
        return context


# Жанр 
class ShowGenre(generic.ListView):
    model = models.Genre
    template_name = 'reference_book/all_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['refb_name'] = 'genre'
        context['refb_url_update'] = 'reference_book:genre-update'
        context['refb_url_delete'] = 'reference_book:genre-delete'
        context['refb_url_create'] = 'reference_book:genre-create'
        return context


class CreateGenre(generic.CreateView):
    model = models.Genre
    form_class = forms.GenreForm
    template_name = 'reference_book/all_create.html'

    def get_success_url(self):
        return reverse_lazy('reference_book:genre-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['refb_name'] = 'genre'
        return context

class ReadGenre(generic.DetailView):
    model = models.Genre
    template_name = 'reference_book/all_read.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['refb_name'] = 'genre'
        context['refb_name_tab'] = 'Genre'
        context['refb_url'] = 'reference_book:genre-show'
        return context

   
class UpdateGenre(generic.UpdateView):
    model = models.Genre
    form_class = forms.GenreForm
    template_name = 'reference_book/all_update.html'

    def get_success_url(self):
        return reverse_lazy('reference_book:genre-detail', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['refb_name'] = 'genre'
        return context

class DeleteGenre(generic.DeleteView):
    model = models.Genre
    template_name = 'reference_book/all_delete.html'
    success_url = reverse_lazy('reference_book:genre-show')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['refb_name'] = 'genre'
        context['refb_name_tab'] = 'Genre'
        return context


# Издательство 
class ShowPublisher(generic.ListView):
    model = models.Publisher
    template_name = 'reference_book/all_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['refb_name'] = 'publisher'
        context['refb_url_update'] = 'reference_book:publisher-update'
        context['refb_url_delete'] = 'reference_book:publisher-delete'
        context['refb_url_create'] = 'reference_book:publisher-create'
        return context



class CreatePublisher(generic.CreateView):
    model = models.Publisher
    form_class = forms.PublisherForm
    template_name = 'reference_book/all_create.html'

    def get_success_url(self):
        return reverse_lazy('reference_book:publisher-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['refb_name'] = 'publisher'
        return context

class ReadPublisher(generic.DetailView):
    model = models.Publisher
    template_name = 'reference_book/all_read.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['refb_name'] = 'publisher'
        context['refb_name_tab'] = 'Publisher'
        context['refb_url'] = 'reference_book:publisher-show'
        return context

   
class UpdatePublisher(generic.UpdateView):
    model = models.Publisher
    form_class = forms.PublisherForm
    template_name = 'reference_book/all_update.html'

    def get_success_url(self):
        return reverse_lazy('reference_book:publisher-detail', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['refb_name'] = 'publisher'
        return context

class DeletePublisher(generic.DeleteView):
    model = models.Publisher
    template_name = 'reference_book/all_delete.html'
    success_url = reverse_lazy('reference_book:publisher-show')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['refb_name'] = 'publisher'
        context['refb_name_tab'] = 'Publisher'
        return context
