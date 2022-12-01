from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Basket(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='baskets',
        blank=True, 
        null=True

    )

class GoodsInBasket(models.Model):
    book = models.ForeignKey("product_card.Book", 
          on_delete=models.PROTECT, 
          verbose_name='Book in basket')
    order = models.ForeignKey("basket.Basket", 
          on_delete=models.CASCADE, 
          related_name='goodsinbaskets')
    quantity = models.IntegerField(
          verbose_name="Quantity",
          default=1
          )
    price = models.DecimalField("price",
            decimal_places=2, 
            max_digits=5
            )
    created = models.DateField(
        "Created", 
        auto_now=False, 
        auto_now_add=True
        )
    updated = models.DateField(
        "Updated", 
        auto_now=True, 
        auto_now_add=False
        )