from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)

class CheckoutForm(forms.Form):
    street_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'đường n9...'
    }))
    deparment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Phòng số..... '
    }))
    country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-50',
        }))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
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



#------------------thử nghiệm smart---------------------
from django import forms
from .models import City, Entry, Language


class EntryCreationForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = '__all__'

#   ---------------kế thúc Thử nghiệm smart---------------------