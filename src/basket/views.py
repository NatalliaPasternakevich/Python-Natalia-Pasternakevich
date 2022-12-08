from django.views import  generic 
from django.views.generic import DeleteView, CreateView, TemplateView
from django.shortcuts import render
from django.urls import reverse_lazy
from product_card import models as book_models
from . import models, forms

# Create your views here.
class DeleteGoodsInBasket(DeleteView):
   model = models.GoodsInBasket
   template_name = "basket/delete_in_basket.html"
   success_url = reverse_lazy('basket:order-show')

   def get_context_data(self, *args, **kwargs):
      context = super().get_context_data(*args, **kwargs)
      return context
   
   
def order_show(request):
   context = {}
   context['basket'] = None
   if request.method == "POST":
      book_pk = request.POST.get('book_pk')
      quantity = int(request.POST.get('quantity'))
      if book_pk and quantity:
         basket_id = int(request.session.get('basket_id', 0))
         if request.user.is_authenticated:
            user = request.user
         else:
            user = None
         if basket_id == 0:
            basket_id = None
         basket, created = models.Basket.objects.get_or_create(
            pk=basket_id,
            defaults={'user': user}
            )
         context['basket'] = basket
         if created:
            request.session['basket_id'] = basket.pk

         product_card = book_models.Book.objects.get(pk=int(book_pk))
         goods_in_basket, created = models.GoodsInBasket.objects.get_or_create(
            book=product_card,
            order=basket,
            defaults={
               'quantity': quantity,
               'price': product_card.price 
               })
         if not created:
            goods_in_basket.quantity = goods_in_basket.quantity + quantity
            goods_in_basket.save()     
   else:
      basket_id = request.session.get('basket_id')
      if basket_id:
         basket = models.Basket.objects.get(pk=basket_id)
         context['basket'] = basket

   context['form'] = forms.BookingForm()    
   return render(request=request, template_name = "basket/in_basket.html", context=context)

class Booking(CreateView):
      model = models.Booking
      form_class = forms.BookingForm
      success_url = reverse_lazy('basket:success-basket')
      template_name = "basket/create_in_basket.html"
      def form_valid(self, form):
         basket = models.Basket.objects.get(pk=self.request.session.get('basket_id') )
         form.instance.basket = basket
         return super().form_valid(form)

      def get_success_url(self) -> str:
         del self.request.session['basket_id']
         return super().get_success_url()

class OrderCompleteDone(TemplateView):
   template_name = "basket/success_in_basket.html"