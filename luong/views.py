from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .forms import *
from . models import *
from enroll.models import Nhan_vien, Quanly
from nhansu.models import Don_vi, TK_ngach
from mota_cv.models import Mota_Cv7
from django.db.models import Sum, Count
from datetime import datetime

import datetime
from datetime import date
import xlwt

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.db.models import Sum, Avg, Max, Min, Count, Q
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
#--------------]
from docxtpl import DocxTemplate, InlineImage #r
#from docx2pdf import convert
from random import randint
import datetime as dt
import pythoncom
import random
from datetime import datetime
from django.contrib import messages
from mota_cv.forms import list_dinhgia_cv

now = datetime.now() # current date and time
import matplotlib.pyplot as plt
#---------------



def yto_luong(request, id):
    form = list_dinhgia_cv(request.POST or None)
    queryset7 = Mota_Cv7.objects.filter(Nhom_luong=id)

    context = {'queryset7': queryset7,'form':form,}
    if request.method == 'POST':
        don_vi=form['don_vi'].value()
        bo_phan =form['bo_phan'].value()
        Ten_Nhom_CV=form['Ten_Nhom_CV'].value()
        queryset7 = Mota_Cv7.objects.filter(Nhom_luong=1)
        if form['Xuất_Excel'].value() == True:
            responese = HttpResponse(content_type='application/ms-excel')
            responese['Content-Disposition'] = 'attachment; filename=Danh sách dinhgia'+ '.xls'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('nhanvien')
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            font_style.font.shadow = True

     #----------------------------------

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
            ws.write_merge(top_row, bottom_row, left_column, right_column, 'BIỂU ĐỊNH GIÁ GIÁ TRỊ CÔNG VIỆC', TIEUDEM)

    #  --------------------------------------------
            row_num = 7
            for_left = xlwt.easyxf("font: bold 1, color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            TABLE_HEADER = xlwt.easyxf(
                'font: bold 1, color blue, name Tahoma, height 220;'
                'align: vertical center, horizontal center, wrap on;'
                'borders: top double, bottom double, left double, right double;'
                'pattern: pattern solid, pattern_fore_colour yellow, pattern_back_colour dark_red_ega;'
                                       )
              #----Định dạng chiều rộng cột
            ws.col(0).width = 2000
            ws.col(1).width = 6600
            ws.col(2).width = 6000
            ws.col(3).width = 6000
            ws.col(4).width = 2200
            ws.col(5).width = 2000
            ws.col(6).width = 2000
            ws.col(7).width = 2000
            ws.col(8).width = 2200
            ws.col(9).width = 2000
            ws.col(10).width = 2000
            ws.col(11).width = 2000

            columns =['Số TT','Chức vụ','Đơn vị', 'Bộ phân', 'Trình độ', 'kỹ năng', 'Trách nhiệm', 'Mức ảnh hưởng', 'Sáng tạo', 'Giao tiếp',
                      'Điều kiện làm việc',
                      ('Nhóm lương'), 'Điểm',
                      ]
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            #----Định dạng chữ
            font_style= xlwt.XFStyle()
            font_style.font.italic = False
            for_left = xlwt.easyxf("font: color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            rows= queryset7.values_list('id', 'Ten_Nhom_CV', 'don_vi__Ten_DV', 'bo_phan__ten_bp', 'Yeu_to_1_trinh_do', 'Yeu_to_2_Ky_nang', 'Yeu_to_3_Trach_nhiem', 'Yeu_to_4_Anh_huong', 'Yeu_to_5_Sangtao', 'Yeu_to_6_Giaotiep',
                      'Yeu_to_7_DK_lamviec', 'Yeu_to_khac', 'tong_diem7')

            for row in rows:
                row_num +=1
                for col_num in range(len(row)):
                    ws.write(row_num,col_num, str(row[col_num]), for_left)

            wb.save(responese)
            return responese
    context = {'queryset7': queryset7,'form':form,}
    return render(request,'mota_cv/dinhgia_list_7yto.html', context)

# ---------------------------------


from django.db.models import Sum
def xepluong(request):
    form = Phuongan_luong_f(request.POST or None)
    PAluong_list = Phuongan_luongbhxh.objects.all()


    total_Luong_BHXH_cu = (PAluong_list.aggregate(total=Sum('Luong_BHXH_cu', field="Luong_BHXH_cu"))['total'])
    total_Luong_BHXH_moi = (PAluong_list.aggregate(total=Sum('Luong_BHXH_moi', field="Luong_BHXH_moi"))['total'])
    total_Luong_cu = (PAluong_list.aggregate(total=Sum('Luong_cu', field="Luong_cu"))['total'])
    total_Luong_moi = (PAluong_list.aggregate(total=Sum('Luong_moi', field="Luong_moi"))['total'])

    if total_Luong_BHXH_moi and total_Luong_BHXH_cu:
        CL_BHXH = total_Luong_BHXH_moi - total_Luong_BHXH_cu
    if total_Luong_moi and total_Luong_moi:
        CL_luong = total_Luong_moi - total_Luong_moi

    total_CL_Luong_BHXH_PA_1 = (PAluong_list.aggregate(total=Sum('CL_Luong_BHXH_PA_1', field="CL_Luong_BHXH_PA_1"))['total'])
    total_CL_Luong_moi_PA_1 = (PAluong_list.aggregate(total=Sum('CL_Luong_moi_PA_1', field="CL_Luong_moi_PA_1"))['total'])


    context = { 'queryset': PAluong_list, 'form': form,'total_Luong_BHXH_cu': total_Luong_BHXH_cu, 'total_Luong_cu':total_Luong_cu,
                'total_Luong_BHXH_moi':total_Luong_BHXH_moi, 'total_Luong_moi':total_Luong_moi,
                'total_CL_Luong_BHXH_PA_1':total_CL_Luong_BHXH_PA_1, 'total_CL_Luong_moi_PA_1':total_CL_Luong_moi_PA_1,
                }

    if form['Xuất_Excel'].value() == True:
            responese = HttpResponse(content_type='application/ms-excel')
            responese['Content-Disposition'] = 'attachment; filename=' +  'PAL.xls'

            wb = xlwt.Workbook(encoding='utf-8')


            ws = wb.add_sheet(str('chucdanh_CV'))

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
            ws.write_merge(top_row, bottom_row, left_column, right_column, 'PHƯƠNG ÁN CHUYỂN XẾP LƯƠNG', TIEUDEM)

           # rows1 = PAluong_list.values_list('Nhanvien__ho_lot_thuong_dung')[1]
           # rows3 = PAluong_list.values_list('Nhanvien__vitri_CV__Ten_Nhom_CV')[1]
           # rows4 = PAluong_list.values_list('Nhanvien__bo_phan__ten_bp')[1]

          #  ws.write(5, 2, "Chức danh công việc:", TIEUDE2)
            top_row8 = 5
            bottom_row8 = 5
            left_column8 = 3
            right_column8 = 5
           # ws.write_merge(top_row8, bottom_row8, left_column8, right_column8,   rows1, TIEUDE2) #cHỨC DANH

           # ws.write(6, 2, "Đơn vị:", TIEUDE2)

            top_rowdv = 6
            bottom_rowdv = 6
            left_columndv = 3
            right_columndv = 5
            STT =1
            #ws.write_merge(top_rowdv, bottom_rowdv, left_columndv, right_columndv,    rows3, TIEUDE2)
            #ws.write(7, 2, "Mã chức danh:", TIEUDE2)
            # ws.write(7,2,  rows4, TIEUDE2)
            row_num = 9
            for_left = xlwt.easyxf(
                "font: bold 1, color blue; borders: top double, bottom double, left double, right double; align: horiz left")

            TABLE_row=xlwt.easyxf(
                'font: bold 1, color white, name calibri, height 250;'
                'align: vertical center, horizontal center, wrap on;'
                'borders: left thin, right thin, top thin, bottom thin;'
                'pattern: pattern solid, pattern_fore_colour green;'
            )
            TABLE_HEADER=xlwt.easyxf(
                'font: bold 1, color blue, name calibri, height 250;'
                'align: vertical center, horizontal center, wrap on;'
                'borders: top double, bottom double, left double, right double;'
                'pattern: pattern solid, pattern_fore_colour yellow, pattern_back_colour dark_red_ega;'
            )
            # ----Định dạng chiều rộng cột
            ws.col(0).width = 2000
            ws.col(1).width = 8000
            ws.col(2).width = 8000
            ws.col(3).width = 7000
            ws.col(4).width = 4000
            ws.col(5).width = 4000
            ws.col(6).width = 4000
            ws.col(7).width = 4000
            ws.col(8).width = 4000
            ws.col(9).width = 4000
            ws.col(10).width = 4000

            columns = ['STT',  'Tên Nhân viên','Chức vụ', 'Đơn vị', 'Nhóm lương',
                       'Lương BHXH cũ', 'BHXH mới', 'Lương cũ',  'Lương mới', 'Chênh lệch BHXH', 'Chênh lệch lương ',]
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            # ----Định dạng chữ
            stt = 1
            font_style = xlwt.XFStyle()
            font_style.font.italic = False
            for_left = xlwt.easyxf(
                "font: color blue, name calibri, height 250; borders: left thin, right thin, top thin, bottom thin; pattern: pattern solid, fore_color white;")

            rows = PAluong_list.values_list( 'Nhanvien_id','Nhanvien__ho_lot_thuong_dung','Nhanvien__vitri_CV__Ten_Nhom_CV',
                                             'Nhanvien__bo_phan__ten_bp','Nhom_luong__Nhom_luong__nhom',
                                            'Luong_BHXH_cu', 'Luong_BHXH_moi', 'Luong_cu',  'Luong_moi', 'CL_Luong_BHXH_PA_1',
                                             'CL_Luong_moi_PA_1' )
            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    if (row[col_num]) != 0 and (row[col_num]) != 'I.NĂNG LỰC CHUNG' and (row[col_num]) != "II.NĂNG LỰC QUẢN LÝ" and (row[col_num]) != "III.NĂNG LỰC CHUYÊN MÔN"\
                            and (row[col_num]) != 'CH00' and (row[col_num]) != "QL00" and (row[col_num]) != "CM00":
                        ws.write(row_num, col_num, (row[col_num]),for_left)
                    else:
                        ws.write(row_num, col_num, (row[col_num]),TABLE_row)


            for_foot = xlwt.easyxf("font: color blue;  pattern: pattern solid, fore_color white;")
            for_foot_ng = xlwt.easyxf('font: color blue, name calibri, height 220;'
                                      'align: vertical center, horizontal center,')
            TABLE_HEADER2 = xlwt.easyxf(
                'font: bold 1, color blue, name calibri, height 220;'
                'align: vertical center, horizontal center;'
            )

            top_row2 = row_num + 1
            bottom_row2 = row_num + 1
            left_column2 = 0
            right_column2 = 2
            ws.write_merge(top_row2, bottom_row2, left_column2, right_column2, 'TỔNG ĐIỂM', TABLE_HEADER)
            ws.write(row_num + 1, 3,"",  TABLE_HEADER)
            ws.write(row_num + 1, 4,"",  TABLE_HEADER)

            ws.write(row_num + 1, 5, total_Luong_BHXH_cu, TABLE_HEADER)
            ws.write(row_num + 1, 6, total_Luong_BHXH_moi, TABLE_HEADER)
            ws.write(row_num + 1, 7, total_Luong_cu, TABLE_HEADER)

            ws.write(row_num + 1, 8, total_Luong_moi, TABLE_HEADER)
            ws.write(row_num + 1, 9, total_CL_Luong_BHXH_PA_1, TABLE_HEADER)
            ws.write(row_num + 1, 10, total_CL_Luong_moi_PA_1, TABLE_HEADER)

            ws.write(row_num + 5, 1, 'Ngày ... tháng ... năm 2023', for_foot_ng)
            ws.write(row_num + 6, 1, 'Người phê duyệt', TABLE_HEADER2)
            ws.write(row_num + 5, 3, 'Ngày .... tháng ... năm 2023', for_foot_ng)
            ws.write(row_num + 6, 3, 'Người xem xét', TABLE_HEADER2)
            ws.write(row_num + 5, 5, 'Ngày ... tháng ... năm 2023', for_foot_ng)
            # ws.write_merge(row_num + 18,row_num + 19, row_num + 20,row_num + 21,  'Người được đánh giá', TABLE_HEADER2)
            ws.write(row_num + 6, 5, 'Người thiết lập', TABLE_HEADER2)

            wb.save(responese)
            return responese



    context = { 'queryset': PAluong_list, 'form': form,'total_Luong_BHXH_cu': total_Luong_BHXH_cu, 'total_Luong_cu':total_Luong_cu,
                'total_Luong_BHXH_moi':total_Luong_BHXH_moi, 'total_Luong_moi':total_Luong_moi,
                'total_CL_Luong_BHXH_PA_1':total_CL_Luong_BHXH_PA_1, 'total_CL_Luong_moi_PA_1':total_CL_Luong_moi_PA_1,
                }

    return render(request,"luong/Phuonganluong.html",context)

