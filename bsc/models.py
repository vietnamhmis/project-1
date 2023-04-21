from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField
from mota_cv.models import Mota_Cv

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

)
ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


Tan_xuat = (
         ('tháng', 'Tháng'),
         ('qu', 'Quý'),
         ('na', 'Năm'),
          )
donvitinh = (
         ('dg', ' đồng'),
         ('kwx', 'kwh/tấn xi măng'),
         ('kwc', 'kcal/kg clanhke'),
         ('kwx', 'tr.đồng/người'),
         ('kwx', 'Tấn'),
         ('kwx', 'ngày'),
         ('kg', 'kg'),

         ('%', '%'),
          )

    #Ten_KPI         = models.CharField(max_length=500, blank=True, null=False)


class Item1(models.Model):
    title           = models.CharField(max_length=500)
    LoaiCV          = models.ForeignKey(Mota_Cv, null=True, on_delete= models.SET_NULL)
    Don_vi_tinh     = models.CharField(default="%",max_length=3, blank=False, null=True, choices= donvitinh)
    Tan_xuat_d_gia  = models.CharField(default="Tháng",max_length=20, blank=False, null=True, choices= Tan_xuat)
    Ti_trong        = models.DecimalField(default="20", max_digits=5, decimal_places=1)

    price           = models.FloatField()
    discount_price  = models.FloatField(blank=True, null=True)
    category        = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label           = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug            = models.SlugField()
    description     = models.TextField()
    image           = models.ImageField()

    def __str__(self):
        return self.title

    def get_trovekpi_url(self):
        return reverse("bsc:product1", kwargs={
            'slug': self.slug
        })
    def get_add_to_kpi_url(self):
        return reverse("bsc:add_to_kpi", kwargs={
            'slug': self.slug
        })
    def get_remove_from_kpi_url(self):
        return reverse("bsc:remove-from-kpi", kwargs={
            'slug': self.slug
        })


class OrderItem1(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered     = models.BooleanField(default=False)
    item        = models.ForeignKey(Item1, on_delete=models.CASCADE)
    quantity    = models.IntegerField(default=20)

    Chi_tieu    = models.IntegerField(default=1)
    Ket_qua    = models.IntegerField(default=1)



    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_titrong_kpi(self):
        return self.quantity

    def get_tile_hoan_thanh_kpi(self):
        return self.Ket_qua / self.Chi_tieu

    def get_diem_congviec_kpi(self):
        return self.Ket_qua * 1

    def get_diem_trongso_kpi(self):
        return self.get_diem_congviec_kpi() * self.quantity



class Order1(models.Model):
    user             = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ref_code        = models.CharField(max_length=20, blank=True, null=True)
    items           = models.ManyToManyField(OrderItem1)

    start_date      = models.DateTimeField(auto_now_add=True)
    ordered_date    = models.DateTimeField(auto_now_add=True)
    ordered         = models.BooleanField(default=False)
    billing_address = models.ForeignKey('Billingaddress1', related_name='Billingaddress1', on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.user.username

    def get_total(self):
        tong = 0
        for order_item1 in self.items.all():
            tong += order_item1.get_diem_trongso_kpi()
        return tong

    def get_total_titrong(self):
        total1 = 0
        for order_item1 in self.items.all():
            total1 += order_item1.get_titrong_kpi()
        return total1


class Billingaddress1(models.Model):
    user                = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address      = models.CharField(max_length=100)
    apartment_address   = models.CharField(max_length=100)
    country             = CountryField(multiple=False)
    zip                 = models.CharField(max_length=100)
   # address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
  #  default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username







