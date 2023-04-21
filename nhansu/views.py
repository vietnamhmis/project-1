from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

from django.db.models import Sum, Avg, Max, Min, Count, Q
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from django.views.generic import ListView, DetailView, View
from .filter import To_Filter

from .forms import Don_vi_SearchForm, Bo_phanSearchForm, DonviUpdateForm, To_nhomSearchForm, \
    To_nhomForm, To_Form, Bo_phanForm, DonviForm, ProductForm, Nangluc_SearchForm, form_nangluc, KPI_SearchForm, \
    form_kpi, VanbanUpdateForm
from .models import *
import csv
import datetime

import xlwt
#----
from django.template.loader import render_to_string
#from weasyprint import HTML

import tempfile
from django.db.models import Sum, Count
from io import StringIO
#-------------
from docx import Document
from docx.shared import Inches
from docx.text import paragraph

#python -m pip install docxtpl
from docxtpl import DocxTemplate, InlineImage
#from docx2pdf import convert
import datetime as dt
import pythoncom
#-------------
from docx import Document
from docx.shared import Inches
from docx.text import paragraph

#python -m pip install docxtpl
from docxtpl import DocxTemplate, InlineImage #r
#from docx2pdf import convert
from random import randint
import datetime as dt
import pythoncom
import random
from datetime import datetime



now = datetime.now() # current date and time

import matplotlib.pyplot as plt

def is_valid_queryparam(param):
    return param != '' and param is not None
def filter_nangluc(request):
    qs = Nang_luc_2.objects.filter()
    qs_1 = qs[0:1]
    name_or_ma_nangluc = request.GET.get('name_or_ma_nangluc')
    ten_nangluc = request.GET.get('ten_nangluc')

    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')

    category = request.GET.get('category')
    su_dung = request.GET.get('su_dung')
    loai_nang_lucy = request.GET.get('loai_nang_lucy')
    Xuất_Excel =request.GET.get('Xuất_Excel')


    if is_valid_queryparam(name_or_ma_nangluc):
        qs = qs.filter(Q(name__icontains=name_or_ma_nangluc)
                       |Q(ma_nangluc__icontains=name_or_ma_nangluc)
                       ).distinct()

    if is_valid_queryparam(name_or_ma_nangluc):
        qs = qs.filter(name__icontains=name_or_ma_nangluc)

    elif is_valid_queryparam(date_min):
        qs = qs.filter(ngay_tao__gte=date_min)
    if is_valid_queryparam(date_max):
        qs = qs.filter(ngay_tao__lt=date_max)
    elif is_valid_queryparam(category) and category != 'Chọn ...':
         qs = qs.filter(tochuc_Sudung__name=category)
    elif is_valid_queryparam(loai_nang_lucy) and loai_nang_lucy != 'Chọn ...':
        qs = qs.filter(loai_nang_luc__name=loai_nang_lucy)
    elif su_dung != '':
        qs = Nang_luc_2.objects.filter(su_dung=1)
    return qs

#-----------------View char---------------------
def Nangluc_list_q(request):
    qs = filter_nangluc(request)
    qs_1 = qs[0:10]

    context = {'queryset': qs,'queryset_1':qs_1,
               'tochuc_Sudungs' : Tochuc_Sudung_KPI_NL.objects.all(),
               'loai_nang_lucs' : Loai_vanban.objects.all(),
               }
    return render(request,'nhansu/Nangluc_list_new.html', context)
#------------
def is_valid_queryparam(param):
    return param != '' and param is not None
def filter_vanban(request):
    qs_vb = Vanban.objects.filter()
    name_or_ma = request.GET.get('name_or_ma')
    ten_vanban = request.GET.get('ten_vanban')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')

    category = request.GET.get('category')
    su_dung = request.GET.get('su_dung')
    loai_vanban_y = request.GET.get('loai_vanban_y')
    Xuất_Excel =request.GET.get('Xuất_Excel')


    if is_valid_queryparam(name_or_ma):
        qs_vb = qs_vb.filter(Q(name__icontains=name_or_ma)
                       |Q(ma_vanban__icontains=name_or_ma)
                       ).distinct()

    elif is_valid_queryparam(date_min):
        qs_vb = qs_vb.filter(ngay_tao__gte=date_min)
    if is_valid_queryparam(date_max):
        qs_vb = qs_vb.filter(ngay_tao__lt=date_max)
    elif is_valid_queryparam(category) and category != 'Chọn ...':
         qs_vb = qs_vb.filter(tochuc_Sudung__name=category)

    elif is_valid_queryparam(loai_vanban_y) and loai_vanban_y != 'Chọn ...':
        qs_vb = qs_vb.filter(loai_vanban__name=loai_vanban_y)


    return qs_vb
#++++++++++++++++++++++++++++++++++++++++++
def Vanban_q(request):
    qs_vb = filter_vanban(request)
    qs_vb_1 = qs_vb[0:10]

    context = {'queryset': qs_vb,'queryset_1':qs_vb_1,
               'tochuc_Sudungs' : Tochuc_Sudung_KPI_NL.objects.all(),
               'loai_nang_lucs' : Loai_vanban.objects.all(),
               }
    return render(request,'nhansu/Van_ban_list.html', context)


