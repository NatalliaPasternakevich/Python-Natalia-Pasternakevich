from django.urls import path
from django.urls import reverse_lazy
from . import views 

app_name = 'basket'
urlpatterns = [
    path('order/', views.order_show, name='order-show'),
    path('goodsinbasket-delete/<int:pk>', views.DeleteGoodsInBasket.as_view(), name='goodsinbasket-delete'),
    path('booking-create/', views.Booking.as_view(), name='booking-create'),
    path('success/', views.OrderCompleteDone.as_view(), name='success-basket'),
]