from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.
from django.views.generic import ListView, DetailView, View

from .forms import CheckoutForm, CouponForm
from .models import Item, OrderItem, Order, Address, BillingAddress
from django.utils.encoding import force_str

class HomeView(ListView):
    model = Item
    paginate_by = 4
    template_name = "core/home_core.html"
    # VIẾT : object_list



class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            ga = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object_ga': ga
            }
            return render(self.request, 'core/order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "Bạn chưa chọn mua hàng")
            return redirect("/")


class ItemDetailView(DetailView):
    model = Item
    paginate_by = 10
    template_name = "core/product.html"
    #có thể viết objects, HOẶC ,Moldel

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order https://www.youtube.com/watch?v=YZvRrldjf1Y PHÚT 34
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Số lượng món hàng được tăng")
            return redirect("core:order-summary")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart/Món hàng này bạn vừa thêm vào giỏ hàng của bạn")

            return redirect("core:order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart/Món hàng này bạn vừa thêm vào giỏ hàng của bạn")
        return redirect("core:order-summary")


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            #order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "Món hàng này được loại khỏi gỏ hàng của bạn cart.")
            return redirect("core:product", slug=slug)
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:product", slug=slug)
def checkout(request):
    return render(request, "checkout.html")


@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("core:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:product", slug=slug)



class CheckoutView(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            form = CheckoutForm()
            context = {
                'form': form,
                'couponform': CouponForm(),
                'order': order,
                'DISPLAY_COUPON_FORM': True
            }
#---------------chua--------<
            shipping_address_qs = Address.objects.filter(
                user=self.request.user,
                address_type='S',
                default=True
            )
            if shipping_address_qs.exists():
                context.update(
                    {'default_shipping_address': shipping_address_qs[0]})

            billing_address_qs = Address.objects.filter(
                user=self.request.user,
                address_type='B',
                default=True
            )
            if billing_address_qs.exists():
                context.update(
                    {'default_billing_address': billing_address_qs[0]})
           # return render(self.request, "core/check_thu.html", context)
            return render(self.request, "core/checkout.html", context)

        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
#Chưa--------------------->
            return redirect("core:checkout")


def post(self, *args, **kwargs):
    form = CheckoutForm(self.request.POST or None)
    try:
        order = Order.objects.get(user=self.request.user, ordered=False)
        if form.is_valid():
            street_address = form.cleaned_data.get('street_address')
            deparment_address = form.cleaned_data.get('deparment_address')
            country = form.cleaned_data.get('country')
            zip = form.cleaned_data.get('zip')
            #same_shipping_address =  form.cleaned_data.get('same_shipping_address')
           # save_info =  form.cleaned_data.get('save_info')
            payment_option =  form.cleaned_data.get('payment_option')
            billing_address =BillingAddress(
                user=self.request.user,
                street_address = street_address,
                deparment_address = deparment_address,
                country =country,
                zip =zip,
            )
            billing_address.save()
            order.billing_address=billing_address
            order.save()
            return redirect('core:checkout')
        messages.warning(self.request,"Failed checkout")
        return redirect('core:checkout')
    except ObjectDoesNotExist:
        messages.warning(self.request, "Bạn chưa chọn mua hàng")
        return redirect("core:checkout")













#------------------thử nghiệm smart---------------------##https://www.youtube.com/watch?v=8VYx-cNF1lU
import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import EntryCreationForm
from .models import Entry, Language, City


def home_select(request):
    form = EntryCreationForm()
    if request.is_ajax():
        term = request.GET.get('term')
        term_citi = request.GET.get('term_citi')
        languages = Language.objects.all().filter(title__icontains=term)

        citi = City.objects.all().filter(title__icontains=term_citi)
        return JsonResponse(list(languages.values(),citi.values()), safe=False)
    if request.method == 'POST':
        form = EntryCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_select')
    return render(request, 'core/home.html', {'form': form})

#------------------KThúc thử nghiệm smart---------------------