def add_vanban(request):
    if request.method == 'POST':
        fm = VanbanUpdateForm(request.POST or None)
        if fm.is_valid():
            fm.save()
        fm = VanbanUpdateForm()
    else:
        fm = VanbanUpdateForm()
    total_CViec = Vanban.objects.count()
    context = {'form': fm, 'total_CViec':total_CViec,}
    return render(request,'nhansu/Vanban_ad.html', context)


def update_Vanban(request, id):
    if request.method == 'POST'  and request.FILES:
        dv = Vanban.objects.get(pk=id)
        fmvb = VanbanUpdateForm(request.POST, request.FILES, instance=dv)
        if fmvb.is_valid():

            fmvb.save()
        messages.success(request, 'Dữ liệu cập nhật')
    else:
        dv = Vanban.objects.get(pk=id)
        fmvb = VanbanUpdateForm(instance=dv)
    return render(request,'nhansu/Vanban_update.html', {'form': fmvb})




# This functions will delete/xóa
def del_Vanban(request, id):
    dv = Vanban.objects.get(pk=id)
    if request.method == 'POST':
        dv.delete()
        return HttpResponseRedirect('/dmvb/')
    return render(request, 'nhansu/Vanban_delete.html')

#>>>>>>>>>>>: Chương trình Danh mục năng lực:
@login_required
def Nangluc_list(request):
    name_or_ma_nangluc = request.GET.get('name_or_ma_nangluc')

    form = Nangluc_SearchForm(request.POST or None)
    queryset = Nang_luc_2.objects.all()[1:100]
    context = {'queryset': queryset,'form':form,}

    if request.method == 'POST':
        loai_nang_luc=form['loai_nang_luc'].value()
        tochuc_Sudung=form['tochuc_Sudung'].value()
        ho_congviec=form['ho_congviec'].value()
        name=form['name'].value()

        if is_valid_queryparam(name):
            queryset = Nang_luc_2.objects.filter(
            name__icontains=form['name'].value(),
                       )
        elif is_valid_queryparam(tochuc_Sudung):
            queryset = Nang_luc_2.objects.filter(
            tochuc_Sudung_id=form['tochuc_Sudung'].value(),
                       )

        elif is_valid_queryparam(loai_nang_luc):
            queryset = Nang_luc_2.objects.filter(
            loai_nang_luc_id=form['loai_nang_luc'].value(),
                       )

        elif is_valid_queryparam(ho_congviec):
            queryset = Nang_luc_2.objects.filter(
            ho_congviec_id=form['ho_congviec'].value(),
                       )


        if form['Xuất_Excel'].value() == True:
            responese = HttpResponse(content_type='application/ms-excel')
            responese['Content-Disposition'] = 'attachment; filename=DM_Nang_luc'+'.xls'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('nhanvien')
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            font_style.font.shadow = True

            TIEUDEM = xlwt.easyxf(
                'font: color RED, bold 1, name calibri, height 420;'
                'align: vertical center, horizontal center, wrap on;'
                'pattern:pattern_back_colour dark_red_ega;'
            )

            TIEUDE = xlwt.easyxf(
                'font: color BLUE, bold 1, name Calibri, height 250;'
                'align: vertical center, horizontal center, wrap on;'
                'pattern:pattern_back_colour dark_red_ega;')

            TIEUDE1 = xlwt.easyxf(
                'font: color RED, bold 1, name Calibri, height 250;'
                'align: vertical center, horizontal center, wrap on;'
                'pattern:pattern_back_colour dark_red_ega;')

            TIEUDE2 = xlwt.easyxf(
                'font: color BLUE, bold 1, name Calibri, height 250;'
 
                'pattern:pattern_back_colour dark_red_ega;')

            TIEUDE3 = xlwt.easyxf(
                'font: color RED, bold 1, name Calibri, height 250;'
                'align: vertical center, horizontal center, wrap on;'
                'pattern:pattern_back_colour dark_red_ega'
            )

            top_row5 = 0
            bottom_row5 = 0
            left_column5 = 0
            right_column5 = 2
            ws.write_merge(top_row5, bottom_row5, left_column5, right_column5,  'UBND TP.HỒ CHÍ MINH',TIEUDE)

            top_row7 = 0
            bottom_row7 = 0
            left_column7 = 3
            right_column7 = 5
            ws.write_merge(top_row7, bottom_row7, left_column7, right_column7,  'CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM', TIEUDE)

            top_row9 = 1
            bottom_row9 = 1
            left_column9 = 3
            right_column9 = 5
            ws.write_merge(top_row9, bottom_row9, left_column9, right_column9, 'Độc lập-Tự do-Hạnh phúc', TIEUDE3)

            top_row6 = 1
            bottom_row6 = 1
            left_column6 = 0
            right_column6 = 2
            ws.write_merge(top_row6, bottom_row6, left_column6, right_column6,  'TỔNG CÔNG TY TM SÀI GÒN-TNHH MTV', TIEUDE3)

            top_row = 3
            bottom_row = 3
            left_column = 0
            right_column = 5
            ws.write_merge(top_row, bottom_row, left_column, right_column, 'DANH MỤC NĂNG LỰC', TIEUDEM)



            row_num = 7
            for_left = xlwt.easyxf(
                "font: color blue, name calibri, height 250; borders: left thin, right thin, top thin, bottom thin; pattern: pattern solid, fore_color white;")

            TABLE_HEADER = xlwt.easyxf(
                'font: bold 1, color blue, name Tahoma, height 220;'
                'align: vertical center, horizontal center, wrap on;'
                'borders: top double, bottom double, left double, right double;'
                'pattern: pattern solid, pattern_fore_colour yellow, pattern_back_colour dark_red_ega;'
                                       )
              #----Định dạng chiều rộng cột
            ws.col(0).width = 1000
            ws.col(1).width = 1500
            ws.col(2).width = 8000
            ws.col(3).width = 8000
            ws.col(4).width = 4000
            ws.col(5).width = 4000
            ws.col(6).width = 5000
            ws.col(7).width = 5000
            ws.col(8).width = 5000
            ws.col(9).width = 5000
            ws.col(9).width = 8000

            columns =['Số TT','Mã', 'Tên năng lực', 'Mô tả',  ' Mức 1','Mức 2', 'Mức 3', 'Mức 4', 'Mức 5', 'Loại']
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            #----Định dạng chữ
            font_style= xlwt.XFStyle()
            font_style.font.italic = False

            rows= queryset.values_list('id', 'ma_nangluc','name','MoTa_nangluc', 'NL_muc_1', 'NL_muc_2', 'NL_muc_3', 'NL_muc_4', 'NL_muc_1', 'loai_nang_luc__name')
            for row in rows:
                row_num +=1
                for col_num in range(len(row)):
                    ws.write(row_num,col_num, str(row[col_num]), for_left)
            wb.save(responese)
            return responese

        total_queryset = queryset.count()
        context = {'queryset': queryset,'form':form,}
    return render(request,'nhansu/Nangluc_list.html', context)
