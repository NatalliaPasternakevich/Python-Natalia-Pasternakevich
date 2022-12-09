from django.views.generic.edit import FormView
from django.views.generic import ListView
from models import Customer
from . import forms
from django.contrib.auth.models import Group
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
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


class ProfileList(ListView):
    model = Customer
    template_name = 'accounts/profile_list.html'

    def get_context_data(self, *args, **kwargs):
        object_list = None
        current_user = User.objects.filter(username=self.request.user)
        if current_user:
            current_user = User.objects.get(username=self.request.user)
            object_list = \
                Customer.objects.filter(
                    Q(user_data__in=User.objects.filter(
                        Q(groups__name="Customers") &
                        ~Q(username=current_user))
                      ))
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        return context


class ProfileListCustomers(ListView):
    model = Customer
    template_name = 'accounts/profile_list_customers.html'

    def get_context_data(self, *args, **kwargs):
        object_list = User.objects.filter(Q(groups__name="Customers"))
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        return context



class ProfileListManagers(ListView):
    model = Customer
    template_name = 'accounts/profile_list_managers.html'

    def get_context_data(self, *args, **kwargs):
        object_list = User.objects.filter(Q(groups__name="Managers"))
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        return context