def xepluong(request):
    form = Phuongan_luong_f(request.POST or None)
    PAluong_list = Phuongan_luongbhxh.objects.all()


    total_Luong_BHXH_cu = (PAluong_list.aggregate(total=Sum('Luong_BHXH_cu', field="Luong_BHXH_cu"))['total'])
    total_Luong_BHXH_moi = (PAluong_list.aggregate(total=Sum('Luong_BHXH_moi', field="Luong_BHXH_moi"))['total'])
    total_Luong_cu = (PAluong_list.aggregate(total=Sum('Luong_cu', field="Luong_cu"))['total'])
    total_Luong_moi = (PAluong_list.aggregate(total=Sum('Luong_moi', field="Luong_moi"))['total'])

    if total_Luong_BHXH_moi and total_Luong_BHXH_cu:
        CL_BHXH = total_Luong_BHXH_moi - total_Luong_BHXH_cu
    if total_Luong_moi and total_Luong_moi:
        CL_luong = total_Luong_moi - total_Luong_moi

    total_CL_Luong_BHXH_PA_1 = (PAluong_list.aggregate(total=Sum('CL_Luong_BHXH_PA_1', field="CL_Luong_BHXH_PA_1"))['total'])
    total_CL_Luong_moi_PA_1 = (PAluong_list.aggregate(total=Sum('CL_Luong_moi_PA_1', field="CL_Luong_moi_PA_1"))['total'])


    context = { 'queryset': PAluong_list, 'form': form,'total_Luong_BHXH_cu': total_Luong_BHXH_cu, 'total_Luong_cu':total_Luong_cu,
                'total_Luong_BHXH_moi':total_Luong_BHXH_moi, 'total_Luong_moi':total_Luong_moi,
                'total_CL_Luong_BHXH_PA_1':total_CL_Luong_BHXH_PA_1, 'total_CL_Luong_moi_PA_1':total_CL_Luong_moi_PA_1,
                }

    if form['Xuất_Excel'].value() == True:
            responese = HttpResponse(content_type='application/ms-excel')
            responese['Content-Disposition'] = 'attachment; filename=' +  'PAL.xls'

            wb = xlwt.Workbook(encoding='utf-8')


            ws = wb.add_sheet(str('chucdanh_CV'))

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
            ws.write_merge(top_row, bottom_row, left_column, right_column, 'PHƯƠNG ÁN CHUYỂN XẾP LƯƠNG', TIEUDEM)

           # rows1 = PAluong_list.values_list('Nhanvien__ho_lot_thuong_dung')[1]
           # rows3 = PAluong_list.values_list('Nhanvien__vitri_CV__Ten_Nhom_CV')[1]
           # rows4 = PAluong_list.values_list('Nhanvien__bo_phan__ten_bp')[1]

          #  ws.write(5, 2, "Chức danh công việc:", TIEUDE2)
            top_row8 = 5
            bottom_row8 = 5
            left_column8 = 3
            right_column8 = 5
           # ws.write_merge(top_row8, bottom_row8, left_column8, right_column8,   rows1, TIEUDE2) #cHỨC DANH

           # ws.write(6, 2, "Đơn vị:", TIEUDE2)

            top_rowdv = 6
            bottom_rowdv = 6
            left_columndv = 3
            right_columndv = 5
            STT =1
            #ws.write_merge(top_rowdv, bottom_rowdv, left_columndv, right_columndv,    rows3, TIEUDE2)
            #ws.write(7, 2, "Mã chức danh:", TIEUDE2)
            # ws.write(7,2,  rows4, TIEUDE2)
            row_num = 9
            for_left = xlwt.easyxf(
                "font: bold 1, color blue; borders: top double, bottom double, left double, right double; align: horiz left")

            TABLE_row=xlwt.easyxf(
                'font: bold 1, color white, name calibri, height 250;'
                'align: vertical center, horizontal center, wrap on;'
                'borders: left thin, right thin, top thin, bottom thin;'
                'pattern: pattern solid, pattern_fore_colour green;'
            )
            TABLE_HEADER=xlwt.easyxf(
                'font: bold 1, color blue, name calibri, height 250;'
                'align: vertical center, horizontal center, wrap on;'
                'borders: top double, bottom double, left double, right double;'
                'pattern: pattern solid, pattern_fore_colour yellow, pattern_back_colour dark_red_ega;'
            )
            # ----Định dạng chiều rộng cột
            ws.col(0).width = 2000
            ws.col(1).width = 8000
            ws.col(2).width = 8000
            ws.col(3).width = 7000
            ws.col(4).width = 4000
            ws.col(5).width = 4000
            ws.col(6).width = 4000
            ws.col(7).width = 4000
            ws.col(8).width = 4000
            ws.col(9).width = 4000
            ws.col(10).width = 4000

            columns = ['STT',  'Tên Nhân viên','Chức vụ', 'Đơn vị', 'Nhóm lương',
                       'Lương BHXH cũ', 'BHXH mới', 'Lương cũ',  'Lương mới', 'Chênh lệch BHXH', 'Chênh lệch lương ',]
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            # ----Định dạng chữ
            stt = 1
            font_style = xlwt.XFStyle()
            font_style.font.italic = False
            for_left = xlwt.easyxf(
                "font: color blue, name calibri, height 250; borders: left thin, right thin, top thin, bottom thin; pattern: pattern solid, fore_color white;")

            rows = PAluong_list.values_list( 'Nhanvien_id','Nhanvien__ho_lot_thuong_dung','Nhanvien__vitri_CV__Ten_Nhom_CV',
                                             'Nhanvien__bo_phan__ten_bp','Nhom_luong__Nhom_luong__nhom',
                                            'Luong_BHXH_cu', 'Luong_BHXH_moi', 'Luong_cu',  'Luong_moi', 'CL_Luong_BHXH_PA_1',
                                             'CL_Luong_moi_PA_1' )
            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    if (row[col_num]) != 0 and (row[col_num]) != 'I.NĂNG LỰC CHUNG' and (row[col_num]) != "II.NĂNG LỰC QUẢN LÝ" and (row[col_num]) != "III.NĂNG LỰC CHUYÊN MÔN"\
                            and (row[col_num]) != 'CH00' and (row[col_num]) != "QL00" and (row[col_num]) != "CM00":
                        ws.write(row_num, col_num, (row[col_num]),for_left)
                    else:
                        ws.write(row_num, col_num, (row[col_num]),TABLE_row)


            for_foot = xlwt.easyxf("font: color blue;  pattern: pattern solid, fore_color white;")
            for_foot_ng = xlwt.easyxf('font: color blue, name calibri, height 220;'
                                      'align: vertical center, horizontal center,')
            TABLE_HEADER2 = xlwt.easyxf(
                'font: bold 1, color blue, name calibri, height 220;'
                'align: vertical center, horizontal center;'
            )

            top_row2 = row_num + 1
            bottom_row2 = row_num + 1
            left_column2 = 0
            right_column2 = 2
            ws.write_merge(top_row2, bottom_row2, left_column2, right_column2, 'TỔNG ĐIỂM', TABLE_HEADER)
            ws.write(row_num + 1, 3,"",  TABLE_HEADER)
            ws.write(row_num + 1, 4,"",  TABLE_HEADER)

            ws.write(row_num + 1, 5, total_Luong_BHXH_cu, TABLE_HEADER)
            ws.write(row_num + 1, 6, total_Luong_BHXH_moi, TABLE_HEADER)
            ws.write(row_num + 1, 7, total_Luong_cu, TABLE_HEADER)

            ws.write(row_num + 1, 8, total_Luong_moi, TABLE_HEADER)
            ws.write(row_num + 1, 9, total_CL_Luong_BHXH_PA_1, TABLE_HEADER)
            ws.write(row_num + 1, 10, total_CL_Luong_moi_PA_1, TABLE_HEADER)

            ws.write(row_num + 5, 1, 'Ngày ... tháng ... năm 2023', for_foot_ng)
            ws.write(row_num + 6, 1, 'Người phê duyệt', TABLE_HEADER2)
            ws.write(row_num + 5, 3, 'Ngày .... tháng ... năm 2023', for_foot_ng)
            ws.write(row_num + 6, 3, 'Người xem xét', TABLE_HEADER2)
            ws.write(row_num + 5, 5, 'Ngày ... tháng ... năm 2023', for_foot_ng)
            # ws.write_merge(row_num + 18,row_num + 19, row_num + 20,row_num + 21,  'Người được đánh giá', TABLE_HEADER2)
            ws.write(row_num + 6, 5, 'Người thiết lập', TABLE_HEADER2)

            wb.save(responese)
            return responese



    context = { 'queryset': PAluong_list, 'form': form,'total_Luong_BHXH_cu': total_Luong_BHXH_cu, 'total_Luong_cu':total_Luong_cu,
                'total_Luong_BHXH_moi':total_Luong_BHXH_moi, 'total_Luong_moi':total_Luong_moi,
                'total_CL_Luong_BHXH_PA_1':total_CL_Luong_BHXH_PA_1, 'total_CL_Luong_moi_PA_1':total_CL_Luong_moi_PA_1,
                }

    return render(request,"luong/Phuonganluong.html",context)

