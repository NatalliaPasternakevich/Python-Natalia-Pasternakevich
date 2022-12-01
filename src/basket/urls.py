from django.urls import path
from . import views

app_name = 'basket'
urlpatterns = [
    path('order/', views.order_show, name='order-show'),

]