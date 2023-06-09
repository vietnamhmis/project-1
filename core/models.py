from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField

CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear'),
    ('co', 'Con Cún con')
)
LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),
    ('I', 'info'),
    ('W', 'warning'),
    ('S', 'success'),
    ('g', 'good')
)
ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


class Item(models.Model):
    title           = models.CharField(max_length=100)
    price           = models.FloatField()
    discount_price  = models.FloatField(blank=True, null=True)
    category        = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label           = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug            = models.SlugField()
    description     = models.TextField()
    image           = models.ImageField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })
    def get_add_to_cart_url(self):
        return reverse("core:add_to_cart", kwargs={
            'slug': self.slug
        })
    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })

class OrderItem(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered     = models.BooleanField(default=False)
    item        = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity    = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()



class Order(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ref_code        = models.CharField(max_length=20, blank=True, null=True)
    items           = models.ManyToManyField(OrderItem)
    start_date      = models.DateTimeField(auto_now_add=True)
    ordered_date    = models.DateTimeField()
    ordered         = models.BooleanField(default=False)

    billing_address = models.ForeignKey('BillingAddress', on_delete=models.SET_NULL, blank=True,null=True )
    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()

        return total


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username


class Address(models.Model):
    user                = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address      = models.CharField(max_length=100)
    apartment_address   = models.CharField(max_length=100)
    country             = CountryField(multiple=False)
    zip                 = models.CharField(max_length=100)
    address_type        = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default             = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name_plural = 'Addresses'


#------------------thử nghiệm smart---------------------https://www.youtube.com/watch?v=8VYx-cNF1lU&t=58s

from django.db import models

class City(models.Model):
    title = models.CharField(max_length=56)
    def __str__(self):
        return self.title

class Language(models.Model):
    title = models.CharField(max_length=56)

    def __str__(self):
        return self.title

class Entry(models.Model):
    name = models.CharField(max_length=124)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Favourite Language")
    citi = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name

#------------------KThúc thử nghiệm smart---------------------
#----------------------