@login_required
def add_paluong(request):
    Nhanvien_danhgia = Nhan_vien.objects.all()
    if request.method == 'POST':
        data = request.POST
        nhanviens = Nhan_vien.objects.filter(da_nghiviec = False)
        luongbhs = bangluong_BHXH.objects.filter()
        luongs = bangluong_chinh.objects.filter()
        for luong in luongs:
            for luong_bh in luongbhs:
                for nhanvien in nhanviens:
                    if luong_bh.diem == nhanvien.vitri_CV and luong.diem == nhanvien.vitri_CV and luong_bh.Bac_2 and luong.Bac_2:
                        khoa_hoc = Phuongan_luongbhxh.objects.update_or_create(
                        Nhanvien=nhanvien, Nhom_luong=luong,
                        Nhom_luongBH = luong_bh,
                        Luong_cu = nhanvien.Luong_cu,
                        Luong_BHXH_cu = nhanvien.Luong_BHXH_cu,

                        Luong_BHXH_moi = luong_bh.Bac_2 * luong.luong_toi_thieu,
                        Luong_moi = luong.Bac_2 * luong.luong_toi_thieu,
                        CL_Luong_moi_PA_1 = (luong.Bac_2 * luong.luong_toi_thieu) - nhanvien.Luong_cu,
                        CL_Luong_BHXH_PA_1 = (luong_bh.Bac_2 * luong_bh.luong_toi_thieu) - nhanvien.Luong_BHXH_cu,
                       )

                else:
                    continue
        return redirect('xepluong')
    context = {'Nhanvien_danhgias': Nhanvien_danhgia}
    return render(request, 'luong/PaChuyenxep_luong.html')


#
@login_required
def add_bangluong(request):
    Nhanvien_danhgia = Nhan_vien.objects.all()
    if request.method == 'POST':
        data = request.POST
        diems = Mota_Cv7.objects.filter()
        Nhom_luongs = TK_ngach.objects.filter()
        for Nhom_luong in Nhom_luongs:
            for diem in diems:
                if Nhom_luong.diem == diem.tong_diem7:
                    khoa_hoc = bangluong_chinh.objects.update_or_create(
                        Nhom_luong=Nhom_luong,
                        diem=diem,
                        tong_diem = diem.tong_diem7,
                        luong_toi_thieu = data['luong_toi_thieu'],
                        Boiso = "1.20",
                        Bac_1 = Nhom_luong.bac_1,
                        Bac_2 = Nhom_luong.bac_2,
                        Bac_3 = Nhom_luong.bac_3,
                        Bac_4 = Nhom_luong.bac_4,
                        Bac_5 = Nhom_luong.bac_5,
                       )
                    BHXH = bangluong_BHXH.objects.update_or_create(
                        Nhom_luong=Nhom_luong,
                        diem=diem,
                        tong_diem = diem.tong_diem7,
                        luong_toi_thieu = data['luong_toi_thieu'],
                        Boiso = "1.20",
                        Bac_1 = Nhom_luong.bac_1_BHXH,
                        Bac_2 = Nhom_luong.bac_2_BHXH,
                        Bac_3 = Nhom_luong.bac_3_BHXH,
                        Bac_4 = Nhom_luong.bac_4_BHXH,
                        Bac_5 = Nhom_luong.bac_5_BHXH,
                       )
                else:
                    continue
        return redirect('bangluong_list')
    context = {'Nhanvien_danhgias': Nhanvien_danhgia}
    return render(request, 'luong/Bangluong_chinh_add.html')


@login_required
def bangluong_BHXH_list(request):
    form = bangluong_list_f(request.POST or None)
    l0= bangluong_BHXH.objects.all()
    l1= bangluong_BHXH.objects.filter(Nhom_luong__nhom ="1")[0:1]
    l2= bangluong_BHXH.objects.filter(Nhom_luong__nhom ="2")[0:1]
    l3= bangluong_BHXH.objects.filter(Nhom_luong__nhom ="3")[0:1]
    l4= bangluong_BHXH.objects.filter(Nhom_luong__nhom ="4")[0:1]
    l5= bangluong_BHXH.objects.filter(Nhom_luong__nhom ="5")[0:1]
    l6= bangluong_BHXH.objects.filter(Nhom_luong__nhom ="6")[0:1]
    l7= bangluong_BHXH.objects.filter(Nhom_luong__nhom ="7")[0:1]
    l8= bangluong_BHXH.objects.filter(Nhom_luong__nhom ="8")[0:1]
    l9= bangluong_BHXH.objects.filter(Nhom_luong__nhom ="9")[0:1]
    l10= bangluong_BHXH.objects.filter(Nhom_luong__nhom ="10")[0:1]
    l11= bangluong_BHXH.objects.filter(Nhom_luong__nhom ="11")[0:1]
    l12= bangluong_BHXH.objects.filter(Nhom_luong__nhom ="12")[0:1]
    l13= bangluong_BHXH.objects.filter(Nhom_luong__nhom ="13")[0:1]
    l14= bangluong_BHXH.objects.filter(Nhom_luong__nhom ="14")[0:1]
    l15= bangluong_BHXH.objects.filter(Nhom_luong__nhom ="15")[0:1]
    l16= bangluong_BHXH.objects.filter(Nhom_luong__nhom ="16")[0:1]
    context = {'productss':l0,'l0':l0, 'l1': l1,'l2': l2,'l3': l3,'l4': l4,'l5': l5,'l6': l6,'l7': l7,'l8': l8,'l9': l9,
              'l10': l10 ,'l11': l11,'l12': l12,'l13': l13,'l14': l14,'l15': l15,'l16': l16,'form':form,}
    return render(request,'luong/bangluong_bhxh.html', context)


