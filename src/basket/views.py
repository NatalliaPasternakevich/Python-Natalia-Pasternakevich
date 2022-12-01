from django.views import  generic 
from django.shortcuts import render
from product_card import models as book_models
from . import models

# Create your views here.

def order_show(request):
    context = {}
    if request.method == "POST":
        book_pk = request.POST.get('book_pk')
        quantity = request.POST.get('quantity')
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
          if created:
            request.session['basket_id'] = basket.pk

          product_card = book_models.Book.objects.get(pk=int(book_pk))
          goods_in_basket = models.GoodsInBasket.objects.create(
                book=product_card,
                order=basket,
                quantity=quantity,
                price=product_card.price,
    
            )

    return render(
    request=request, 
    template_name = "basket/in_basket.html", 
    context=context)





# class InBasket(generic.TemplateView):
#     template_name = "basket/in_basket.html"