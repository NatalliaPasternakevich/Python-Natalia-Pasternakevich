from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from . import models 
from . import forms
from django.http import Http404
from django.contrib.auth.models import Group
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q


# Create your views here.

User = get_user_model()

class Registration(FormView):
    model = User
    form_class = forms.UserForm
    template_name = 'accounts/registration.html'
    def form_valid(self, form):
        new_user = form.save()
        new_user.groups.add(Group.objects.get(name='Customers').pk)
        if self.request.user is not None:
            update_session_auth_hash(self.request, self.request.user)
            auth_logout(self.request)
        auth_login(self.request, new_user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('accounts:registration_fill')


class RegistrationFill(CreateView):
    model = models.Customer
    form_class = forms.CustomerForm
    template_name = 'accounts/registration_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('accounts:profile_list')





class ProfileList(DetailView):
    model = User
    template_name = 'accounts/profile_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username=self.request.user)
        models.Customer.objects.get_or_create(
            user=user,
            defaults={
                'phone': '',
                'country': '',
                'city': '',
                'zip_code': '',
                'address1': '',
                'address2': '',
                'information': '',
            }
        )
        return context

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        if self.kwargs.get("pk") is None:
            userid = request.user.id
            if userid is not None:
                self.kwargs["pk"] = userid
            else:
                raise Http404("Error")



class ProfileListCustomers(ListView):
    model = models.Customer
    template_name = 'accounts/profile_list_customers.html'

    def get_context_data(self, *args, **kwargs):
        object_list = User.objects.filter(Q(groups__name="Customers"))
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        return context



class ProfileListManagers(ListView):
    model = models.Customer
    template_name = 'accounts/profile_list_managers.html'

    def get_context_data(self, *args, **kwargs):
        object_list = User.objects.filter(Q(groups__name="Managers"))
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        return context