def bangluong_chinh_list(request):
    form = bangluong_list_f(request.POST or None)
    l0= bangluong_chinh.objects.all()
    l1= bangluong_chinh.objects.filter(Nhom_luong__nhom ="1")[0:1]
    l2= bangluong_chinh.objects.filter(Nhom_luong__nhom ="2")[0:1]
    l3= bangluong_chinh.objects.filter(Nhom_luong__nhom ="3")[0:1]
    l4= bangluong_chinh.objects.filter(Nhom_luong__nhom ="4")[0:1]
    l5= bangluong_chinh.objects.filter(Nhom_luong__nhom ="5")[0:1]
    l6= bangluong_chinh.objects.filter(Nhom_luong__nhom ="6")[0:1]
    l7= bangluong_chinh.objects.filter(Nhom_luong__nhom ="7")[0:1]
    l8= bangluong_chinh.objects.filter(Nhom_luong__nhom ="8")[0:1]
    l9= bangluong_chinh.objects.filter(Nhom_luong__nhom ="9")[0:1]
    l10= bangluong_chinh.objects.filter(Nhom_luong__nhom ="10")[0:1]
    l11= bangluong_chinh.objects.filter(Nhom_luong__nhom ="11")[0:1]
    l12= bangluong_chinh.objects.filter(Nhom_luong__nhom ="12")[0:1]
    l13= bangluong_chinh.objects.filter(Nhom_luong__nhom ="13")[0:1]
    l14= bangluong_chinh.objects.filter(Nhom_luong__nhom ="14")[0:1]
    l15= bangluong_chinh.objects.filter(Nhom_luong__nhom ="15")[0:1]
    l16= bangluong_chinh.objects.filter(Nhom_luong__nhom ="16")[0:1]


    context = {'productss':l0,'l0':l0, 'l1': l1,'l2': l2,'l3': l3,'l4': l4,'l5': l5,'l6': l6,'l7': l7,'l8': l8,'l9': l9,
              'l10': l10 ,'l11': l11,'l12': l12,'l13': l13,'l14': l14,'l15': l15,'l16': l16,'form':form,}
    return render(request,'luong/bangluong_chinh.html', context)


#-----------Bắt đầu quản lý hợp đồng lao động-----------------------------------------
def is_valid_queryparam(param):
    return param != '' and param is not None
