from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

statuses = [
    ('created', 'Created'),
    ('in_process', 'In Process'),
    ('done', 'Processed and delivered'),
]


# Create your models here.

class Basket(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='baskets',
        blank=True, 
        null=True)

    def total_price(self):
        all_books = self.goodsinbaskets.all()
        total_price = 0
        for books in all_books:
            total_price += books.total_sum
        return total_price

class GoodsInBasket(models.Model):
    book = models.ForeignKey("product_card.Book", 
        on_delete=models.PROTECT, 
        verbose_name='Book in basket',
        )
    order = models.ForeignKey("basket.Basket", 
        on_delete=models.CASCADE, 
        related_name='goodsinbaskets')
    quantity = models.IntegerField(
        verbose_name="Quantity",
        default=1)
    price = models.DecimalField("price",
        decimal_places=2, 
        max_digits=5)
    created = models.DateField(
        "Created", 
        auto_now=False, 
        auto_now_add=True)
    updated = models.DateField(
        "Updated", 
        auto_now=True, 
        auto_now_add=False)
    
    @property
    def total_sum(self):
        return self.price * self.quantity

class Booking(models.Model):
    status = models.CharField(
        max_length=50,
        verbose_name= 'Stasuses',
        choices=statuses,
        default='created')
    basket = models.OneToOneField("basket.Basket",  
        on_delete=models.PROTECT, 
        related_name='booking')
    contact_phone = models.CharField(
        max_length=20)
    address = models.CharField( 
        max_length=20, 
        blank=True, null=True)
    created = models.DateField(
        "Created", 
        auto_now=False, 
        auto_now_add=True)
    updated = models.DateField(
        "Updated", 
        auto_now=True, 
        auto_now_add=False)