##<<<<<<<<<<<<: Danh mục năng lực<<


def index(request):
    pro = Don_vi.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    context = {
        "pp": pro,
        "form": form
    }
    return render(request, 'partials/index.html', context)


#--------------------Chương trình Hiển thị /Sửa/ Xóa:.. ĐƠN VỊ ...........................................



def listDon_vi(request):
    form = Don_vi_SearchForm(request.POST or None)
    queryset = Don_vi.objects.all()
    bophan=queryset.all().aggregate(sobp=Count('bo_phan__id'))
    vitri_chucvu=queryset.filter().aggregate(soto=Count('mota_cv__id'))
    nhanvien=queryset.filter(id=5).aggregate(soto=Count('nhan_vien__id'))
    context = {'queryset': queryset,'form':form,'bophan':bophan,'vitri_chucvu':vitri_chucvu,'nhanvien':nhanvien}


    if request.method == 'POST':
        queryset = Don_vi.objects.filter(
            Ten_DV__icontains =form['Ten_DV'].value(),
           # Ten_DV__iregex=form['Ten_DV'].value(), #lỗi khi không có dự liệu lọc
            diachi__icontains=form['diachi'].value(),
        )

        vitri_chucvu=queryset.filter(Ten_DV__icontains =form['Ten_DV'].value(),diachi__icontains=form['diachi'].value(),).aggregate(vt=Count('mota_cv__id'))
        bophan=queryset.filter(Ten_DV__icontains =form['Ten_DV'].value(),diachi__icontains=form['diachi'].value(),).aggregate(bp=Count('bo_phan__id'))
        nhanvien=queryset.filter(Ten_DV__icontains =form['Ten_DV'].value(),diachi__icontains=form['diachi'].value(),).aggregate(nv=Count('nhan_vien__id'))

        rows= queryset.values_list('id', 'Ten_DV', 'diachi')


        context = {'queryset': queryset,'form':form,'bophan':bophan,'vitri_chucvu':vitri_chucvu,'nhanvien':nhanvien}



    return render(request,'nhansu/Don_vi_list.html', context)


def update_donvi(request, id):
    if request.method == 'POST':
        dv = Don_vi.objects.get(pk=id)
        fmdv = DonviUpdateForm(request.POST, instance=dv)
        if fmdv.is_valid():
            fmdv.save()
    else:
        dv = Don_vi.objects.get(pk=id)
        fmdv = DonviUpdateForm(instance=dv)
    return render(request,'nhansu/Don_vi_update.html', {'form': fmdv})

# This functions will delete/xóa
def del_donvi(request, id):
    dv = Don_vi.objects.get(pk=id)
    if request.method == 'POST':
        dv.delete()
        return HttpResponseRedirect('/dmdv/')
    return render(request, 'nhansu/Don_vi_delete.html')
        #return redirect('/')

#--------------------KẾT THÚC CHƯƠNG TRÌNH HIỂN THỊ DM ĐƠN VỊ.............................................