def filter(request):
    qs = hd_laodong.objects.filter(Hieuluc=1)
    qs_1 = qs[0:1]
  #  ho_lot_thuong_dung_contains_query = request.GET.get('ho_lot_thuong_dung_contains')
 #   id_nhanvien_query = request.GET.get('id_nhanvien')
    ho_lot_thuong_dung_or_chucvu_query = request.GET.get('ho_lot_thuong_dung_or_chucvu')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    category = request.GET.get('category')
    Hieuluc = request.GET.get('Hieuluc')
    loai_HD = request.GET.get('loai_HD')
    Xuất_Excel =request.GET.get('Xuất_Excel')

    if is_valid_queryparam(ho_lot_thuong_dung_or_chucvu_query):
        qs = qs.filter(Q(Ho_ten__ho_lot_thuong_dung__icontains=ho_lot_thuong_dung_or_chucvu_query)
                       | Q(Ho_ten__vitri_CV__Ten_Nhom_CV__icontains=ho_lot_thuong_dung_or_chucvu_query)
                       | Q(Ho_ten__id__icontains=ho_lot_thuong_dung_or_chucvu_query)
                       ).distinct()

    if is_valid_queryparam(date_min):
        qs = qs.filter(Tu_ngay__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(Tu_ngay__lt=date_max)

    elif is_valid_queryparam(category) and category != 'Chọn ...':
        qs = qs.filter(Ho_ten__don_vi__Ten_DV=category)

    elif is_valid_queryparam(loai_HD) and loai_HD != 'Chọn ...':
        qs = qs.filter(Loai_hd=loai_HD)

    elif Hieuluc == 'on':
        qs = Nhan_vien.objects.filter(Hieuluc=True)
    return qs




def nhanvien_hopdong(request, id):
    form = hd_laodong_list_f(request.POST or None)
    queryset_hopdong_Nhanvien = hd_laodong.objects.filter(Ho_ten_id=id)
    context = {'queryset': queryset_hopdong_Nhanvien,'form':form,}
    return render(request,'luong/hopdong_list_nhanvien.html', context)


@login_required
def add_hopdong(request):
    if request.method == 'POST':
        data = request.POST
        nhanviens = Nhan_vien.objects.filter(da_nghiviec=0)
        for nhanvien in nhanviens:
            khoa_hoc = hd_laodong.objects.get_or_create(
                    So_hopdong=data['name'],
                    Hoten_nhanvien = data['name'],
                    Ho_ten=nhanvien,
                    Ht_traluong = 'Khoán',
                    Loai_hd = 'Thử việc',
                    Tu_ngay = '2021-03-30',
                    Den_ngay = '2021-05-30',
                    Ly_do = "Ký mới",
                    Hieuluc = 1,
                )
        return redirect('hopdong_view')
    return render(request, 'luong/Hopdong_add.html')

@login_required
def luong_tamung_add(request):
    if request.method == 'POST':
        data = request.POST
        nhanviens = Nhan_vien.objects.filter(da_nghiviec=0)
        for nhanvien in nhanviens:
            khoa_hoc = luongthang.objects.get_or_create(
                    Thang_tra_luong=data['thang'],
                    Nam = data['nam'],
                    hoten_nhanvien=nhanvien,
                    Tam_ung = 100000000,

                )
        return redirect('luongthang_tamung')
    return render(request, 'luong/Tamung_add.html')

@login_required
def add_nangluong(request):
    if request.method == 'POST':
        data = request.POST
        nhanviens = Nhan_vien.objects.filter(da_nghiviec=0)
        for nhanvien in nhanviens:
            khoa_hoc = hd_laodong.objects.get_or_create(
                    So_hopdong=data['name'],
                    Hoten_nhanvien = data['name'],
                    Ho_ten=nhanvien,
                    Ht_traluong = 'Khoán',
                    Loai_hd = 'Thử việc',
                    Tu_ngay = '2021-03-30',
                    Den_ngay = '2021-05-30',
                    Ly_do = "Ký mới",
                    Hieuluc = 1,
                )
        return redirect('hopdong_view')
    return render(request, 'luong/Nangluong_add.html')


#----------------
def nangluong_view(request):
   qs = filter(request)
   qs_1 = qs[0:10]
   hopdong_s = ('Có thời hạn','Không thời hạn', 'Thử việc')
   context = {'queryset': qs,'queryset_1':qs_1,
               'categories' : Don_vi.objects.all(),
               'hopdong_s':  hopdong_s
    }
   return render(request,'luong/Nangluong_list_new.html', context)


def update_nangluong_1(request, id):
    if request.method == 'POST':
        dv = hd_laodong.objects.get(pk=id)
        fmhd = nangluong(request.POST, instance=dv)
        if fmhd.is_valid():
            fmhd.save()
            messages.success(request, 'Dữ liệu cập nhật')
    else:
        dv = hd_laodong.objects.get(pk=id)
        fmhd = nangluong(instance=dv)
    return render(request,'luong/nangluong_up.html', {'form': fmhd})

#--------------------
def update_nangluong(request, id):
    if request.method == 'POST':
        dv = hd_laodong.objects.get(pk=id)
        fmhd = nangluong(request.POST, instance=dv)
        if fmhd.is_valid():
            fmhd.save()
            messages.success(request, 'Dữ liệu cập nhật')
    else:
        dv = hd_laodong.objects.get(pk=id)
        fmhd = nangluong(instance=dv)

    if fmhd['Xuất_Word'].value() == True:
        doc = DocxTemplate("word_template/M_nangluong.docx")
        pnv = hd_laodong.objects.get(id=id)
        queryset4 = {
                  "Ho_ten":pnv.Ho_ten,
                  "Chuc_danh":pnv.Ho_ten.vitri_CV,
                  "Don_vi":pnv.Ho_ten.don_vi.Ten_DV,

                  "Heso":pnv.Heso,
                  "Bac":pnv.Bac,
                  "Nhom_luong":pnv.bangluong.Nhom_luong,
                    }
        doc.render(queryset4)
        doc.save('thu_word/QD_nang_luong_'+ str(pnv.Ho_ten)+ '.docx')
    context = {'form':fmhd, }
    return render(request,'luong/nangluong_up.html', context)

# This functions will delete/xóa
def del_nangluong(request, id):
    dv = hd_laodong.objects.get(pk=id)
    if request.method == 'POST':
        dv.delete()
        return HttpResponseRedirect('/hopdong/')
    return render(request, 'luong/nangluong_delete.html')
        #return redirect('/')


#---Điều động-------------------------------
def dieu_dong_view(request):
    qs = filter(request)
    qs_1 = qs[0:10]
    hopdong_s = ('Có thời hạn','Không thời hạn', 'Thử việc')
    context = {'queryset_1': qs,'queryset':qs_1,
               'categories' : Don_vi.objects.all(),
               'hopdong_s':  hopdong_s
    }
    return render(request,'luong/dieu_dong_list.html', context)



def update_dieu_dong(request, id):
    if request.method == 'POST':
        dv = hd_laodong.objects.get(pk=id)
        fmhd = nangluong(request.POST, instance=dv)
        if fmhd.is_valid():
            fmhd.save()
            messages.success(request, 'Dữ liệu cập nhật')
    else:
        dv = hd_laodong.objects.get(pk=id)
        fmhd = nangluong(instance=dv)

    if fmhd['Xuất_Word'].value() == True:
        doc = DocxTemplate("word_template/M_Dieudong.docx")
        pnv = hd_laodong.objects.get(id=id)
        queryset4 = {
                  "Ho_ten":pnv.Ho_ten,
                  "Chuc_danh":pnv.Ho_ten.vitri_CV,
                  "Don_vi":pnv.Ho_ten.don_vi.Ten_DV,

                  "Heso":pnv.Heso,
                  "Bac":pnv.Bac,
                  "Nhom_luong":pnv.bangluong.Nhom_luong,
                    }
        doc.render(queryset4)
        doc.save('thu_word/QD_Dieudong_'+ str(pnv.Ho_ten)+ '.docx')
    context = {'form':fmhd, }
    return render(request,'luong/dieudong_up.html', context)


def del_dieu_dong(request, id):
    dv = hd_laodong.objects.get(pk=id)
    if request.method == 'POST':
        dv.delete()
        return HttpResponseRedirect('/hopdong/')
    return render(request, 'luong/nangluong_delete.html')

#----------------ĐIỀU ĐỘNG NHÂN SỰ-----------------


def bo_nhiem_view(request):
    qs = filter(request)
    qs_1 = qs[0:10]
    hopdong_s = ('Có thời hạn','Không thời hạn', 'Thử việc')
    context = {'queryset_1': qs,'queryset':qs_1,
               'categories' : Don_vi.objects.all(),
               'hopdong_s':  hopdong_s
    }
    return render(request,'luong/Bo_nhiem_list.html', context)

def update_bonhiem(request, id):
    if request.method == 'POST':
        dv = hd_laodong.objects.get(pk=id)
        fmhd = nangluong(request.POST, instance=dv)
        if fmhd.is_valid():
            fmhd.save()
            messages.success(request, 'Dữ liệu cập nhật')
    else:
        dv = hd_laodong.objects.get(pk=id)
        fmhd = nangluong(instance=dv)

    if fmhd['Xuất_Word'].value() == True:
        doc = DocxTemplate("word_template/M_Bo_nhiem.docx")
        pnv = hd_laodong.objects.get(id=id)
        queryset4 = {
                  "Ho_ten":pnv.Ho_ten,
                  "Chuc_danh":pnv.Ho_ten.vitri_CV,
                  "Don_vi":pnv.Ho_ten.don_vi.Ten_DV,

                  "Heso":pnv.Heso,
                  "Bac":pnv.Bac,
                  "Nhom_luong":pnv.bangluong.Nhom_luong,
                    }
        doc.render(queryset4)
        doc.save('thu_word/QD_Bo_nhiem_'+ str(pnv.Ho_ten)+ '.docx')
    context = {'form':fmhd, }
    return render(request,'luong/Bo_nhiem_up.html', context)

def del_bonhiem(request, id):
    dv = hd_laodong.objects.get(pk=id)
    if request.method == 'POST':
        dv.delete()
        return HttpResponseRedirect('/hopdong/')
    return render(request, 'luong/nangluong_delete.html')





def hopdong_view(request):
    qs = filter(request)
    qs_1 = qs[0:10]

    hopdong_s = ('Có thời hạn','Không thời hạn', 'Thử việc')

    context = {'queryset': qs,'queryset_1':qs_1,
               'categories' : Don_vi.objects.all(),
               'hopdong_s':  hopdong_s,

    }
    return render(request,'luong/hopdong_list_new.html', context)


def update_hopdong(request, id):
    if request.method == 'POST':
        dv = hd_laodong.objects.get(pk=id)
        fmhd = hd_laodong_list_f(request.POST, instance=dv)
        if fmhd.is_valid():
            fmhd.save()
    else:
        dv = hd_laodong.objects.get(pk=id)
        fmhd = hd_laodong_list_f(instance=dv)

    if fmhd['Xuất_Word'].value() == True:
        doc = DocxTemplate("word_template/M_hdld_2022.docx")
        pnv = hd_laodong.objects.get(id=id)
        queryset2 = {
                  "Ho_ten":pnv.Ho_ten,
                  "Loai_hd":pnv.Loai_hd,
                  "Tu_ngay":pnv.Tu_ngay,
                  "Nhan_vien_dcthuongtru":pnv.Ho_ten.dc_thuong_tru,
                  "Nhan_vien_gioitinh":pnv.Ho_ten.Gioi_tinh,
                  "Nhan_vien_cmnd":pnv.Ho_ten.so_CCCD,
                  "Nhan_vien_cmnd_ngay":pnv.Ho_ten.ngay_cap_CCCD,
                  "Nhan_vien_noicap_cmnd":pnv.Ho_ten.quoctich,
                  "Heso":pnv.Heso,
                  "Muc_luong":pnv.Muc_luong,
                   "bannerImg" : InlineImage(doc, "thu_word/party_banner_2.png"),
                    }
        doc.render(queryset2)
        doc.save('thu_word/hdld_'+ str(pnv.Ho_ten)+ '.docx')
        file=open('thu_word/hdld_'+ str(pnv.Ho_ten)+ '.docx')

        messages.info(request, "Hợp đồng đã được mở trong file MS.Word.")
        messages.warning(request, "Hợp đồng đã được mở trong file MS.Word.")

    return render(request,'luong/hopdong_up.html', {'form': fmhd})


def chamdut_hopdong(request, id):
    if request.method == 'POST':
        dv = hd_laodong.objects.get(pk=id)
        f_ketthuc_hopdong = ketthuc_laodong_f(request.POST, instance=dv)
        if f_ketthuc_hopdong.is_valid():
            f_ketthuc_hopdong.save()
    else:
        dv = hd_laodong.objects.get(pk=id)
        f_ketthuc_hopdong = ketthuc_laodong_f(instance=dv)

    if f_ketthuc_hopdong['Xuất_Word'].value() == True:
        doc = DocxTemplate("word_template/M_nghiviecnew.docx")
        pnv = hd_laodong.objects.get(id=id)
        queryset3 = {
                  "Ho_ten":pnv.Ho_ten,
                  "Chuc_danh":pnv.Ho_ten.vitri_CV,
                  "ngay_sinh":pnv.Ho_ten.ngay_sinh,
                  "dc_hiennay":pnv.Ho_ten.dc_thuong_tru,
                  "Don_vi":pnv.Ho_ten.don_vi.Ten_DV,
                  "ngay_vao_dv":pnv.Ho_ten.ngay_vao_dv,
                    }
        doc.render(queryset3)
        doc.save('thu_word/HSNV_'+ str(pnv.Ho_ten)+ '.docx')

    return render(request,'luong/hopdong_chamdut.html', {'form': f_ketthuc_hopdong})

# This functions will delete/xóa
def del_hopdong(request, id):
    dv = hd_laodong.objects.get(pk=id)
    if request.method == 'POST':
        dv.delete()
        return HttpResponseRedirect('/hopdong/')
    return render(request, 'luong/hopdong_delete.html')
        #return redirect('/')


#-------- in hợp đồng chi tiết
def hopdongchitiet(request, id):

    pnv = hd_laodong.objects.get(id=id)
    return render(request, 'luong/hophong_nhanvien_chitiet.html', {'form_hd_nhanvien': pnv})


def hopdongketthuc(request, id):
    doc = DocxTemplate("word_template/M_nghiviec.docx")
    pnv = hd_laodong.objects.get(id=id)
    queryset3 = {
              "Ho_ten":pnv.Ho_ten,
              "Chuc_danh":pnv.Ho_ten.vitri_CV,
              "ngay_sinh":pnv.Ho_ten.ngay_sinh,
              "dc_hiennay":pnv.Ho_ten.dc_thuong_tru,
              "Don_vi":pnv.Ho_ten.don_vi.Ten_DV,
              "ngay_vao_dv":pnv.Ho_ten.ngay_vao_dv,
                }
    doc.render(queryset3)
    doc.save('thu_word/HSNV_'+ str(pnv.Ho_ten)+ '.docx')
    doc.open('thu_word/HSNV_'+ str(pnv.Ho_ten)+ '.docx')
    return render(request, 'luong/hophong_nhanvien_chitiet.html', {'form_hd_nhanvien': pnv})

#------------------KẾT THÚC QUẢN LÝ HỢP ĐỒNG LAO ĐỘNG....................................


@login_required
def bangluong_list(request):
    form = bangluong_list_f(request.POST or None)
    l0= bangluong.objects.all()
    l1= bangluong.objects.filter(Nhom_luong ="Ngạch 1")[0:7]
    l2= bangluong.objects.filter(Nhom_luong ="Ngạch 2")[0:7]
    l3= bangluong.objects.filter(Nhom_luong ="Ngạch 3")[0:7]
    l4= bangluong.objects.filter(Nhom_luong ="Ngạch 4")[0:7]
    l5= bangluong.objects.filter(Nhom_luong ="Ngạch 5")[0:7]
    l6= bangluong.objects.filter(Nhom_luong ="Ngạch 6")[0:7]
    l7= bangluong.objects.filter(Nhom_luong ="Ngạch 7")[0:7]
    l8= bangluong.objects.filter(Nhom_luong ="Ngạch 8")[0:7]
    l9= bangluong.objects.filter(Nhom_luong ="Ngạch 9")[0:7]
    l10= bangluong.objects.filter(Nhom_luong ="Ngạch 10")[0:7]
    l11= bangluong.objects.filter(Nhom_luong ="Ngạch 11")[0:7]
    l12= bangluong.objects.filter(Nhom_luong ="Ngạch 12")[0:7]
    l13= bangluong.objects.filter(Nhom_luong ="Ngạch 13")[0:7]
    l14= bangluong.objects.filter(Nhom_luong ="Ngạch 14")[0:7]
    l15= bangluong.objects.filter(Nhom_luong ="Ngạch 15")[0:7]
    l16= bangluong.objects.filter(Nhom_luong ="Ngạch 16")[0:7]
    l17= bangluong.objects.filter(Nhom_luong ="Ngạch 17")[0:7]
    l18= bangluong.objects.filter(Nhom_luong ="Ngạch 18")[0:7]
    l19= bangluong.objects.filter(Nhom_luong ="Ngạch 19")[0:7]
    context = {'l0':l0, 'l1': l1,'l2': l2,'l3': l3,'l4': l4,'l5': l5,'l6': l6,'l7': l7,'l8': l8,'l9': l9,
              'l10': l10 ,'l11': l11,'l12': l12,'l13': l13,'l14': l14,'l15': l15,'l16': l16,'l17': l17,'l18': l18,'l19': l19,'form':form,}
    return render(request,'luong/bangluong_list.html', context)



@login_required
def luong_thang(request):
    form = luongthang_f(request.POST or None)
    queryset = luongthang.objects.all() [1:100]
    Nhan_vien= luongthang.objects.filter()
    Thang_tra_luong= luongthang.objects.filter()
    Nam= luongthang.objects.filter()

   # context = {'queryset': queryset,'form':form,'Nhan_vien':Nhan_vien,'thang':thang, 'Nam':Nam, 'don_vi': don_vi, 'bo-phan':bo_phan}


    context = {'queryset': queryset,'form':form,'Nhan_vien':Nhan_vien,'Thang_tra_luong':Thang_tra_luong, 'Nam':Nam}
    if request.method == 'POST':
        bo_phan=form['bo_phan'].value()
        queryset=luongthang.objects.filter(Thang_tra_luong=form['Thang_tra_luong'].value(), Nam=form['Nam'].value())

        if (bo_phan !=  ''):
            queryset = luongthang.objects.filter(bo_phan_id=form['bo_phan'].value()).filter(Thang_tra_luong=form['Thang_tra_luong'].value(), Nam=form['Nam'].value())
    context = {'queryset': queryset,'form':form,'Nhan_vien':Nhan_vien,'Thang_tra_luong':Thang_tra_luong, 'Nam':Nam}

    if form['Xuất_Excel'].value() == True:
            responese = HttpResponse(content_type='application/ms-excel')
            responese['Content-Disposition'] = 'attachment; filename=Danh sách dinhgia'+ \
                    str(datetime.datetime.now())+'.xls'
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
            ws.write_merge(top_row, bottom_row, left_column, right_column, 'BẢNG LƯƠNG', TIEUDEM)

            rows1 = queryset.values_list('Thang_tra_luong')[1]
            rows2 = queryset.values_list('Nam')[1]
            print(rows2)
            rows3 = queryset.values_list('hoten_nhanvien__don_vi__Ten_DV')[1]
            row_phay = ("- ",)

            ws.write(6, 2, "Tháng/năm:", TIEUDE1)
            ws.write(6, 3, rows1 +row_phay+ rows2, TIEUDE2)
            ws.write(7, 2, "Đơn vị:", TIEUDE1)
            ws.write(7, 3, rows3, TIEUDE2)



        #----kẾT THÚC TIÊU ĐỀ:
            row_num = 9
            for_left = xlwt.easyxf("font: bold 1, color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            TABLE_HEADER = xlwt.easyxf(
                'font: bold 1, color blue, name Tahoma, height 220;'
                'align: vertical center, horizontal center, wrap on;'
                'borders: top double, bottom double, left double, right double;'
                'pattern: pattern solid, pattern_fore_colour yellow, pattern_back_colour dark_red_ega;'
                                       )
              #----Định dạng chiều rộng cột
            ws.col(0).width = 2000
            ws.col(1).width = 6000
            ws.col(2).width = 6000
            ws.col(3).width = 6000
            ws.col(4).width = 6000
            ws.col(5).width = 6000
            ws.col(6).width = 6000
            ws.col(7).width = 2000
            ws.col(8).width = 2200
            ws.col(9).width = 2000
            ws.col(10).width = 2000
            ws.col(11).width = 2000
            ws.col(12).width = 2200
            ws.col(13).width = 2000
            ws.col(14).width = 2000
            ws.col(15).width = 2000
            ws.col(16).width = 2200
            ws.col(17).width = 2000

            columns =['Số TT','Họ tên','Chức vụ', 'Đơn vị', 'Số Tài khoản', 'Ngân hàng','Hệ số', 'Mức lương', 'Tạm ứng', 'Lương', 'Hệ số P P2', 'Hệ số P3',  'Số giờ làm thêm',
                      'Số giờ làm thêm T7+CN', 'Số giờ làm thêm ngày lễ', 'Phụ câp KN', 'Phụ cấp khác',
            'Tiền ăn', 'Lương tháng', 'Ngày công', 'Boiduong_dochai', 'Tổng thu nhập', 'Trừ thuế', 'Trừ BHXH',
            'Trừ KPCĐ', 'Trừ_khac', 'Lương thêm giờ', 'Lương T7+CN', 'Luong thêm giờ N.lễ', 'Thu nhập còn lại'

                      ]
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            #----Định dạng chữ
            font_style= xlwt.XFStyle()
            font_style.font.italic = False
            for_left = xlwt.easyxf("font: color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            rows= queryset.values_list('id', 'hoten_nhanvien__ho_lot_thuong_dung', 'hoten_nhanvien__vitri_CV__Ten_Nhom_CV',  'hoten_nhanvien__don_vi__Ten_DV',
                                       'hoten_nhanvien__Taikhoan_nh','hoten_nhanvien__Ten_nganhang','Heso', 'Muc_luongBHXH', 'Tam_ung', 'Muc_luong', 'luong_p2', 'luong_p3',  'Gio_lam_them', 'Gio_lam_them_CT', 'Gio_lam_them_le', 'phucap_knhiem', 'phucap_khac',
            'Tien_an', 'Luong_thang', 'Ngay_cong', 'Boiduong_dochai', 'Thu_nhap', 'kn_thuetncn', 'kn_BHXH_BYTT',
            'kn_KPCĐ', 'kn_khac', 'luong_themgio', 'Luong_lamthemT7', 'Luong_lamthemle', 'Thu_nhapthuclinh')

            for row in rows:
                row_num +=1
                for col_num in range(len(row)):
                    ws.write(row_num,col_num, str(row[col_num]), for_left)

            wb.save(responese)
            return responese
    context = {'queryset': queryset,'form':form,'Nhan_vien':Nhan_vien,'thang':Thang_tra_luong, 'Nam':Nam,}
    return render(request,'luong/Luong_thang.html', context)



def update_luong(request, id):
    if request.method == 'POST':
        dv = luongthang.objects.get(pk=id)
        fmdv = luongthang_Form(request.POST, instance=dv)
        if fmdv.is_valid():
            fmdv.save()
    else:
        dv = luongthang.objects.get(pk=id)
        fmdv = luongthang_Form(instance=dv)
    return render(request,'mota_cv/dinhgia_up-2.html', {'form': fmdv})

# This functions will delete/xóa
def del_luong(request, id):
    dv = luongthang.objects.get(pk=id)
    if request.method == 'POST':
        dv.delete()
        return HttpResponseRedirect('/dinhgia/')
    return render(request, 'mota_cv/Dinhgia_delete.html')
        #return redirect('/')


#<<<<<<... Chương trình xem  Lương tháng chi tiết theo nhân viên:
@login_required
def luongthang_nhanvien(request, id):
    pnv = luongthang.objects.get(id=id)
    #form_nhanvien = luongthang_Form(request.POST, or)
    return render(request, 'luong/luongthang_nhanvien_chitiet_thu.html', {'form_nhanvien': pnv})





#<<<<<<...kết thúc Chương trình Lương tháng chi tiết theo nhân viên:
@login_required
def luongthang_tamung(request):
    form = luongthang_f(request.POST or None)
    queryset = luongthang.objects.all() [1:5]
  #  Nhan_vien= luongthang.objects.filter()
  #  Thang_tra_luong= luongthang.objects.filter()
   # Nam= luongthang.objects.filter()

    context = {'queryset': queryset,'form':form,}
    if request.method == 'POST':
        bo_phan=form['bo_phan'].value()
        queryset=luongthang.objects.filter(Thang_tra_luong=form['Thang_tra_luong'].value(), Nam=form['Nam'].value())

        if (bo_phan !=  ''):
            queryset = luongthang.objects.filter(bo_phan_id=form['bo_phan'].value()).filter(Thang_tra_luong=form['Thang_tra_luong'].value(), Nam=form['Nam'].value())
    context = {'queryset': queryset,'form':form,}


#<<<<<<... Chương trình xem  Lương tam ứng theo nhân viên:



#-----------------------------
    if form['Xuất_Excel'].value() == True:
            responese = HttpResponse(content_type='application/ms-excel')
            responese['Content-Disposition'] = 'attachment; filename=Danh sách dinhgia'+ \
                    str(datetime.datetime.now())+'.xls'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('nhanvien')
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            font_style.font.shadow = True
    #-----------------------------

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
            left_column7 = 4
            right_column7 = 8
            ws.write_merge(top_row7, bottom_row7, left_column7, right_column7,  'CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM', TIEUDE)

            top_row9 = 1
            bottom_row9 = 1
            left_column9 = 4
            right_column9 = 8
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
            ws.write_merge(top_row, bottom_row, left_column, right_column, 'BẢNG TẠM ỨNG LƯƠNG', TIEUDEM)

            rows1 = queryset.values_list('Thang_tra_luong')[1]
            rows2 = queryset.values_list('Nam')[1]
            print(rows2)
            rows3 = queryset.values_list('hoten_nhanvien__don_vi__Ten_DV')[1]
            row_phay = ("- ",)

            ws.write(6, 2, "Tháng/năm:", TIEUDE1)
            ws.write(6, 3, rows1 +row_phay+ rows2, TIEUDE2)
            ws.write(7, 2, "Đơn vị:", TIEUDE1)
            ws.write(7, 3, rows3, TIEUDE2)


        #----kẾT THÚC TIÊU ĐỀ:


            row_num = 9
            for_left = xlwt.easyxf("font: bold 1, color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            TABLE_HEADER = xlwt.easyxf(
                'font: bold 1, color blue, name Tahoma, height 220;'
                'align: vertical center, horizontal center, wrap on;'
                'borders: top double, bottom double, left double, right double;'
                'pattern: pattern solid, pattern_fore_colour yellow, pattern_back_colour dark_red_ega;'
                                       )
              #----Định dạng chiều rộng cột
            ws.col(0).width = 2000
            ws.col(1).width = 6000
            ws.col(2).width = 6000
            ws.col(3).width = 6000
            ws.col(4).width = 6000
            ws.col(5).width = 6000
            ws.col(6).width = 6000
            ws.col(7).width = 2000
            ws.col(8).width = 2200
            ws.col(9).width = 2000
            ws.col(10).width = 2000
            ws.col(11).width = 2000
            ws.col(12).width = 2200
            ws.col(13).width = 2000
            ws.col(14).width = 2000
            ws.col(15).width = 2000
            ws.col(16).width = 2200
            ws.col(17).width = 2000

            columns =['Số TT','Họ tên','Chức vụ', 'Đơn vị', 'Số Tài khoản', 'Ngân hàng', 'Tạm ứng',


                      ]
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            #----Định dạng chữ
            font_style= xlwt.XFStyle()
            font_style.font.italic = False
            for_left = xlwt.easyxf("font: color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            rows= queryset.values_list('id', 'hoten_nhanvien__ho_lot_thuong_dung', 'hoten_nhanvien__vitri_CV__Ten_Nhom_CV',  'hoten_nhanvien__don_vi__Ten_DV',
                                       'hoten_nhanvien__Taikhoan_nh',
                                       'hoten_nhanvien__Ten_nganhang',
                                       'Tam_ung', )

            for row in rows:
                row_num +=1
                for col_num in range(len(row)):
                    ws.write(row_num,col_num, str(row[col_num]), for_left)
            wb.save(responese)
            return responese
    context = {'queryset': queryset,'form':form,'Nhan_vien':Nhan_vien,}
    return render(request,'luong/luongthang_tamung_1.html', context)



def update_luong_tamung(request, id):
    if request.method == 'POST':
        dv = luongthang.objects.get(pk=id)
        fmdv = luongthang_Form(request.POST, instance=dv)
        if fmdv.is_valid():
            fmdv.save()
    else:
        dv = luongthang.objects.get(pk=id)
        fmdv = luongthang_Form(instance=dv)
    return render(request,'mota_cv/dinhgia_up-2.html', {'form': fmdv})

# This functions will delete/xóa
def del_luong_tamung(request, id):
    dv = luongthang.objects.get(pk=id)
    if request.method == 'POST':
        dv.delete()
        return HttpResponseRedirect('/dinhgia/')
    return render(request, 'mota_cv/Dinhgia_delete.html')
        #return redirect('/')
#<<<<<<...kết thúc Chương trình Lương ttạm ứng nhân viên:




import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)
#------------cham công thang-----


