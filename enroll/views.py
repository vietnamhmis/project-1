from django.db.models import Q, Count
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#from .models import dmkpi
#from .filters import UserFilter
from .models import *
from .forms import *

import xlwt
from datetime import datetime, timedelta


from django.template.loader import render_to_string
import tempfile
from django.db.models import Sum, Count

#--------------]
from docxtpl import DocxTemplate, InlineImage #r

from random import randint
import datetime as dt
import pythoncom
import random
from datetime import datetime

now = datetime.now() # current date and time
import matplotlib.pyplot as plt
#---------------

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from nhansu.models import Don_vi

from .models import *
from .forms import *
import datetime
import xlwt
from django.template.loader import render_to_string
import tempfile
from django.db.models import Sum


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = Nhan_vien.objects.filter(da_nghiviec = False)
    categories = Don_vi.objects.all()
    ho_lot_thuong_dung_contains_query = request.GET.get('ho_lot_thuong_dung_contains')
    id_nhanvien_query = request.GET.get('id_nhanvien')
    ho_lot_thuong_dung_or_chucvu_query = request.GET.get('ho_lot_thuong_dung_or_chucvu')
    dantoc_tocngiao = request.GET.get('dantoc_tocngiao')
    view_count_max = request.GET.get('view_count_max')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    category = request.GET.get('category')
    da_nghiviec = request.GET.get('da_nghiviec')

    if is_valid_queryparam(ho_lot_thuong_dung_contains_query):
        qs = qs.filter(ho_lot_thuong_dung__icontains=ho_lot_thuong_dung_contains_query)

    elif is_valid_queryparam(id_nhanvien_query):
        qs = qs.filter(id=id_nhanvien_query)

    elif is_valid_queryparam(ho_lot_thuong_dung_or_chucvu_query):
        qs = qs.filter(Q(ho_lot_thuong_dung__icontains=ho_lot_thuong_dung_or_chucvu_query)
                       | Q(vitri_CV__Ten_Nhom_CV__icontains=ho_lot_thuong_dung_or_chucvu_query)
                       ).distinct()

    elif is_valid_queryparam(dantoc_tocngiao):
        qs = qs.filter(Q(ton_giao__TEN_TON_GIAO__icontains=dantoc_tocngiao)
                       | Q(dan_toc__TEN_DAN_TOC__icontains=dantoc_tocngiao)
                       ).distinct()

    if is_valid_queryparam(view_count_max):
        qs = qs.filter(views__lt=view_count_max)
    if is_valid_queryparam(date_min):
        qs = qs.filter(ngay_vao_dv__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(ngay_vao_dv__lt=date_max)

    elif is_valid_queryparam(category) and category != 'Chọn ...':
        qs = qs.filter(don_vi__Ten_DV=category)

    elif da_nghiviec == 'on':
        qs = Nhan_vien.objects.filter(da_nghiviec=True)

    return qs

def infinite_filter(request):
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    return Nhan_vien.objects.all()[int(offset): int(offset) + int(limit)]


def is_there_more_data(request):
    offset = request.GET.get('offset')
    if int(offset) > Nhan_vien.objects.all().count():
        return False
    return True


@login_required
def list_nhanvien(request):
    form = NhanvienSearchForm(request.POST or None)
    queryset = Nhan_vien.objects.all()[0:10]
    Nhan_vienql = Nhan_vien.objects.all()
    for vitri in Nhan_vienql:
        if vitri.vitriquanly == True:
                    ql = Quanly.objects.get_or_create(
                        quanly = vitri,
                        ten_thuong_dung= vitri.ho_lot_thuong_dung,
                        )
        else:
            continue

    context = {'queryset': queryset,'form':form,}
    if request.method == 'POST':

        vitri_CV=form['vitri_CV'].value()
        queryset = Nhan_vien.objects.filter(
            ten_thuong_dung__icontains=form['ten_thuong_dung'].value(),
            ho_lot_thuong_dung__icontains=form['ho_lot_thuong_dung'].value(),
           )
        if (vitri_CV != ''):
            queryset = queryset.filter(vitri_CV_id=vitri_CV)


        if form['Xuất_Excel'].value() == True:
            responese = HttpResponse(content_type='application/ms-excel')
            responese['Content-Disposition'] = 'attachment; filename=DSNS'+ \
                    str(datetime.datetime.now())+'.xls'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('nhanvien')
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            font_style.font.shadow = True

            TIEUDE = xlwt.easyxf(
                'font: color RED, bold 1, name Tahoma, height 320;'
                'align: vertical center, horizontal center, wrap on;'
                'pattern:pattern_back_colour dark_red_ega;'
                                       )
            #----------

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
            left_column7 = 5
            right_column7 = 9
            ws.write_merge(top_row7, bottom_row7, left_column7, right_column7,  'CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM', TIEUDE)

            top_row9 = 1
            bottom_row9 = 1
            left_column9 = 5
            right_column9 = 9
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
            right_column = 9
            ws.write_merge(top_row, bottom_row, left_column, right_column, 'DANH SÁCH NHÂN VIÊN', TIEUDEM)

            #--------

            row_num = 7
            for_left = xlwt.easyxf("font: bold 1, color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            TABLE_HEADER = xlwt.easyxf(
                'font: bold 1, color blue, name Tahoma, height 220;'
                'align: vertical center, horizontal center, wrap on;'
                'borders: top double, bottom double, left double, right double;'
                'pattern: pattern solid, pattern_fore_colour yellow, pattern_back_colour dark_red_ega;'
                                       )
              #----Định dạng chiều rộng cột
            ws.col(0).width = 1000
            ws.col(1).width = 2000
            ws.col(2).width = 6000
            ws.col(3).width = 4000
            ws.col(4).width = 6000
            ws.col(5).width = 6000
            ws.col(6).width = 6000
            ws.col(7).width = 2000
            columns =['Số TT','Mã', 'Họ', 'Tên',  'Chức vụ', 'Đơn vị', 'Bộ phận' 'Quản lý']
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            #----Định dạng chữ
            font_style= xlwt.XFStyle()
            font_style.font.italic = False
            for_left = xlwt.easyxf("font: color blue; borders: top double, bottom double, left double, right double; align: horiz left")

            rows= queryset.values_list('id', 'ma_nhan_vien','ho_lot_thuong_dung','ten_thuong_dung', 'vitri_CV__Ten_Nhom_CV','don_vi__Ten_DV', 'bo_phan__ten_bp', 'vitriquanly')
            for row in rows:
                row_num +=1
                for col_num in range(len(row)):
                    ws.write(row_num,col_num, str(row[col_num]), for_left)

            wb.save(responese)
            return responese
        total_queryset = queryset.count()
        context = {'queryset': queryset,'form':form,}
    return render(request,'enroll/employee_list_n.html', context)



def BaocaoFilter(request):
    qs = filter(request)
    qs_1 = qs[0:10]
    #Giới tính

    Tong_NV = qs.aggregate(total=Count('id', field="id"))['total']
    Nam = qs.filter(Gioi_tinh='Nam').count()
    Nu = qs.filter(Gioi_tinh='Nữ').count()
    #Chuyê  môn:
    TDTS = qs.filter(trinhdo__TEN_TRINH_DO='Tiến sĩ').count()
    TDTHS = qs.filter(trinhdo__TEN_TRINH_DO='Thạc sĩ').count()
    TDDH = qs.filter(trinhdo__TEN_TRINH_DO='Đại học').count()
    TDCD = qs.filter(trinhdo__TEN_TRINH_DO='Cao đẳng').count()
    TDTC = qs.filter(trinhdo__TEN_TRINH_DO='Trung cấp').count()
    TDSC = qs.filter(trinhdo__TEN_TRINH_DO='Sơ cấp').count()
    TDkhac = Tong_NV - TDTS - TDTHS -TDDH - TDTC -TDCD -TDTC -TDSC
    #Chính trị
    CTCC=  qs.filter(trinh_do_ctri__TEN_TRINH_DO='Cao cấp').count()
    CTTC = qs.filter(trinh_do_ctri__TEN_TRINH_DO='Trung cấp').count()
    CTSC = qs.filter(trinh_do_ctri__TEN_TRINH_DO='Sơ cấp').count()
    CTkhac = Tong_NV - CTCC - CTTC - CTSC

    NV_qly = qs.filter(vitriquanly=1).count()
    #Loại lAO ĐỘNG
    Nhom_1 = qs.filter(vitri_CV__Loai_laodong= 1).count()
    print(Nhom_1)
    Nhom_2  = qs.filter(vitri_CV__Loai_laodong= 2).count()
    Nhom_3  = qs.filter(vitri_CV__Loai_laodong= 3).count()
    Nhom_4  = qs.filter(vitri_CV__Loai_laodong= 4).count()
    #Đơn vị
    DV_1= qs.filter(don_vi__id= 1).count()
    DV_2= qs.filter(don_vi__id= 2).count()
    DV_3= qs.filter(don_vi__id= 3).count()
    DV_4= qs.filter(don_vi__id= 4).count()
    DV_5= qs.filter(don_vi__id= 5).count()
    DV_6= qs.filter(don_vi__id= 6).count()
    DV_7= qs.filter(don_vi__id= 7).count()
    DV_8= qs.filter(don_vi__id= 8).count()
    DV_9= qs.filter(don_vi__id= 9).count()
    DV_10= qs.filter(don_vi__id= 10).count()
    DV_11= qs.filter(don_vi__id= 11).count()
    DV_12= qs.filter(don_vi__id= 12).count()
    DV_13= qs.filter(don_vi__id= 13).count()
    DV_14= qs.filter(don_vi__id= 14).count()
    DV_15= qs.filter(don_vi__id= 15).count()
    DV_16= qs.filter(don_vi__id= 16).count()
    DV_17= qs.filter(don_vi__id= 17).count()
    DV_18= qs.filter(don_vi__id= 18).count()
    DV_19= qs.filter(don_vi__id= 19).count()
    DV_20= qs.filter(don_vi__id= 20).count()

    context = {
        'queryset': qs, 'queryset_1': qs_1, 'Nam':Nam, 'Nu':Nu, 'Tong_NV':Tong_NV,'NV_qly':NV_qly,
        'TDTS':TDTS, 'TDTHS':TDTHS, 'TDDH':TDDH,'TDCD':TDCD, 'TDTC':TDTC, 'TDSC':TDSC, 'TDkhac':TDkhac,
        'CT khac':CTkhac, 'CTCC': CTCC, 'CTTC':CTTC, 'CTSC': CTSC,
        'Nhom_1': Nhom_1, 'Nhom_2': Nhom_2, 'Nhom_3': Nhom_3, 'Nhom_4': Nhom_4,
        'DV_1':DV_1, 'DV_2':DV_2, 'DV_3':DV_3, 'DV_4':DV_3, 'DV_5':DV_5, 'DV6':DV_6, 'DV_7':DV_7, 'DV_8':DV_8, 'DV_9':DV_9, 'DV_10': DV_10,
        'DV_11':DV_11, 'DV_12':DV_12, 'DV_13':DV_13, 'DV_14':DV_13, 'DV_15':DV_15, 'DV6':DV_16, 'DV_17':DV_17, 'DV_18':DV_18, 'DV_19':DV_19, 'DV_20': DV_20,
        'categories': Don_vi.objects.all()
    }
    return render(request, "enroll/Baocao_nhanvien.html", context)



def BaocaoFilter_DSVN(request):
    qs = filter(request)
    context = {
        'querysetbs': qs,
        'categories': Don_vi.objects.all()[0:10]
    }
    return render(request, "enroll/employee_bc.html", context)




@login_required(login_url='login')
#@allowed_users(allowed_roles= ['customer'])


##********>>>>>>> Đây là chương trình THÊM/SỬA/XÓA NHÂN VIÊN:
@login_required(login_url='/dangnhap/')
def uploat_File (request):
     fmnv = Form_Nhanvien

     context = {'form_vn':fmnv}

     return render(request, 'enroll/employee_addsua.html',context )
#Thêm nhân viên
@login_required(login_url='/dangnhap/')
def add_nhanvien (request):
    if request.method == 'POST':
        fmvn = Form_Nhanvien(request.POST)
        if fmvn.is_valid():
           fmvn.save()
        fmvn = Form_Nhanvien()
        return HttpResponse("<h1>Nhân Sự được lưu<h1/>")
    else:
        fmnv = Form_Nhanvien()

        return render(request, 'enroll/test_diaphuong_addnv.html', {'form':fmnv})

   # return render(request, 'enroll/employee_add.html', {'fmnv':fmnv})


# This function will update and edit/sửa data-Ok
@login_required(login_url='/dangnhap/')
def update_nhanvien(request, id):
    pnv = Nhan_vien.objects.get(pk=id)
    fmnv = Form_Nhanvien(instance=pnv)
    if request.method == 'POST':
        fmnv = Form_Nhanvien(request.POST,request.FILES, instance=pnv)
        data = request.POST
        #print('data:', data)
        if fmnv.is_valid():
            fmnv.save()
        return redirect('employees')
    else:
        pnv = Nhan_vien.objects.get(pk=id)
        fmnv = Form_Nhanvien(instance=pnv)
    #return render(request, 'enroll/test.html', {'fmnv': fmnv})
    return render(request, 'enroll/employee_update.html', {'fmnv': fmnv})



# This functions will delete/xóa- ok
def delete_nhanvien(request, id):
    pnv = Nhan_vien.objects.get(pk=id)
    if request.method == 'POST':
        pnv.delete()
        return HttpResponseRedirect('/dmnv/')
    return render(request, 'enroll/employees_delete.html')
        #return redirect('/')

##********>>>>>>> kết thúc chương trình THÊM/SỬA/XÓA NHÂN VIÊN:>>>>>>>>>>>>>>>>>>>>

@login_required(login_url='/dangnhap/')
def employee(request):
    form = NhanvienSearchForm(request.POST or None)
    queryset = Nhan_vien.objects.all() [1:20]
    context = {'queryset': queryset,'form':form,}
    if request.method == 'POST':
        vitri_CV=form['vitri_CV'].value()
        queryset = Nhan_vien.objects.filter(
            ho_lot_thuong_dung__icontains=form['ho_lot_thuong_dung'].value(),
            ten_thuong_dung__icontains=form['ten_thuong_dung'].value(),
           )
        if (vitri_CV != ''):
            queryset = queryset.filter(vitri_CV_id=vitri_CV)
            context = {'queryset': queryset,'form':form}
        if form['Xuất_Excel'].value() == True:
            responese = HttpResponse(content_type='application/ms-excel')
            responese['Content-Disposition'] = 'attachment; filename=Danh sách CBNV'+ \
                    str(datetime.datetime.now())+'.xls'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('nhanvien')
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            font_style.font.shadow = True
            ws.write(0,0,'   TỔNG CÔNG TY XI MĂNG VIỆT NAM')
            ws.write(0,2,'   CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM',font_style )
            ws.write(1,2,'           Độc lập-Tự do-Hạnh phúc')
            ws.write(1,0,'CÔNG TY CỔ PHẦN XI MĂNG HÀ TIÊN 1',font_style)

            TIEUDE = xlwt.easyxf(
                'font: color RED, bold 1, name Tahoma, height 320;'
                'align: vertical center, horizontal center, wrap on;'
                'pattern:pattern_back_colour dark_red_ega;'
                                       )
            ws.write(3,2,'DANH SÁCH NHÂN VIÊN',TIEUDE)
            row_num = 5
            for_left = xlwt.easyxf("font: bold 1, color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            TABLE_HEADER = xlwt.easyxf(
                'font: bold 1, color blue, name Tahoma, height 220;'
                'align: vertical center, horizontal center, wrap on;'
                'borders: top double, bottom double, left double, right double;'
                'pattern: pattern solid, pattern_fore_colour yellow, pattern_back_colour dark_red_ega;'
                                       )
              #----Định dạng chiều rộng cột
            ws.col(0).width = 3000
            ws.col(1).width = 6000
            ws.col(2).width = 10000
            ws.col(3).width = 5000
            ws.col(4).width = 3500
            ws.col(5).width = 2000
            columns =['Số TT','Mã', 'Họ', 'Tên',  'Chức vụ']
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            #----Định dạng chữ
            font_style= xlwt.XFStyle()
            font_style.font.italic = False
            for_left = xlwt.easyxf("font: color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            rows= queryset.values_list('id', 'ma_nhan_vien','ho_lot_thuong_dung','ten_thuong_dung', 'vitri_CV_id')
            for row in rows:
                row_num +=1
                for col_num in range(len(row)):
                    ws.write(row_num,col_num, str(row[col_num]), for_left)
            wb.save(responese)
            return responese
        total_queryset = queryset.count()
        context = {'queryset': queryset,'form':form,}
    return render(request,'enroll/employees.html', context)

#>>>>>>>>>>>: Chương trình HIỂN THỊ List+ Xuât excel nhân viên:
#diemdanhgia=queryset.filter(ten_thuong_dung__icontains =form['ten_thuong_dung'].value(),ho_lot_thuong_dung__icontains=form['ho_lot_thuong_dung'].value(),).aggregate(diem=Count('Danhgia_nluc__id'))


@login_required
def list_nhanvienc(request):
    form = NhanvienSearchForm(request.POST or None)
    queryset = Nhan_vien.objects.all()


    Nhan_vienql = Nhan_vien.objects.all()
    for vitri in Nhan_vienql:
        if vitri.vitriquanly == True:
                    ql = Quanly.objects.get_or_create(
                        quanly = vitri,
                        ten_thuong_dung= vitri.ho_lot_thuong_dung,

                        )

        else:
            continue


    #diemdanhgia=queryset.filter().aggregate(diem=Count('Danhgia_nluc__id'))

    context = {'queryset': queryset,'form':form,}
    if request.method == 'POST':
        vitri_CV=form['vitri_CV'].value()
        queryset = Nhan_vien.objects.filter(
            ten_thuong_dung__icontains=form['ten_thuong_dung'].value(),
            ho_lot_thuong_dung__icontains=form['ho_lot_thuong_dung'].value(),
           )
        if (vitri_CV != ''):
            queryset = queryset.filter(vitri_CV_id=vitri_CV)
            #diemdanhgia=queryset.filter().aggregate(diem=Count('Danhgia_nluc__id'))

        if form['Xuất_Excel'].value() == True:
            responese = HttpResponse(content_type='application/ms-excel')
            responese['Content-Disposition'] = 'attachment; filename=DSNS'+ \
                    str(datetime.datetime.now())+'.xls'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('nhanvien')
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
            ws.write(3,2,'DANH SÁCH NHÂN VIÊN',TIEUDE)
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
            ws.col(1).width = 2000
            ws.col(2).width = 6000
            ws.col(3).width = 4000
            ws.col(4).width = 6000
            ws.col(5).width = 6000
            ws.col(6).width = 6000
            ws.col(7).width = 2000
            columns =['Số TT','Mã', 'Họ', 'Tên',  'Chức vụ', 'Đơn vị', 'Bộ phận' 'Quản lý']
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            #----Định dạng chữ
            font_style= xlwt.XFStyle()
            font_style.font.italic = False
            for_left = xlwt.easyxf("font: color blue; borders: top double, bottom double, left double, right double; align: horiz left")

            rows= queryset.values_list('id', 'ma_nhan_vien','ho_lot_thuong_dung','ten_thuong_dung', 'vitri_CV__Ten_Nhom_CV','don_vi__Ten_DV', 'bo_phan__ten_bp', 'vitriquanly')
            for row in rows:
                row_num +=1
                for col_num in range(len(row)):
                    ws.write(row_num,col_num, str(row[col_num]), for_left)

            wb.save(responese)
            return responese
        total_queryset = queryset.count()
        context = {'queryset': queryset,'form':form,}
    return render(request,'enroll/employee_list_n.html', context)

@login_required
def add_quanly(request):
    Nhan_vienql = Nhan_vien.objects.all()
    for vitriquanly in Nhan_vienql:
        if vitriquanly.vitriquanly == True:
                    ql = Quanly.objects.create(
                        quanly = vitriquanly,
                        ten_thuong_dung=Nhan_vien.ten_thuong_dung,

                        )
        else:
            continue
        return redirect('list_nangluc_2')
    context = {'Nhanvien_danhgias': Nhan_vienql}

    return render(request, 'enroll/employee_list.html')

##<<<<<<<<<<<<: Kết thúc Chương trình Hiện thị List+ Excel NHÂN VIÊN<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
@login_required(login_url='/dangnhap/')
def donvi_nhanvien(request, id):
    form = NhanvienSearchForm(request.POST or None)
    queryset_nvien_dvi = Nhan_vien.objects.filter(don_vi_id=id)

    context = {'queryset': queryset_nvien_dvi,'form':form,}
    return render(request,'enroll/employee_list_nvien_dvi.html', context)

@login_required(login_url='/dangnhap/')
def bophan_nhanvien(request, id):
    form = NhanvienSearchForm(request.POST or None)
    queryset_nvien_bp = Nhan_vien.objects.filter(bo_phan_id=id)
    context = {'queryset': queryset_nvien_bp,'form':form,}
    return render(request,'enroll/employee_list_nvien_bp.html', context)

@login_required(login_url='/dangnhap/')
def tonhom_nhanvien(request, id):
    form = NhanvienSearchForm(request.POST or None)
    queryset_nvien_to = Nhan_vien.objects.filter(to_nhom_id=id)
    context = {'queryset': queryset_nvien_to,'form':form,}
    return render(request,'enroll/employee_list_nvien_to.html', context)





#form = Form_FNhanvien(request.POST or None)
   #if form['Xuất_word'].value() == True:
#<<<<<<... Chương trình xem Profile nhân viên:
def nhanvien_profile_up(request, id):
    pnv = Nhan_vien.objects.get(id=id)
    doc = DocxTemplate("word_template/M_2C_TCTW.docx")
    queryset2 = {
        "ho_lot_thuong_dung": pnv.ho_lot_thuong_dung,
        "ten_thuong_dung" : pnv.ten_thuong_dung,
        "ma_nhan_vien": pnv.ma_nhan_vien,
        "Chuc_vu_dang": pnv.Chuc_vu_dang,
        "avatar": pnv.avatar,

        "C_danh_kiem_nhiem": pnv.C_danh_kiem_nhiem,
        "ngay_sinh": pnv.ngay_sinh,
        "ma_tinh_noi_sinh": pnv.ma_tinh_noi_sinh.TEN_TINH,
        "Nguyen_quan": pnv.Nguyen_quan.TEN_TINH,
        "dc_hiennay": pnv.dc_hiennay, "tel_dd": pnv.tel_dd,
        "dc_thuong_tru": pnv.dc_thuong_tru,
        "phuong_xa": pnv.phuong_xa.Ten_xa,
        "quan_huyen": pnv.quan_huyen.Ten_quan,
        "dan_toc": pnv.dan_toc.TEN_DAN_TOC,
        "ton_giao": pnv.ton_giao.TEN_TON_GIAO,
        "thanhphan_gd": pnv.thanhphan_gd.THANH_PHAN,
        "ngay_vao_nganh": pnv.ngay_vao_nganh,
        "ngay_vao_dv": pnv.ngay_vao_dv,
        "Ngay_vao_dang": pnv.Ngay_vao_dang,
        "Ngay_ct": pnv.Ngay_ct,
        "Ngay_vao_doan": pnv.Ngay_vao_doan,
        "trinh_do_ctri": pnv.trinh_do_ctri.TEN_TRINH_DO,
        "trinhdovh": pnv.trinhdovh.TEN_TRINH_DO,
        "trinhdo": pnv.trinhdo.TEN_TRINH_DO,
        "vitri_CV": pnv.vitri_CV.Ten_vitri_full,
        "Danh_hieu_ph_tang": pnv.Danh_hieu_ph_tang,
        "So_truong":pnv.So_truong,
         "Can_nang": pnv.Can_nang,
         "Chieu_cao": pnv.Chieu_cao,
         "so_CCCD": pnv.so_CCCD,
                }
    doc.render(queryset2)
    doc.save('thu_word/LL2c_'+ str(pnv.ho_lot_thuong_dung+" "+ pnv.ten_thuong_dung)+'.docx')

    return render(request, 'enroll/employes_profile_3.html', {'form_nhanvien': pnv})



def nhanvien_profile_view(request, id):
    pnv = Nhan_vien.objects.get(id=id)
    return render(request, 'enroll/employes_profile_3.html', {'form_nhanvien': pnv})
#<<<<<<...kết thúc Chương trình xem Profile nhân viên:


def nhanvien_profile_3(request, id):
    if request.method == 'request.POST or None':
        pnv = Nhan_vien.objects.get(id=id)
        form_nv = Form_Nhanvien(request.POST, instance=pnv)
        if form_nv.is_valid():
            form_nv.save()
    else:
        pnv = Nhan_vien.objects.get(pk=id)
        form_nv = Form_Nhanvien(instance=pnv)
        context = {'form_nhanvien': pnv, 'form_nv_update': form_nv}
        return render(request, 'enroll/employes_profile_3.html.html', context)


def nhanvien_profile_up_tt1(request, id):
    if request.method == 'request.POST or None':
        pnv = Nhan_vien.objects.get(pk=id)
        form_nv = Form_Nhanvien(request.POST, instance=pnv)
        if form_nv.is_valid():
            form_nv.save()
    else:
        pnv = Nhan_vien.objects.get(pk=id)
        form_nv = Form_Nhanvien(instance=pnv)
        context = {'form_nhanvien': pnv, 'form_nv_update': form_nv}
        return render(request, 'enroll/profile_up_tt1.html',context)


#_--------------Chương trinh load tỉnh, huyện, xã...

from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from nhansu.models import Tinh, Quan_huyen, Phuong_xa, Bo_phan,To_nhom
def load_diaphuong(request):
    tinh_thanh_id = request.GET.get('tinh_thanh')
    quan_huyens = Quan_huyen.objects.filter(Tinh_thanh_id=tinh_thanh_id).order_by('Ten_quan')
    quan_huyen_id = request.GET.get('quan_huyen')
    phuong_xas = Phuong_xa.objects.filter(Quan_huyen_id=quan_huyen_id).order_by('Ten_xa')

  #---------------

    don_vi_id = request.GET.get('don_vi')
    bo_phans = Bo_phan.objects.filter(don_vi_id=don_vi_id).order_by('ten_bp')
    bo_phan_id = request.GET.get('bo_phan')
    to_nhoms = To_nhom.objects.filter(bo_phan_id=bo_phan_id).order_by('ten_to')
    context= {'bo_phans': bo_phans, 'to_nhoms':to_nhoms, 'quan_huyens': quan_huyens, 'phuong_xas':phuong_xas}
    return render(request, 'enroll/list_choise_diaphuong.html', context)