#--------------------Chương trình Hiển thị /Sửa/ Xóa:..BỘ PHẬN............................................
@login_required(login_url='/dangnhap/')
def list_Bophan(request):
    form = Bo_phanSearchForm(request.POST or None)
    queryset = Bo_phan.objects.all()
    vitri_chucvu=Bo_phan.objects.filter().aggregate(bp=Count('mota_cv__id'))
    to_nhom=Bo_phan.objects.filter().aggregate(bp=Count('to_nhom__id'))
    nhanvien=Bo_phan.objects.filter().aggregate(bp=Count('nhan_vien__id'))
    context = {'queryset': queryset,'form':form,'to_nhom':to_nhom,'vitri_chucvu':vitri_chucvu,'nhanvien':nhanvien}
    if request.method == 'POST':
        don_vi=form['don_vi'].value()
        #aa = don_vi.objects.all()
        queryset = Bo_phan.objects.filter(
            ten_bp__icontains=form['ten_bp'].value(),
           )
        if (don_vi != ''):
            queryset = queryset.filter(don_vi_id=don_vi)
            vitri_chucvu=Bo_phan.objects.filter(don_vi_id=don_vi).filter(ten_bp__icontains=form['ten_bp'].value(),).aggregate(bp=Count('mota_cv__id'))
            to_nhom=Bo_phan.objects.filter(don_vi_id=don_vi).filter(ten_bp__icontains=form['ten_bp'].value(),).aggregate(bp=Count('to_nhom__id'))
            nhanvien=Bo_phan.objects.filter(don_vi_id=don_vi).filter(ten_bp__icontains=form['ten_bp'].value(),).aggregate(bp=Count('nhan_vien__id'))

        context = {'queryset': queryset,'form':form,'to_nhom':to_nhom,'vitri_chucvu':vitri_chucvu,'nhanvien':nhanvien}



        if form['Xuất_Excel'].value() == True:
            responese = HttpResponse(content_type='application/ms-excel')
            responese['Content-Disposition'] = 'attachment; filename=DM bophan'+ '.xls'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Bo_phan')
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            font_style.font.shadow = True
            ws.write(0,1,'   TỔNG CÔNG TY XI MĂNG VIỆT NAM')
            ws.write(0,2,'   CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM',font_style )
            ws.write(1,2,'           Độc lập-Tự do-Hạnh phúc')
            ws.write(1,1,'CÔNG TY CỔ PHẦN XI MĂNG HÀ TIÊN 1',font_style)

            TIEUDE = xlwt.easyxf(
                'font: color RED, bold 1, name Tahoma, height 320;'
                'align: vertical center, horizontal center, wrap on;'
                'pattern:pattern_back_colour dark_red_ega;'
                                       )
            ws.write(3,1,'DANH SÁCH BỘ PHẬN',TIEUDE)
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
            ws.col(1).width = 9000
            ws.col(2).width = 18000
            ws.col(3).width = 15000
            ws.col(4).width = 3500
            ws.col(5).width = 2000


            columns =['Số TT', 'Tên bộ phận', 'Đơn vị', 'Nhiệm vụ']
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            #----Định dạng chữ
            font_style= xlwt.XFStyle()
            font_style.font.italic = False
            for_left = xlwt.easyxf("font: color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            rows= queryset.values_list('id', 'ten_bp', 'don_vi', 'nv_bp')
            for row in rows:
                row_num +=1
                for col_num in range(len(row)):
                    ws.write(row_num,col_num, str(row[col_num]), for_left)
            wb.save(responese)
            return responese
        context = {'queryset': queryset,'form':form,'to_nhom':to_nhom,'vitri_chucvu':vitri_chucvu,'nhanvien':nhanvien}
    return render(request,'nhansu/Bo_phan_list.html', context)

#---------------Xuất Pdf


#--------------------KẾT THÚC CHƯƠNG TRÌNH HIỂN THỊ DM ĐƠN VỊ.............................................
def s_bophan(request, id):
    queryset_bp = Bo_phan.objects.filter(don_vi_id=id)
    form = Bo_phanSearchForm(request.POST or None)
    queryset = Bo_phan.objects.all()
    bophan_sum = Bo_phan.objects.filter(don_vi_id=id).count()
    context = {'queryset': queryset_bp,'form':form,'bophan_sum':bophan_sum}
    return render(request,'nhansu/Bophan_list_sub.html', context)

def s_to_nhom(request, id):
    form = To_nhomSearchForm(request.POST or None)
    queryset = To_nhom.objects.all()
    queryset_to = To_nhom.objects.filter(bo_phan_id=id)
    To_nhom_sum = To_nhom.objects.filter(bo_phan_id=id).count()

    context = {'queryset': queryset_to,'form':form,'To_nhom_sum':To_nhom_sum}
    return render(request,'nhansu/To_nhom_list_sub.html', context)


#------------------.......................................................................................
def update_bophan(request, id):
    if request.method == 'POST':
        bp = Bo_phan.objects.get(pk=id)
        fmbp = Bo_phanForm(request.POST, instance=bp)
        if fmbp.is_valid():
            fmbp.save()
    else:
        bp = Bo_phan.objects.get(pk=id)
        fmbo = Bo_phanForm(instance=bp)
    return render(request,'nhansu/Bophan_update.html', {'form': fmbo})

# This functions will delete/xóa
def del_bophan(request, id):
    bp = Bo_phan.objects.get(pk=id)
    if request.method == 'POST':
        bp.delete()
        return HttpResponseRedirect('/dmbp/')
    return render(request, 'nhansu/Bophan_delete.html')
        #return redirect('/')


#--------------------Chương trình Hiển thị /Sửa/ Xóa:.. TỔ............................................
@login_required(login_url='/login/')
def list_to(request):
    form = To_nhomSearchForm(request.POST or None)
    queryset = To_nhom.objects.all()
    vitri_chucvu=To_nhom.objects.filter()
    nhanvien=To_nhom.objects.filter()

    context = {'queryset': queryset,'form':form,'vitri_chucvu':vitri_chucvu,'nhanvien':nhanvien}

    if request.method == 'POST':
        bo_phan=form['bo_phan'].value()
        queryset = To_nhom.objects.filter(
            ten_to__icontains=form['ten_to'].value(),
           )
        if (bo_phan != ''):
            queryset = queryset.filter(bo_phan_id=bo_phan)

            vitri_chucvu=To_nhom.objects.filter(bo_phan_id=bo_phan).filter(ten_to__icontains=form['ten_to'].value(),).aggregate(bp=Count('mota_cv__id'))

            nhanvien=To_nhom.objects.filter(bo_phan_id=bo_phan).filter(ten_to__icontains=form['ten_to'].value(),).aggregate(bp=Count('nhan_vien__id'))
        context = {'queryset': queryset,'form':form,'vitri_chucvu':vitri_chucvu,'nhanvien':nhanvien}



        if form['Xuất_Excel'].value() == True:
            responese = HttpResponse(content_type='application/ms-excel')
            responese['Content-Disposition'] = 'attachment; filename=DM bophan'+ \
                    str(datetime.datetime.now())+'.xls'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('kpi')
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            font_style.font.shadow = True
            ws.write(0,1,'   TỔNG CÔNG TY XI MĂNG VIỆT NAM')
            ws.write(0,2,'   CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM',font_style )
            ws.write(1,2,'           Độc lập-Tự do-Hạnh phúc')
            ws.write(1,1,'CÔNG TY CỔ PHẦN XI MĂNG HÀ TIÊN 1',font_style)

            TIEUDE = xlwt.easyxf(
                'font: color RED, bold 1, name Tahoma, height 320;'
                'align: vertical center, horizontal center, wrap on;'
                'pattern:pattern_back_colour dark_red_ega;'
                                       )
            ws.write(3,1,'DANH SÁCH TỔ',TIEUDE)
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
            ws.col(1).width = 9000
            ws.col(2).width = 18000
            ws.col(3).width = 1800
            ws.col(4).width = 3500
            ws.col(5).width = 2000


            columns =['Số TT', 'Tên Tổ', 'Tên bộ phận',  'Nhiệm vụ']
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            #----Định dạng chữ
            font_style= xlwt.XFStyle()
            font_style.font.italic = False
            for_left = xlwt.easyxf("font: color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            rows= queryset.values_list('id', 'ten_to', 'bo_phan',  'nv_tn')
            for row in rows:
                row_num +=1
                for col_num in range(len(row)):
                    ws.write(row_num,col_num, str(row[col_num]), for_left)
            wb.save(responese)
            return responese

        context = {'queryset': queryset,'form':form,'vitri_chucvu':vitri_chucvu,'nhanvien':nhanvien}

    return render(request,'nhansu/To_nhom_list_sub.html', context)

#--------------------KẾT THÚC CHƯƠNG TRÌNH HIỂN THỊ DM TỔ.............................................
#--------------------CHƯƠNG TRÌNH THÊM SỬA XÓA............................................
def update_tonhom(request, id):
    if request.method == 'POST':
        to_nhom = To_nhom.objects.get(pk=id)
        fmto_nhom = To_nhomForm(request.POST, instance=to_nhom)
        if fmto_nhom.is_valid():
            fmto_nhom.save()
    else:
        to_nhom = To_nhom.objects.get(pk=id)
        fmto_nhom = To_nhomForm(instance=to_nhom)
    return render(request,'nhansu/To_nhom_up.html', {'form': fmto_nhom})

# This functions will delete/xóa
def del_to(request, id):
    to_nhom = To_nhom.objects.get(pk=id)
    if request.method == 'POST':
        to_nhom.delete()
        return HttpResponseRedirect('/dmto/')
    return render(request, 'nhansu/To_nhom_delete.html')
        #return redirect('/')


 #------lọc theo search và xuất exel---------------------------------------------------------------



#-------------------- CHƯƠNG TRÌNH UP DATE DM ĐƠN VỊ.............................................

def add_to(request):
    fmt = To_Form()
    if request.method == 'POST':
        fmt = To_Form(request.POST)
        if fmt.is_valid():
            mt = fmt.cleaned_data['ma_to']
            tt = fmt.cleaned_data['ten_to']
            bp = fmt.cleaned_data['bo_phan']
            tn = fmt.cleaned_data['nv_tn']
            reg = To_nhom(ma_to=mt, ten_to=tt, bo_phan=bp, nv_tn=tn)
            reg.save()
        fmt = To_Form()
    else:
      fmt = To_Form()
    list_to = To_nhom.objects.all()
    cont ={'form': fmt, 'locds_to': list_to}

    return render(request, 'nhansu/To_nhom_add.html', cont)

def add_bophan(request):
    if request.method == 'POST':
        fmt = Bo_phanForm(request.POST or None)
        if fmt.is_valid():
            b1 = fmt.cleaned_data['ma_bp']
            b2 = fmt.cleaned_data['ten_bp']
            b3= fmt.cleaned_data['don_vi']
            b4 = fmt.cleaned_data['nv_bp']
            reg = Bo_phan(ma_bp=b1, ten_bp=b2, don_vi=b3, nv_bp=b4)
            reg.save()
        fmt = Bo_phanForm()
    else:
      fmt = Bo_phanForm()
    list_to = Bo_phan.objects.all()
    cont ={'form': fmt, 'locds_to': list_to}

    return render(request, 'nhansu/Bo_phan_add.html', cont)


def add_donvi(request):
    if request.method == 'POST':
        fmt = DonviForm(request.POST or None)
        if fmt.is_valid():
            b1 = fmt.cleaned_data['ma_DV']
            b2 = fmt.cleaned_data['Ten_DV']
            b3 = fmt.cleaned_data['diachi']
            b4 = fmt.cleaned_data['khoi_SXKD']
            b5 = fmt.cleaned_data['nv_dv']
            reg = Bo_phan(ma_DV=b1, Ten_DV=b2, diachi=b3, khoi_SXKD=b4, nv_dv=b5 )
            print("ccccc:", reg)
            reg.save()
        fmt = DonviForm()
    else:
      fmt = DonviForm()
    list_to = Don_vi.objects.all()
    cont ={'form': fmt, 'locds_to': list_to}

    return render(request, 'nhansu/Don_vi_add.html', cont)

#----------------------------------------

from django.shortcuts import render
from .models import Bo_phan
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# ------------Ajax
# Views.py

from django.views.generic import ListView
from .models import Don_vi

class Donvi_View(ListView):
    model = Don_vi
    template_name = 'nhansu/crud.html'
    context_object_name = 'users'
    paginate_by = 50

# Views.pyPost.objects.all().order_by('-date')


from django.views.generic import View
from django.http import JsonResponse
#------------------------------

# Views.py

from django.views.generic import ListView
from .models import Yeu_to_1_trinh_do

class YtoView(ListView):
    model = Yeu_to_1_trinh_do
    template_name = 'nhansu/yeuto_1.html'
    context_object_name = 'users'
    paginate_by = 15

# Views.pyPost.objects.all().order_by('-date')

from .models import Yeu_to_1_trinh_do
from django.views.generic import View
from django.http import JsonResponse

#-------------------------------
class CreateYeu_to_1_trinh_do(View):
    def  get(self, request):
        name1 = request.GET.get('name', None)
        titrong1 = request.GET.get('titrong', None)
        diem1 = request.GET.get('diem', None)

        obj = Yeu_to_1_trinh_do.objects.create(
            name = name1,
            titrong = titrong1,
            diem = diem1
        )
        user = {'id':obj.id,'name':obj.name,'titrong':obj.titrong,'diem':obj.diem}
        data = {
            'user': user
        }
        return JsonResponse(data)


class UpdateYeu_to_1_trinh_do(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        titrong1 = request.GET.get('titrong', None)
        diem1 = request.GET.get('diem', None)
        obj = Yeu_to_1_trinh_do.objects.get(id=id1)
        obj.name = name1
        obj.titrong = titrong1
        obj.diem = diem1
        obj.save()
        user = {'id':obj.id,'name':obj.name,'titrong':obj.titrong,'diem':obj.diem}
        data = {
            'user': user
        }
        return JsonResponse(data)

class DeleteYeu_to_1_trinh_do(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Yeu_to_1_trinh_do.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


#---------------------------
class Create_donvi(View):
    def  get(self, request):
        ma_DV1 = request.GET.get('ma_DV', None)
        Ten_DV1 = request.GET.get('Ten_DV', None)
        so_nhanvien1 = request.GET.get('so_nhanvien', None)
        obj = Don_vi.objects.create(
            ma_DV = ma_DV1,
            Ten_DV = Ten_DV1,
            so_nhanvien = so_nhanvien1
        )
        user = {'id':obj.id,'ma_DV':obj.ma_DV,'Ten_DV':obj.Ten_DV,'so_nhanvien':obj.so_nhanvien}
        data = {
            'user': user
        }
        return JsonResponse(data)
class Update_ax_Donvi(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)

        ma_DV1 = request.GET.get('ma_DV', None)
        Ten_DV1 = request.GET.get('Ten_DV', None)
        so_nhanvien1 = request.GET.get('so_nhanvien', None)

        obj = Don_vi.objects.get(id=id1)
        obj.ma_DV = ma_DV1
        obj.Ten_DV = Ten_DV1
        obj.so_nhanvien = so_nhanvien1
        obj.save()
        user = {'id':obj.id,'ma_DV':obj.ma_DV,'Ten_DV':obj.Ten_DV,'so_nhanvien':obj.so_nhanvien}
        data = {
            'user': user
        }
        return JsonResponse(data)
class Delete_ax_donvi(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Don_vi.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
#-----------------



#---
def show_products(request):
    products = Bo_phan.objects.all()
    context = {
        'queryset': products
    }
    return render(request, 'nhansu/Bo_phan_list.html', context)




#--------------------Chương trình Hiển thị /Năng lực............................................
def nangluc_chitiet(request, id):
    form = Nangluc_SearchForm(request.POST or None)
    queryset = Nang_luc_2.objects.get(pk=id)
    context = {'item': queryset,'form':form,}
    return render(request,'nhansu/nangluc_chitiet.html', context)


def nangluc_chitiet2(request, id):
    form = Nangluc_SearchForm(request.POST or None)
    queryset = Nang_luc_2.objects.get(pk=id)
    context = {'item': queryset,'form':form,}
    return render(request,'nhansu/nangluc_chitiet2.html', context)

def list_nangluc_2(request):
    loai_nang_luc = request.GET.get('loai_nang_luc')
    print("loai_nang_luc:", loai_nang_luc)
    if loai_nang_luc == None:
       list_nangluc = Nang_luc_2.objects.all()
    else:
       list_nangluc = Nang_luc_2.objects.filter(loai_nang_luc__name = loai_nang_luc)

    nhom_loai_nangluc = Loai_nangluc.objects.all()

    context = {'nhom_nangluc': nhom_loai_nangluc, 'list_nangluc': list_nangluc}
    return render(request, 'nhansu/nangluc_list_2.html', context)


def add_nangluc(request):
    ten_nhom_nangluc = Loai_nangluc.objects.all()
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        print('data:', data)
        print('avatars:', images)

        if data['loai_nang_luc'] != 'none':
            loai_nang_luc= Loai_nangluc.objects.get(id=data['loai_nang_luc'])

        elif data['loai_nang_luc_new'] != '':
            loai_nang_luc, created = Loai_nangluc.objects.get_or_create(
                name=data['loai_nang_luc_new'])
        else:
            loai_nang_luc = None
        for image in images:
            khoa_hoc = Nang_luc_2.objects.create(
                loai_nang_luc=loai_nang_luc,
                name=data['name'],
                MoTa_nangluc=data['MoTa_nangluc'],
                ngay_tao=data['ngay_tao'],
                NL_muc_1=data['NL_muc_1'],
                NL_muc_2=data['NL_muc_2'],
                NL_muc_3=data['NL_muc_3'],
                NL_muc_4=data['NL_muc_4'],
                NL_muc_5=data['NL_muc_5'],
                image = image,
            )
        return redirect('list_nangluc_2')
    context = {'ten_nhom_nangluc': ten_nhom_nangluc}
    return render(request, 'nhansu/nangluc_add.html', context)
#----------------------------------

def add_nangluc_thu(request):
    if request.method == 'POST':
        data = request.POST
        loai_nang_lucs = Loai_nangluc.objects.all()
        print('data:', data)
        print('avatars:', loai_nang_lucs)
        for loai_nang_luc in loai_nang_lucs:
            khoa_hoc = Nang_luc_2.objects.create(
                 name=data['name'],
                MoTa_nangluc=data['MoTa_nangluc'],
                ngay_tao=data['ngay_tao'],
                NL_muc_1=data['NL_muc_1'],
                NL_muc_2=data['NL_muc_2'],
                NL_muc_3=data['NL_muc_3'],
                NL_muc_4=data['NL_muc_4'],
                NL_muc_5=data['NL_muc_5'],
                loai_nang_luc = loai_nang_luc,
            )
        return redirect('list_nangluc_2')

    return render(request, 'nhansu/nangluc_add.html')


def del_nangluc(request, id):
    del_nangluc = Nang_luc_2.objects.get(pk=id)
    if request.method == 'POST':
        del_nangluc.delete()
        return redirect('list_nangluc')

    return render(request, 'nhansu/nangluc_del.html')

def update_nangluc(request, id):
    if request.method == 'POST':
        nangluc = Nang_luc_2.objects.get(pk=id)
        fm_nangluc = form_nangluc(request.POST, instance=nangluc)
        if fm_nangluc.is_valid():
            fm_nangluc.save()
    else:
        nangluc = Nang_luc_2.objects.get(pk=id)
        fm_nangluc = form_nangluc(instance=nangluc)
    return render(request,'Nhansu/Nang_luc_up.html', {'form': fm_nangluc})




#>>>>>>>>>>>: Chương trình Danh mục năng lực:
@login_required
def kpi_list(request):
    form = KPI_SearchForm(request.POST or None)
    queryset = KPI_list.objects.all()[1:20]
    context = {'queryset': queryset,'form':form,}

    if request.method == 'POST':
        loai_kpi=form['loai_kpi'].value()
        queryset = KPI_list.objects.filter(
            name__icontains=form['name'].value(),
                       )
        if (loai_kpi != ''):
            queryset = queryset.filter(loai_kpi_id=loai_kpi)

        if form['Xuất_Excel'].value() == True:
            responese = HttpResponse(content_type='application/ms-excel')
            responese['Content-Disposition'] = 'attachment; filename=DM_kpi'+'.xls'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('KPI')
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            font_style.font.shadow = True

            TIEUDEM = xlwt.easyxf(
                        'font: color RED, bold 1, name calibri, height 420;'
                        'align: vertical center, horizontal center, wrap on;'
                        'pattern:pattern_back_colour dark_red_ega;'
                    )

            TIEUDE = xlwt.easyxf(
                        'font: color BLUE, bold 1, name Calibri, height 250;'
                        'align: vertical center, horizontal center, wrap on;'
                        'pattern:pattern_back_colour dark_red_ega;')

            TIEUDE1 = xlwt.easyxf(
                        'font: color RED, bold 1, name Calibri, height 280;'
                        'align: horiz right, wrap on;'
                        'pattern:pattern_back_colour dark_red_ega;')

            TIEUDE2 = xlwt.easyxf(
                        'font: color BLUE, bold 1, name Calibri, height 280;'
         
                        'pattern:pattern_back_colour dark_red_ega;')

            TIEUDE3 = xlwt.easyxf(
                        'font: color RED, bold 1, name Calibri, height 250;'
                        'align: vertical center, horizontal center, wrap on;'
                        'pattern:pattern_back_colour dark_red_ega'
                    )


            top_row5 = 0
            bottom_row5 = 0
            left_column5 = 0
            right_column5 = 2
            ws.write_merge(top_row5, bottom_row5, left_column5, right_column5,  'UBND TP.HỒ CHÍ MINH',TIEUDE)
            top_row7 = 0
            bottom_row7 = 0
            left_column7 = 3
            right_column7 = 4
            ws.write_merge(top_row7, bottom_row7, left_column7, right_column7,  'CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM', TIEUDE)

            top_row9 = 1
            bottom_row9 = 1
            left_column9 = 3
            right_column9 = 4
            ws.write_merge(top_row9, bottom_row9, left_column9, right_column9, 'Độc lập-Tự do-Hạnh phúc', TIEUDE3)

            top_row6 = 1
            bottom_row6 = 1
            left_column6 = 0
            right_column6 = 2
            ws.write_merge(top_row6, bottom_row6, left_column6, right_column6,  'TỔNG CÔNG TY TM SÀI GÒN-TNHH MTV', TIEUDE3)
    #  --------------------------------------------
            top_row = 4
            bottom_row = 4
            left_column = 0
            right_column = 4
            ws.write_merge(top_row, bottom_row, left_column, right_column, 'DANH SÁCH KPI/BSC', TIEUDEM)


            row_num = 7
            for_left = xlwt.easyxf("font: bold 1, color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            TABLE_HEADER = xlwt.easyxf(
                'font: bold 1, color blue, name Tahoma, height 220;'
                'align: vertical center, horizontal center, wrap on;'
                'borders: top double, bottom double, left double, right double;'
                'pattern: pattern solid, pattern_fore_colour yellow, pattern_back_colour dark_red_ega;'
                                       )
              #----Định dạng chiều rộng cột
            ws.col(0).width = 1500
            ws.col(1).width = 1800
            ws.col(2).width = 12000
            ws.col(3).width = 12000
            ws.col(4).width = 3000
            ws.col(5).width = 2500
            ws.col(6).width = 2500
            ws.col(7).width = 5000
            ws.col(8).width = 3000
            ws.col(9).width = 1000

            columns =['Số TT','Mã', 'Tên KPO', 'Tên KPI',
                      'Tần xuất ĐG', 'ĐVị tính', 'Chỉ tiêu', 'Loại/Đơn vị']
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            #----Định dạng chữ
            font_style= xlwt.XFStyle()
            font_style.font.italic = False
            for_left = xlwt.easyxf(
                "font: color blue, name calibri, height 230; borders: left thin, right thin, top thin, bottom thin; pattern: pattern solid, fore_color white;")

            rows= queryset.values_list('id', 'ma_kpi','kpo', 'name','tan_xuat_d_gia','donvi_tinh__name','chi_tieu', 'loai_kpi__name')
            for row in rows:
                row_num +=1
                for col_num in range(len(row)):
                    ws.write(row_num,col_num, str(row[col_num]), for_left)


            for_foot = xlwt.easyxf("font: color blue;  pattern: pattern solid, fore_color white;")
            for_foot_ng = xlwt.easyxf('font: color blue, name Tahoma, height 230;'
                                      'align: vertical center, horizontal center,')
            TABLE_HEADER2 = xlwt.easyxf(
                'font: bold 1, color blue, name Tahoma, height 200;'
                'align: vertical center, horizontal center;'
            )


            ws.write(row_num + 3, 1, 'Ngày .... tháng 12 năm 2022', for_foot_ng)
            ws.write(row_num + 4, 1, 'Người phê duyệt', TABLE_HEADER2)
            ws.write(row_num + 3, 3, 'Ngày .... tháng 12 năm 2022', for_foot_ng)
            ws.write(row_num + 4, 3, 'Người đánh giá', TABLE_HEADER2)
            ws.write(row_num + 3, 5, 'Ngày ... tháng 12 năm 2022', for_foot_ng)
            # ws.write_merge(row_num + 18,row_num + 19, row_num + 20,row_num + 21,  'Người được đánh giá', TABLE_HEADER2)
            ws.write(row_num + 4, 5, 'Người được đánh giá', TABLE_HEADER2)
            wb.save(responese)
            return responese

        total_queryset = queryset.count()
        context = {'queryset': queryset,'form':form,}
    return render(request,'nhansu/KPI_list.html', context)
##<<<<<<<<<<<<: Danh mục năng lực<<
#--------------------Chương trình Hiển thị /Năng lực............................................
def kpi_chitiet(request, id):
    form = Nangluc_SearchForm(request.POST or None)
    queryset = KPI_list.objects.get(pk=id)
    context = {'item': queryset,'form':form,}
    return render(request,'nhansu/KPI_chitiet.html', context)

def update_kpi(request, id):
    if request.method == 'POST':
        kpi = KPI_list.objects.get(pk=id)
        fm_kpi = form_kpi(request.POST, instance=kpi)
        if fm_kpi.is_valid():
            fm_kpi.save()
    else:
        kpi = KPI_list.objects.get(pk=id)
        fm_kpi = form_kpi(instance= kpi)
    return render(request,'Nhansu/KPI_up.html', {'form': fm_kpi})

def del_kpi(request, id):
    del_kpi = KPI_list.objects.get(pk=id)
    if request.method == 'POST':
        del_kpi.delete()
        return redirect('kpi_list')

    return render(request, 'nhansu/KPI_del.html')


def add_kpi(request):
    if request.method == 'POST':
        fm = form_kpi(request.POST or None)
        if fm.is_valid():
            fm.save()
        fm = form_kpi()
    else:
        fm = form_kpi()

    context = {'form': fm, }
    return render(request,'nhansu/kpi_add.html', context)