def add_chamcong(request):
    # Nhanvien_dg_nangluc = request.GET.get('Nhanvien_dg_nangluc')
    Nhanvien_chamcong = Nhan_vien.objects.all()
    u =Chamcongchitiet.objects.all()
    if request.method == 'POST':
        data = request.POST
        Nhanvien_chamcongs = Nhan_vien.objects.filter()
        thangs = [1,2,3,4,5,6,7,8,10,11,12]
        nams = [2023, 2024]
        for Nhanvien_chamcong in Nhanvien_chamcongs:
            for thang in thangs:
                for namcc in nams:
                        khoa_hoc = Chamcongchitiet.objects.create(
                            Nam=namcc,
                            Nhan_vien=Nhanvien_chamcong,
                            thang=thang,
                            don_vi =Nhanvien_chamcong.don_vi,
                            bo_phan =Nhanvien_chamcong.bo_phan,
                            to_nhom =Nhanvien_chamcong.to_nhom,
                            )

                        continue

    if u.filter(Nam =" ",thang =" ", Ngay_1=" "):
            u.filter(Nam="2023").update(Ngay_1="X", Ngay_2="X", Ngay_3="X", Ngay_4="X", Ngay_5="X", Ngay_6="X", Ngay_7="X", Ngay_8="X", Ngay_9="X", Ngay_10="X",
                                        Ngay_11="X", Ngay_12="X", Ngay_13="X", Ngay_14="X", Ngay_15="X", Ngay_16="X", Ngay_17="X", Ngay_18="X", Ngay_19="X", Ngay_20="X",
                                        Ngay_21="X", Ngay_22="X", Ngay_23="X", Ngay_24="X", Ngay_25="X", Ngay_26="X", Ngay_27="X", Ngay_28="X", Ngay_29="X", Ngay_30="X", Ngay_31="X")

            u.filter(thang="1").update(Ngay_1='NL', Ngay_2="CN", Ngay_8="T7", Ngay_9="CN", Ngay_15="T7", Ngay_16="CN", Ngay_22="T7", Ngay_23="CN", Ngay_29="T7", Ngay_30="CN", Ngay_31="NT")
            u.filter(thang="2").update(Ngay_1="NT", Ngay_2="NT", Ngay_3="NT", Ngay_4="NT", Ngay_5="T7", Ngay_6="CN", Ngay_12="T7", Ngay_13="CN", Ngay_19="T7", Ngay_20="CN", Ngay_26="T7", Ngay_27="CN")
            u.filter(thang="3").update(Ngay_5="T7", Ngay_6="CN", Ngay_12="T7", Ngay_13="CN", Ngay_19="T7", Ngay_20="CN", Ngay_26="T7", Ngay_27="CN")
            u.filter(thang="4").update(Ngay_2="T7", Ngay_3="CN", Ngay_9="T7", Ngay_10="NL",Ngay_11="NL", Ngay_16="T7", Ngay_17="CN", Ngay_23="T7", Ngay_24="CN", Ngay_29="T7", Ngay_30='NL')
            u.filter(thang="5").update(Ngay_1="NL", Ngay_7="T7", Ngay_8="CN", Ngay_14="T7", Ngay_15="CN", Ngay_21="T7", Ngay_22="CN",Ngay_28="T7", Ngay_29="CN")
            u.filter(thang="6").update(Ngay_4="T7", Ngay_5="CN", Ngay_11="T7", Ngay_12="CN", Ngay_18="T7", Ngay_19="CN", Ngay_25="T7", Ngay_26="CN")
            u.filter(thang="7").update(Ngay_2="T7", Ngay_3="CN", Ngay_9="T7", Ngay_10="CN", Ngay_16="T7", Ngay_17="CN", Ngay_23="T7", Ngay_24="CN", Ngay_30="T7", Ngay_31="CN")
            u.filter(thang="8").update(Ngay_6="T7", Ngay_7="CN", Ngay_13="T7", Ngay_14="CN", Ngay_20="T7", Ngay_21="CN", Ngay_27="T7", Ngay_28="CN", )
            u.filter(thang="9").update(Ngay_3="T7", Ngay_4="NL", Ngay_10="T7", Ngay_11="CN", Ngay_17="T7", Ngay_18="CN", Ngay_24="T7", Ngay_25="CN")
            u.filter(thang="10").update(Ngay_1="T7", Ngay_2="CN", Ngay_8="T7", Ngay_9="CN", Ngay_15="T7", Ngay_16="CN", Ngay_22="T7", Ngay_23="CN", Ngay_29="T7", Ngay_30="CN")
            u.filter(thang="11").update(Ngay_5="T7", Ngay_6="CN", Ngay_12="T7", Ngay_13="CN", Ngay_19="T7", Ngay_20="CN", Ngay_26="T7", Ngay_27="CN")
            u.filter(thang="12").update(Ngay_3="T7", Ngay_4="NL", Ngay_10="T7", Ngay_11="CN", Ngay_17="T7", Ngay_18="CN", Ngay_24="T7", Ngay_25="CN")

            return redirect('chamcong_thang')
    context = {'Nhanvien_danhgias': Nhanvien_chamcong}

    return render(request, 'nangluc/Danhgia_nangluc_add.html')





