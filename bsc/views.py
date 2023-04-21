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

from .forms import CheckoutForm, CouponForm, OrderItem1_form
from .models import *
from django.utils.encoding import force_str




class HomeView(ListView):
    model = Item1
    paginate_by = 4
    template_name = "bsc/home.html"

def danhmuc_KPI(request):
    queryset = Item1.objects.all()[1:50]
    context = {'queryset': queryset,}
    return render(request,'bsc/home.html', context)


class OrderSummaryView1(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            ga = Order1.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': ga
            }
            return render(self.request, 'bsc/order_summary1.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "Bạn chưa chọn KPI")
            return redirect("bsc/")




class ItemDetailView(DetailView):
    model = Item1
    paginate_by = 10
    template_name = "bsc/product.html"


@login_required
def add_to_kpi(request, slug):
    item1 = get_object_or_404(Item1, slug=slug)
    order_item1, created = OrderItem1.objects.get_or_create(
        item=item1,
        user=request.user,
        ordered=False,
        Chi_tieu =2,
        Ket_qua = 2
    )

    order_qs = Order1.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item1.slug).exists():
            order_item1.quantity += 1
            order_item1.save()
            messages.info(request, "Tỉ trọng vừa cập nhật")
            return redirect("bsc:order-summary1")
        else:
            order.items.add(order_item1)
            messages.info(request, "KPI này bạn vừa thêm vào bảng giao KPI của bạn")
            return redirect("bsc:order-summary1")
    else:
        ordered_date = timezone.now()
        order1 = Order1.objects.create(
            user=request.user, ordered_date=ordered_date)

        order1.items.add(order_item1)
        messages.info(request, "KPI này bạn vừa thêm vào bảng giao KPI của bạn")
        return redirect("bsc:order-summary1")



@login_required
def remove_from_kpi(request, slug):
    item1 = get_object_or_404(Item1, slug=slug)
    order_qs = Order1.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item1.slug).exists():
            order_item1 = OrderItem1.objects.filter(
                item=item1,
                user=request.user,
                ordered=False,
            )[0]
            #order.items.remove(order_item)
            order_item1.delete()
            messages.info(request, "KPI này được loại khỏi bảng giao KPI của bạn")
            return redirect("bsc:order-summary1")
        else:
            messages.info(request, "Không có KPi được chọn")
            return redirect("bsc:order-summary1")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("bsc:order-summary1")



class CheckoutView(View):
    def get(self, *args,**kwargs):
        form = CheckoutForm
        context = {
            "form" : form
        }
        return render(self.request, "bsc/checkout.html", context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order1.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                apartment_address =form.cleaned_data.get('apartment_address')
                country= form.cleaned_data.get('country')
                zip= form.cleaned_data.get('zip')
                    #save_info= form.cleaned_data.get('save_info')
                  #  payment_option= form.cleaned_data.get('payment_option')
                billing_address = Billingaddress1(
                    user = self.request.user,
                    street_address= street_address,
                    apartment_address=apartment_address,
                    country=country,
                    zip=zip,
                )
                billing_address.save()
                order.billing_address= billing_address
                order.save()
                # To do: add redirect to the select payment opyion

            return redirect('bsc:checkout')
            messages.warning(self.request("thanh toán thất bại"))
            return redirect('bsc: checkout')
        except ObjectDoesNotExist:
            messages.warning(self.request, "Bạn chưa chọn KPI")
            return redirect("bsc:checkout")

class PaymentView(View): # Thanh toán
    def  get(self, *args, **kwargs):
        return render(self.request, "bsc/payment.html")


@login_required
def remove_single_item_from_kpi(request, slug):
    item1 = get_object_or_404(Item1, slug=slug)
    order_qs = Order1.objects.filter(
        user=request.user,
        ordered=False,
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item1.slug).exists():
            order_item1 = OrderItem1.objects.filter(
                item=item1,
                user=request.user,
                ordered=False
            )[0]
            if order_item1.quantity > 1:
                order_item1.quantity -= 5
                order_item1.save()
            else:
                order.items.remove(order_item1)
            messages.info(request, "Tỉ trọng vừa cập nhật")
            return redirect("bsc:order-summary1")
        else:
            messages.info(request, "KPI không còn trong bàn giao")
            return redirect("bsc:product1", slug=slug)
    else:
        messages.info(request, "Bạn không có còn bản KPI nào")
        return redirect("bsc:product1", slug=slug)



# This function will update and edit/sửa data

def update_kpi(request, id):
    if request.method == 'POST':
        bp = Order1.objects.get(pk=id)
        fmbp = OrderItem1_form(request.POST, instance=bp)
        if fmbp.is_valid():
            fmbp.save()
    else:
        bp = Order1.objects.get(pk=id)
        fmbo = OrderItem1_form(instance=bp)
    return render(request,'bsc/kpi_update_giaokp.html', {'form': fmbo})


@login_required
def update_single_item_from_cart(request, slug):
    item1 = get_object_or_404(Item1, slug=slug)
    order_qs = Order1.objects.filter(
        user=request.user,
        ordered=False,
    )
    fmbp = OrderItem1_form(request.POST or None)

    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item1.slug).exists():
            order_item1 = OrderItem1.objects.filter(
                item=item1,
                user=request.user,
                ordered=False
            )[0]
            if order_item1.Ket_qua > 1:
                order_item1.Ket_qua = fmbp['Ket_qua'].value()
                order_item1.save()
            else:
                order.items.remove(order_item1)
            messages.info(request, "Tỉ trọng vừa cập nhật")
            return redirect("bsc:order-summary1")
        else:
            messages.info(request, "KPI không còn trong bàn giao")
            return redirect("bsc:product1", slug=slug)
    else:
        messages.info(request, "Bạn không có còn bản KPI nào")
        return redirect("bsc:product1", slug=slug)
