from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from .models import Order1, OrderItem1

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)

class CheckoutForm(forms.Form):
    street_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'đường Võ Chí Công...',
        'class' : 'form-control',
    }))


    deparment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Phòng Nhân sự..... ',
        'class' : 'form-control',
    }))

    country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-50',
        }))

    zip = forms.CharField(widget=forms.TextInput(attrs={
         'placeholder': 'Zip..... ',
        'class': 'form-control  d-block w-40 ',
        'id':'zip'
    }))

    same_shipping_address = forms.BooleanField(required=False)

   # billing_address2 = forms.CharField(required=False)
    #billing_country = CountryField(blank_label='(select country)').formfield(
     #   required=False,
      #  widget=CountrySelectWidget(attrs={
       #     'class': 'custom-select d-block w-100',
     #   }))
   # billing_zip = forms.CharField(required=False)
  #  same_billing_address = forms.BooleanField(widget=forms.CheckboxInput())

    save_info = forms.BooleanField(widget=forms.CheckboxInput())

    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class Item1_form(forms.Form):
    class Meta:
     model = Order1
     fields = '__all__'

class OrderItem1_form(forms.Form):
    class Meta:
     model = OrderItem1
     fields = '__all__'