def chamcong_thang(request):

    form = Chamcong_f(request.POST or None)
    queryset = Chamcongchitiet.objects.all() [1:100]
    Nhan_viencc= Chamcongchitiet.objects.filter()
    thang= Chamcongchitiet.objects.filter()
    Nam= Chamcongchitiet.objects.filter()

   # context = {'queryset': queryset,'form':form,'Nhan_vien':Nhan_vien,'thang':thang, 'Nam':Nam, 'don_vi': don_vi, 'bo-phan':bo_phan}
    context = {'queryset': queryset,'form':form,'Nhan_vien':Nhan_vien,'thang':thang, 'Nam':Nam}
    if request.method == 'POST':
        bo_phan=form['bo_phan'].value()
        queryset=Chamcongchitiet.objects.filter(thang=form['thang'].value(), Nam=form['Nam'].value())
        if (bo_phan !=  ''):
            queryset = Chamcongchitiet.objects.filter(bo_phan_id=form['bo_phan'].value()).filter(thang=form['thang'].value(), Nam=form['Nam'].value())
    context = {'queryset': queryset,'form':form,'Nhan_vien':Nhan_viencc,'thang':thang, 'Nam':Nam}
    if form['Xuất_Excel'].value() == True:
            responese = HttpResponse(content_type='application/ms-excel')
            responese['Content-Disposition'] = 'attachment; filename=Chamcong'+ \
                    str(datetime.datetime.now())+'.xls'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('nhanvien')
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            font_style.font.shadow = True
#----------------------------------
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
            right_column7 = 30
            ws.write_merge(top_row7, bottom_row7, left_column7, right_column7,  'CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM', TIEUDE)

            top_row9 = 1
            bottom_row9 = 1
            left_column9 = 5
            right_column9 = 30
            ws.write_merge(top_row9, bottom_row9, left_column9, right_column9, 'Độc lập-Tự do-Hạnh phúc', TIEUDE3)

            top_row6 = 1
            bottom_row6 = 1
            left_column6 = 0
            right_column6 = 2
            ws.write_merge(top_row6, bottom_row6, left_column6, right_column6,  'TỔNG CÔNG TY TM SÀI GÒN-TNHH MTV', TIEUDE3)

            top_row = 4
            bottom_row = 4
            left_column = 0
            right_column = 30
            ws.write_merge(top_row, bottom_row, left_column, right_column, 'BẢNG CHẤM CÔNG', TIEUDEM)

            #rows1 = queryset.values_list('thang')[1]
            #rows2 = queryset.values_list('Nam')[1]

   #  --------------------------------------------
            row_num = 9

            TABLE_HEADER = xlwt.easyxf(
                'font: bold 1, color blue, name Tahoma, height 220;'
                'align: vertical center, horizontal center, wrap on;'
                'borders: top double, bottom double, left double, right double;'
                'pattern: pattern solid, pattern_fore_colour yellow, pattern_back_colour dark_red_ega;'
                                       )
            for_left = xlwt.easyxf(
                "font: color blue, name calibri, height 250; borders: left thin, right thin, top thin, bottom thin; pattern: pattern solid, fore_color white;")

            TABLE_row=xlwt.easyxf(
                'font: bold 1, color white, name calibri, height 250;'
                'align: vertical center, horizontal center, wrap on;'
                'borders: left thin, right thin, top thin, bottom thin;'
                'pattern: pattern solid, pattern_fore_colour green;'
            )
              #----Định dạng chiều rộng cột
            ws.col(0).width = 1500
            ws.col(1).width = 6000
            ws.col(2).width = 5000
            ws.col(3).width = 1000
            ws.col(4).width = 1000
            ws.col(5).width = 1000
            ws.col(6).width = 1000
            ws.col(7).width = 1000
            ws.col(8).width = 1000
            ws.col(9).width = 1000
            ws.col(10).width = 1000
            ws.col(11).width = 1000
            ws.col(12).width = 1000
            ws.col(13).width = 1000
            ws.col(14).width = 1000
            ws.col(15).width = 1000
            ws.col(16).width = 1000
            ws.col(17).width = 1000
            ws.col(18).width = 1000
            ws.col(19).width = 1000
            ws.col(20).width = 1000
            ws.col(21).width = 1000
            ws.col(22).width = 1000
            ws.col(23).width = 1000
            ws.col(24).width = 1000
            ws.col(25).width = 1000
            ws.col(26).width = 1000
            ws.col(27).width = 1000
            ws.col(28).width = 1000
            ws.col(29).width = 1000
            ws.col(30).width = 1000
            ws.col(31).width = 1000
            ws.col(32).width = 1000
            ws.col(33).width = 1000
            ws.col(34).width = 3000

            columns =['Số TT','Họ tên', 'Đơn vị','1','2','3','4','5','6','7','8','9','10',
                      '11','12','13','14','15','16','17','18','19','20',
                      '21','22','23','24','25','26','27','28','29','30','31', 'Tổng ngày công','Ngày nghỉ'

                      ]
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            #----Định dạng chữ
            font_style= xlwt.XFStyle()
            font_style.font.italic = False

            rows= queryset.values_list('id', 'Nhan_vien__ho_lot_thuong_dung',
                    'Nhan_vien__don_vi__Ten_DV',
                    'Ngay_1','Ngay_2','Ngay_3','Ngay_4','Ngay_5','Ngay_6','Ngay_7','Ngay_8','Ngay_9','Ngay_10',
                    'Ngay_11','Ngay_12','Ngay_13','Ngay_14','Ngay_15','Ngay_16','Ngay_17','Ngay_18','Ngay_19','Ngay_20',
                   'Ngay_21','Ngay_22','Ngay_23','Ngay_24','Ngay_25','Ngay_26','Ngay_27','Ngay_28','Ngay_29','Ngay_30','Ngay_31',)

            for row in rows:
                row_num +=1
                for col_num in range(len(row)):
                    if (row[col_num]) =='NL' and (row[col_num]) =="T7" and (row[col_num]) =="CN":
                        ws.write(row_num,col_num, str(row[col_num]), TABLE_row )
                    else:
                        ws.write(row_num, col_num, (row[col_num]),for_left)

            for_foot_ng = xlwt.easyxf('font: color blue, name Tahoma, height 220;'
                                  'align: vertical center, horizontal center,')
            TABLE_HEADER2 = xlwt.easyxf(
            'font: bold 1, color blue, name Tahoma, height 160;'
            'align: vertical center, horizontal center;'
        )
            ws.write(row_num + 3, 2, 'Ngày .... tháng 12 năm 2022', for_foot_ng)
            ws.write(row_num + 4, 2, 'Người phê duyệt', TABLE_HEADER2)

            ws.write(row_num + 3, 15, 'Ngày .... tháng 12 năm 2022', for_foot_ng)
            ws.write(row_num + 4, 15, 'Người xem xét', TABLE_HEADER2)

            ws.write(row_num + 3, 30, 'Ngày ... tháng 12 năm 2022', for_foot_ng)
            ws.write(row_num + 4, 30, 'Người  lập', TABLE_HEADER2)

            wb.save(responese)
            return responese
    context = {'queryset': queryset,'form':form,'Nhan_vien':Nhan_viencc,'thang':thang, 'Nam':Nam,}
    return render(request,'luong/chamcong_thang.html', context)


