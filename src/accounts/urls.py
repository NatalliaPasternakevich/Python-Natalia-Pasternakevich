from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views
from django.urls import reverse_lazy


app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', next_page='home_page'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html', success_url=reverse_lazy('accounts:password_change_done')), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),

    path('registration/', user_views.Registration.as_view(), name='registration'),
    path('registration/fill', user_views.RegistrationFill.as_view(), name='registration_fill'),
    path('profile/list/', user_views.ProfileList.as_view(), name='profile_list'),
    path('profile/list/customers/<int:pk>', user_views.ProfileListCustomers.as_view(), name='profile_list_customers'),
    path('profile/list/managers/<int:pk>', user_views.ProfileListManagers.as_view(), name='profile_list_managers'),
]