from django.db.models import Q, Count
from . forms import ProductForm
from django.shortcuts import render, get_object_or_404
#from rest_framework import generics
#from rest_framework.response import Response
from .models import Journal, Category, Author, Product
#from .serializers import JournalSerializer

from django.shortcuts import render, redirect, get_object_or_404

#----------https://www.youtube.com/watch?v=Qc5NnpxFbBo&t=4s-

import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt



#--------------------------


from django.http import JsonResponse

from django.template.loader import render_to_string


def index(request):
    return render(request, 'templates/index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'templates/product_list.html', {'products': products})

def save_product_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            products = Product.objects.all()
            data['html_product_list'] = render_to_string('templates/includes/partial_product_list.html', {
                'products': products
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
    else:
        form = ProductForm()
    return save_product_form(request, form, 'templates/includes/partial_product_create.html')


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
    else:
        form = ProductForm(instance=product)
    return save_product_form(request, form, 'templates/includes/partial_product_update.html')

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    data = dict()
    if request.method == 'POST':
        product.delete()
        data['form_is_valid'] = True
        products = Product.objects.all()
        data['html_product_list'] = render_to_string('templates/includes/partial_product_list.html', {
            'products': products
        })
    else:
        context = {'product': product}
        data['html_form'] = render_to_string('templates/includes/partial_product_delete.html', context, request=request)
    return JsonResponse(data)
















































from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .forms import TaskForm
from .models import Task
# from django.shortcuts import render, redirect
# from django.template import loader
class TaskView(View):
    form_class = TaskForm
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({"message": "success"})
            return JsonResponse({"message": "Validation failed"})
        return JsonResponse({"message": "Wrong request"})

    def get(self,request, *args, **kwargs):
        return render(request, "jquery/index.html", {})

class ViewTaskView(View):

    def get(self,request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, "jquery/view.html", {"tasks":tasks})

class TaskDeleteView(View):

    def get(self,request, pk, *args, **kwargs):
        if request.is_ajax():
            task = Task.objects.get(pk=pk)
            task.delete()
            return JsonResponse({"message":"success"})
        return JsonResponse({"message": "Wrong request"})




































def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = Journal.objects.all()
    categories = Category.objects.all()
    title_contains_query = request.GET.get('title_contains')
    id_exact_query = request.GET.get('id_exact')
    title_or_author_query = request.GET.get('title_or_author')
    view_count_min = request.GET.get('view_count_min')
    view_count_max = request.GET.get('view_count_max')


    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')

    category = request.GET.get('category')

    reviewed = request.GET.get('reviewed')
    not_reviewed = request.GET.get('notReviewed')

    if is_valid_queryparam(title_contains_query):
        qs = qs.filter(title__icontains=title_contains_query)

    elif is_valid_queryparam(id_exact_query):
        qs = qs.filter(id=id_exact_query)

    elif is_valid_queryparam(title_or_author_query):
        qs = qs.filter(Q(title__icontains=title_or_author_query)
                       | Q(author__name__icontains=title_or_author_query)
                       ).distinct()



    if is_valid_queryparam(view_count_min):
        qs = qs.filter(views__gte=view_count_min)

    if is_valid_queryparam(view_count_max):
        qs = qs.filter(views__lt=view_count_max)



    if is_valid_queryparam(date_min):
        qs = qs.filter(publish_date__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(publish_date__lt=date_max)

    if is_valid_queryparam(category) and category != 'Choose...':
        qs = qs.filter(categories__name=category)

    if reviewed == 'on':
        qs = qs.filter(reviewed=True)

    elif not_reviewed == 'on':
        qs = qs.filter(reviewed=False)

    return qs


def infinite_filter(request):
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    return Journal.objects.all()[int(offset): int(offset) + int(limit)]


def is_there_more_data(request):
    offset = request.GET.get('offset')
    if int(offset) > Journal.objects.all().count():
        return False
    return True


def BootstrapFilterView(request):
    qs = filter(request)
    context = {
        'queryset': qs,
        'don_vi': Category.objects.all()
    }
    return render(request, "bootstrap_form.html", context)









from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import dmkpi_form, kpi_dv_f, giao_KPI_f, dmkpi_SearchForm
from .models import dmkpi
from .filters import  KPI_Filter, Dmkpi_dv_Filter
from . models import *
from .forms import *
import datetime
import xlwt
from django.template.loader import render_to_string
import tempfile
from django.db.models import Sum


#>>>>>>>>>>>:  Đây là Chương trình THÊM/SỬA/XÓA: LIST KPI CÁ NHÂN:
def add_kpi(request):
    if request.method == 'POST':
        fm = dmkpi_form(request.POST or None)
        if fm.is_valid():
            tk = fm.cleaned_data['Ten_KPI']
            lc = fm.cleaned_data['LoaiCV']
            dv = fm.cleaned_data['Don_vi_tinh']
            tx = fm.cleaned_data['Tan_xuat_d_gia']
            tt = fm.cleaned_data['Ti_trong']
            reg = dmkpi(Ten_KPI=tk, LoaiCV=lc, Don_vi_tinh=dv, Tan_xuat_d_gia=tx,Ti_trong=tt)
            reg.save()
        fm = dmkpi_form()
    else:
        fm = dmkpi_form()
    total_dmkpi = dmkpi.objects.count()

 #--LỌC THEO FLTER-------------------------------------------------------------------
    stud = dmkpi.objects.filter()
    # stud = dmkpi.objects.all()[:100] #Hiện thị 5 phần tử cuối cùng
   # if request.method == 'POST':
       # LoaiCV=fm['LoaiCV'].value()
        #aa = don_vi.objects.all()
   # stud = dmkpi.objects.filter(LoaiCV=fm['LoaiCV'].value())
    context = {'form': fm, 'stu': stud,  'total_dmkpi':total_dmkpi,}
    return render(request, 'kpi/kpi_add_1.html', context)
#-------------------------------------------------------

# This function will update and edit/sửa data
def update_data(request, id):
    if request.method == 'POST':
        pi = dmkpi.objects.get(pk=id)
        fm = dmkpi_form(request.POST, instance=pi)
         #----------------------------------------------------
#        print(request.user.get_all_permision())
        if request.user.has_perm('Login.add_post'):
            if fm.is_valid():
                fm.save()
    else:
        pi = dmkpi.objects.get(pk=id)
        fm = dmkpi_form(instance=pi)
    return render(request, 'kpi/kpi_update.html', {'form': fm})

# This functions will delete/xóa
def delete_data(request, id):
    if request.method == 'POST':
        pi = dmkpi.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/kpi/')
        #return redirect('/')


#>>>>>>>>>>>: Chương trình XUẤT ECXEL Danh mục KPI CÁ NHÂN:
def ex_excel(request):
    responese = HttpResponse(content_type='application/ms-excel')
    responese['Content-Disposition'] = 'attachment; filename=KPICÁNHÂN'+ \
            str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('kpi')
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    font_style.font.shadow = True
    ws.write(0,0,'   TỔNG CÔNG TY XI MĂNG VIỆT NAM')
    ws.write(0,1,'CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM',font_style )
    ws.write(1,1,'       Độc lập-Tự do-Hạnh phúc')
    ws.write(1,0,'CÔNG TY CỔ PHẦN XI MĂNG HÀ TIÊN 1',font_style)
    TIEUDE = xlwt.easyxf(
        'font: color RED, bold 1, name Tahoma, height 320;'
        'align: vertical center, horizontal center, wrap on;'
        'pattern:pattern_back_colour dark_red_ega;'
                               )
    ws.write(3,0,'BẢNG DANH MỤC KPI',TIEUDE)
    row_num = 5
    for_left = xlwt.easyxf("font: bold 1, color blue; borders: top double, bottom double, left double, right double; align: horiz left")
    TABLE_HEADER = xlwt.easyxf(
        'font: bold 1, color blue, name Tahoma, height 220;'
        'align: vertical center, horizontal center, wrap on;'
        'borders: top double, bottom double, left double, right double;'
        'pattern: pattern solid, pattern_fore_colour yellow, pattern_back_colour dark_red_ega;'
                               )
      #----Định dạng chiều rộng cột
    ws.col(0).width = 30000
    ws.col(1).width = 1800
    ws.col(2).width = 1800
    ws.col(3).width = 3500
    ws.col(4).width = 2000
    columns =['Tên KPI','Loại','ĐV tính', 'Tấn xuất Đ.giá','Tỉ trọng']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
    #----Định dạng chữ
    font_style= xlwt.XFStyle()
    font_style.font.italic = False
    for_left = xlwt.easyxf("font: color blue; borders: top double, bottom double, left double, right double; align: horiz left")

    rows= dmkpi.objects.filter().values_list('Ten_KPI','LoaiCV','Don_vi_tinh', 'Tan_xuat_d_gia','Ti_trong')
    for row in rows:
        row_num +=1
        for col_num in range(len(row)):
            ws.write(row_num,col_num, str(row[col_num]), for_left)
    wb.save(responese)
    return responese
##<<<<<<<<<<<<: Kết thúc XUẤT ECXEL Danh mục KPI CÁ NHÂN:>>>>>>>>>>>>>>>>>>
##<<<<<<<<<<<<: Kết thúc Chương trình THÊM/SỬA/XÓA: LIST KPI CÁ NHÂN


#>>>>>>>>>>>: Đây là chương trình THÊM/SỬA/XÓA KPI CÁ NHÂN:
def add_kpicn(request):
    if request.method == 'POST':
        fmm = giao_KPI_f(request.POST)
        if fmm.is_valid():
            kg = fmm.cleaned_data['Ky_giao_KPI']
            ng = fmm.cleaned_data['Nguoigiao']
            nn = fmm.cleaned_data['Nguoi_nhan']
            tk = fmm.cleaned_data['Ten_KPI']
            tt = fmm.cleaned_data['Ti_trong']
            ct = fmm.cleaned_data['Chitieu']
            kn = fmm.cleaned_data['Ketqua_cn']
            kd = fmm.cleaned_data['ketqua_dv']
            kc = fmm.cleaned_data['ketqua_cuoi']
            tl = fmm.cleaned_data['ti_le_ht']
            dc = fmm.cleaned_data['diem_CV']
            dt = fmm.cleaned_data['diemtrongso']
            dg = fmm.cleaned_data['DVi_giao']
            dn = fmm.cleaned_data['DVi_nhan']
            ck = fmm.cleaned_data['Cap_KPI']
            cp = fmm.cleaned_data['dmkpi_phan_KPI']
            #
            dq = fmm.cleaned_data['Dv_quanly_KPI']
            ic = fmm.cleaned_data['KPI_cha']
            vc = fmm.cleaned_data['Vien_canh_cluoc']
            mc = fmm.cleaned_data['Mtieu_cluoc']
            td = fmm.cleaned_data['Tan_xuat_d_gia']
            #
            cc = fmm.cleaned_data['Chi_tieu_c_bo']
            du = fmm.cleaned_data['Don_vi_nhan_c_bo']
            dh = fmm.cleaned_data['Don_vi_tinh']
            reh = giao_KPI(Ky_giao_KPI=kg,Nguoigiao=ng, Nguoi_nhan=nn, Ten_KPI=tk,Ti_trong=tt,Chitieu=ct,Ketqua_cn=kn, ketqua_dv=kd,ketqua_cuoi=kc,ti_le_ht=tl, diem_CV=dc, diemtrongso=dt, DVi_giao=dg, DVi_nhan=dn, Cap_KPI=ck, dmkpi_phan_KPI=cp, Dv_quanly_KPI=dq,KPI_cha= ic, Vien_canh_cluoc=vc, Mtieu_cluoc=mc, Tan_xuat_d_gia=td, Chi_tieu_c_bo=cc, Don_vi_nhan_c_bo=du, Don_vi_tinh=dh
                        )
            reh.save()
        fmm = giao_KPI_f()
    else:
        fmm = giao_KPI_f()
  #  stud = dmkpi.objects.all()
  #  bienloc = 2---LoaiCV_id= bienloc
    stud = giao_KPI.objects.filter()
    KPIFiter = KPI_Filter(request.GET, queryset=stud)
    #form = StockSearchForm(request.POST or None)
    stud = KPIFiter.qs
    contextkpi = {'form': fmm,'KPIFiter': KPIFiter, 'stu': stud, }
    return render(request, 'kpi/sua_kpicn.html', contextkpi)


# This function will update and edit data
def update_kpicn(request, id):
    if request.method == 'POST':
        pii = giao_KPI.objects.get(pk=id)
        fmm = giao_KPI_f(request.POST, instance=pii)
        if fmm.is_valid():
            fmm.save()
    else:
        pii = giao_KPI.objects.get(pk=id)
        fmm = giao_KPI_f(instance=pii)
    return render(request, 'kpi/update_kpi.html', {'form': fmm})


# This functions will delete
def delete_kpicn(request, id):
    if request.method == 'POST':
        pii = giao_KPI.objects.get(pk=id)
        pii.delete()
        return HttpResponseRedirect('/kpicn/')
##*<<<<<<<<< kẾT THÚC Chương trình THÊM/SỬA/XÓA KPI CÁ NHÂN:................................



#>>>>>>>>>>>: Đây là chương trình THÊM/SỬA/XÓA List KPI ĐƠN VỊ:
# This function will ADD data
def kpi_donvi(request):
    if request.method == 'POST':
        fmd = kpi_dv_f(request.POST)
        if fmd.is_valid():
            mk = fmd.cleaned_data['Ma_KPo']
            ko = fmd.cleaned_data['Ten_KPo']
            tk = fmd.cleaned_data['Ten_KPI']
            dv = fmd.cleaned_data['Don_vi_tinh']
            ct = fmd.cleaned_data['Chitieu_KPI']
            tt = fmd.cleaned_data['Ti_trong']
            ck = fmd.cleaned_data['Cap_KPI']
            vc = fmd.cleaned_data['Vien_canh_cluoc']
            tx = fmd.cleaned_data['Tan_xuat_d_gia']
            ql = fmd.cleaned_data['Dv_quanly_KPI']
            reg = Dmkpi_dv(Ma_KPo=mk, Ten_KPo=ko, Ten_KPI=tk, Don_vi_tinh= dv, Chitieu_KPI=ct,Ti_trong=tt,Cap_KPI=ck,Vien_canh_cluoc=vc, Tan_xuat_d_gia=tx,Dv_quanly_KPI=ql)
            reg.save()
        fmd = kpi_dv_f()
    else:
        fmd = kpi_dv_f()
    loc_ki_dv = Dmkpi_dv.objects.filter()
    dvFiter = Dmkpi_dv_Filter(request.GET, queryset=loc_ki_dv)
    loc_ki_dv = dvFiter.qs
    context = {'form': fmd, 'loc_ki': loc_ki_dv,'donviFiter':dvFiter,}
    return render(request, 'kpi/kpidv_add_1.html', context)


# This function will update and edit data
def update_kpidv(request, id):
    if request.method == 'POST':
        pi = Dmkpi_dv.objects.get(pk=id)
        fmdv = kpi_dv_f(request.POST, instance=pi)
        if fmdv.is_valid():
            fmdv.save()
    else:
        pi = Dmkpi_dv.objects.get(pk=id)
        fmdv = kpi_dv_f(instance=pi)
    return render(request, 'kpi/kpidv_update.html', {'formdv': fmdv})


# This functions will delete
def delete_datadv(request, id):
    if request.method == 'POST':
        pi = Dmkpi_dv.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/kpidv/')
       # return redirect('/')
    context = {'item': pi}
    return render(request, 'kpi/kpidv_delete.html', context)
#<<<<<<... KẾT THÚC chương trình THÊM/SỬA/XÓA List KPI ĐƠN VỊ-----------------------------------------


#>>>>>>>>>>>: Chương trình XUẤT ECXEL Danh mục KPI ĐƠN VỊ:
def ex_exceldv(request):
    responese = HttpResponse(content_type='application/ms-excel')
    responese['Content-Disposition'] = 'attachment; filename=KPICÁNHÂN'+ \
            str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('kpi')
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    font_style.font.shadow = True
    ws.write(0,0,'   TỔNG CÔNG TY XI MĂNG VIỆT NAM')
    ws.write(0,4,'CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM',font_style )
    ws.write(1,4,'       Độc lập-Tự do-Hạnh phúc')
    ws.write(1,0,'CÔNG TY CỔ PHẦN XI MĂNG HÀ TIÊN 1',font_style)

    TIEUDE = xlwt.easyxf(
        'font: color RED, bold 1, name Tahoma, height 320;'
        'align: vertical center, horizontal center, wrap on;'
        'pattern:pattern_back_colour dark_red_ega;'
                               )
    ws.write(3,2,'DANH MỤC BSC/KPI ĐƠN VỊ',TIEUDE)
    row_num = 5
    for_left = xlwt.easyxf("font: bold 1, color blue; borders: top double, bottom double, left double, right double; align: horiz left")
    TABLE_HEADER = xlwt.easyxf(
        'font: bold 1, color blue, name Tahoma, height 220;'
        'align: vertical center, horizontal center, wrap on;'
        'borders: top double, bottom double, left double, right double;'
        'pattern: pattern solid, pattern_fore_colour yellow, pattern_back_colour dark_red_ega;'
                               )
      #----Định dạng chiều rộng cột
    ws.col(0).width = 1000
    ws.col(1).width = 15000
    ws.col(2).width = 15000
    ws.col(3).width = 1800
    ws.col(5).width = 1800
    ws.col(5).width = 1800
    ws.col(6).width = 2000

    columns =['Mã KPo','Tên KPo','Tên KPI','Đ.vị tính','Chỉ tiêu KPI', 'Tỉ trọng','Tần xuất đ.giá', 'Cấp KPI', 'Viễn cảnh','Đ.vị Q.lý']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
    #----Định dạng chữ
    font_style= xlwt.XFStyle()
    font_style.font.italic = False
    for_left = xlwt.easyxf("font: color blue; borders: top double, bottom double, left double, right double; align: horiz left")

    rows= Dmkpi_dv.objects.filter().values_list('Ma_KPo','Ten_KPo','Ten_KPI','Don_vi_tinh','Chitieu_KPI', 'Ti_trong','Tan_xuat_d_gia', 'Cap_KPI', 'Vien_canh_cluoc', 'Dv_quanly_KPI')
    for row in rows:
        row_num +=1
        for col_num in range(len(row)):
            ws.write(row_num,col_num, str(row[col_num]), for_left)
    wb.save(responese)
    return responese
#<<<<<<... Finish chương trình: XUẤT ECXEL list KPI ĐƠN VỊ...............................