#---update cham công------
def update_chamcong(request, id):

    if request.method == 'POST':
        dv = Chamcongchitiet.objects.get(pk=id)
        fmdv = Chamcong_f(request.POST, instance=dv)
        if fmdv.is_valid():
            fmdv.save()
    else:
        dv = Chamcongchitiet.objects.get(pk=id)
        fmdv = Chamcong_f(instance=dv)
    return render(request,'luong/chamcong_update.html', {'form': fmdv})

#------------ Chấm công tháng finish---

# chay lệnh : pip install xhtml2pdf
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView

from io import BytesIO


class Luonglistviews(ListView):
    models= hd_laodong
    #form_class = hd_laodong_list_f
    #context_object_name = 'people'
    template_name = 'luong/main.html'

def luong_render_pdf_view(request, *args, **kwargs):
    pk= kwargs.get('pk')
    template_path = 'luong/pdf2.html'
    Hd_laodong = get_object_or_404(hd_laodong, pk=pk)
    context = {'form_hd_nhanvien': Hd_laodong}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/word')
    #if download:
   # response['Content-Disposition'] = 'attachment; filename="report5.pdf"'
     #if display:
    response['Content-Disposition'] = 'filename="reportthu.doc"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def render_pdf_view(request):
    template_path = 'luong/pdf1.html'
    context = {'myvar': 'chạy thử tiếng việt'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if download:
    #response['Content-Disposition'] = 'attachment; filename="report5.pdf"'
     #if display:
    response['Content-Disposition'] = 'filename="report5.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response, encoding="utf-8")
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


