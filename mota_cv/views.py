from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
import datetime
import xlwt
from django.db.models import Sum, Avg, Max, Min, Count, Q
from docxtpl import DocxTemplate, InlineImage #r
from datetime import datetime
from .models import *
from django.views.decorators.csrf import csrf_exempt
now = datetime.now() # current date and time
import os
import json
from django.http import HttpResponse, JsonResponse


#>>>>>>>>>>>: Chương trình HIỂN THỊ List+ Xuât excel nhân viên:---
from nhansu.models import Bo_phan, Don_vi
from nhansu.models import To_nhom

#------------------

#-----------Bắt đầu quản lý hợp đồng lao động-----------------------------------------
def is_valid_queryparam(param):
    return param != '' and param is not None

def filter(request):
    qsvt = Mota_Cv7.objects.filter()
    qs_1 = qsvt[0:1]
    ho_lot_thuong_dung_or_chucvu_query = request.GET.get('ho_lot_thuong_dung_or_chucvu')
    category = request.GET.get('category')
    bo_phan = request.GET.get('bo_phan')
    chuc_danh = request.GET.get('chuc_danh')
    Xuất_Excel =request.GET.get('Xuất_Excel')
    if is_valid_queryparam(ho_lot_thuong_dung_or_chucvu_query):
        qsvt = qsvt.filter(Ten_Nhom_CV__icontains=ho_lot_thuong_dung_or_chucvu_query)
    if is_valid_queryparam(category) and category != 'Chọn ...':
        qsvt = qsvt.filter(don_vi__Ten_DV=category)
    if is_valid_queryparam(bo_phan) and bo_phan != 'Chọn ...':
        qsvt = qsvt.filter(bo_phan__ten_bp=bo_phan)
    elif is_valid_queryparam(chuc_danh) and chuc_danh != 'Chọn ...':
        qsvt = qsvt.filter(chuc_danh__Ten=chuc_danh)
    return qsvt

#------------DANH MỤC mô tả công việc 7 yêu tố -----------------
def dm_vitricv(request):
    qsvt = filter(request)
    qs_1 = qsvt[0:10]

    context = {'queryset_1': qsvt,'queryset':qs_1,
               'categories' : Don_vi.objects.all(),
               'bophan_s':  Bo_phan.objects.all(),
               'chuc_danh_s' :  Chuc_danh.objects.all(),
    }
    return render(request,'mota_cv/Vitri_congviec_list.html', context)
#------------add mô tả công việc 7 yêu tố -----------------

def add_motacv(request):
    if request.method == 'POST':
        fm = motacongviec_Form7yt(request.POST or None)
        if fm.is_valid():
            fm.save()
        fm = motacongviec_Form7yt()
    else:
        fm = motacongviec_Form7yt()

    context = {'form': fm, }
    return render(request,'mota_cv/dinhgia_add_mota_new.html', context)

#------------Định giá công việc 7 yêu tố -----------------
def dinhgia_list_7yto(request):
    form = list_dinhgia_cv(request.GET or None)
    queryset7 = filter(request)[0:10]
    total = Mota_Cv7.objects.filter(don_vi_id=2).aggregate(Sum('Yeu_to_2_Ky_nang_id'))
    context = {'queryset7': queryset7,'form':form,'total':total,
               'categories' : Don_vi.objects.all(),
               'bophan_s':  Bo_phan.objects.all(),
               'chuc_danh_s' :  Chuc_danh.objects.all(),
               }
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
    context = {'queryset7': queryset7,'form':form,'total':total,
                    'categories' : Don_vi.objects.all(),
                     'bophan_s':  Bo_phan.objects.all(),
                     'chuc_danh_s' :  Chuc_danh.objects.all(),
                   }
    return render(request,'mota_cv/dinhgia_list_7yto.html', context)


#------------UPDATE Định giá công việc 7 yêu tố -----------------
def update_dinhgia7(request, id):
    if request.method == 'POST':
        dv = Mota_Cv7.objects.get(pk=id)
        fmdv = dinhgiaUpdateForm7(request.POST, instance=dv)
        if fmdv.is_valid():
            fmdv.save()
    else:
        dv = Mota_Cv7.objects.get(pk=id)
        fmdv = dinhgiaUpdateForm7(instance=dv)
    return render(request,'mota_cv/dinhgia_UPDATE_new.html', {'form': fmdv})
 #-----------------

#------------UPDATE MỘ TẢ công việc 7 yêu tố -----------------
def update_mota_7(request, id):
    if request.method == 'POST':
        dv = Mota_Cv7.objects.get(pk=id)
        fmdv = motacongviec_Form7yt(request.POST, instance=dv)
        if fmdv.is_valid():
            fmdv.save()
    else:
        dv = Mota_Cv7.objects.get(pk=id)
        fmdv = motacongviec_Form7yt(instance=dv)
    return render(request,'mota_cv/dinhgia_add_mota_new.html', {'form': fmdv})

def dinhgia_list_7yto_cu(request):
    form = list_dinhgia_cv(request.POST or None)
    queryset7 = Mota_Cv7.objects.all()
    total = Mota_Cv7.objects.filter(don_vi_id=2).aggregate(Sum('Yeu_to_2_Ky_nang_id'))
    context = {'queryset7': queryset7,'form':form,'total':total}
    if request.method == 'POST':
        don_vi=form['don_vi'].value()
        bo_phan =form['bo_phan'].value()
        Ten_Nhom_CV=form['Ten_Nhom_CV'].value()
        queryset7 = Mota_Cv7.objects.filter(Ten_Nhom_CV__icontains=form['Ten_Nhom_CV'].value())

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
    context = {'queryset7': queryset7,'form':form,'total':total}
    return render(request,'mota_cv/dinhgia_list_7yto.html', context)


def view_dinhgia_mota(request, id):
    if request.method == 'POST':
        dv = Mota_Cv.objects.get(pk=id)
        fmdv = motacongviec_Form(request.POST, instance=dv)
        if fmdv.is_valid():
            fmdv.save()

    else:
        dv = Mota_Cv.objects.get(pk=id)
        fmdv = motacongviec_Form(instance=dv)
        return render(request,'mota_cv/mota_dinhgia_up.html', {'fmdv': fmdv})


def load_bophans(request):
    don_vi_id = request.GET.get('don_vi')
    bo_phans = Bo_phan.objects.filter(don_vi_id=don_vi_id).order_by('ten_bp')

    bo_phan_id = request.GET.get('bo_phan')
    to_nhoms = To_nhom.objects.filter(bo_phan_id=bo_phan_id).order_by('ten_to')
    return render(request, 'mota_cv/list_choise_bophan.html', {'bo_phans': bo_phans, 'to_nhoms':to_nhoms,})


def view_motacv_chitiet77(request, id):
    pnv7 = Mota_Cv7.objects.get(id=id)
    doc = DocxTemplate("word_template/M_motacongviec7.docx")
    queryset7 = {
        "Ten_Nhom_CV": pnv7.Ten_Nhom_CV,
        "Ten_vitri_full": pnv7.Ten_vitri_full,
        "bo_phan" : pnv7.bo_phan,
        "don_vi": pnv7.don_vi,
        "Captren": pnv7.Captren,
        "diadiem_lv": pnv7.don_vi.diachi,
        "Mucdich_cv": pnv7.Mucdich_cv,
        "Qhe_captren": pnv7.Qhe_captren,
        "Qhe_cungcap": pnv7.Qhe_cungcap,
         "Qhe_capduoi": pnv7.Qhe_capduoi,
        "Qhe_nn_xahoi": pnv7.Qhe_nn_xahoi,
        "Qhe_khachhang": pnv7.Qhe_khachhang,
         "Nh_vu_ket_qua": pnv7.Nh_vu_ket_qua,
        "Trach_nhiem": pnv7.Trach_nhiem,
        "Ptien_laodong": pnv7.Ptien_laodong,
        "Yeu_to_1_trinh_do": pnv7.Yeu_to_1_trinh_do.name,
        "Yeu_to_2_Ky_nang": pnv7.Yeu_to_2_Ky_nang.name,
        "Yeu_to_3_Trach_nhiem": pnv7.Yeu_to_3_Trach_nhiem.name,
        "Yeu_to_4_Anh_huong": pnv7.Yeu_to_4_Anh_huong.name,
        "Yeu_to_5_Sangtao": pnv7.Yeu_to_5_Sangtao.name,
        "Yeu_to_6_Giaotiep": pnv7.Yeu_to_6_Giaotiep.name,
        "Yeu_to_7_DK_lamviec": pnv7.Yeu_to_7_DK_lamviec.name,
        "ten_nghe_NNDH": pnv7.ten_nghe_NNDH.name,
        "Donvi_Captren": pnv7.Donvi_Captren,
        "Yeu_to_khac": pnv7.Yeu_to_khac.name,
        "Ycau_Ngoaingu_23": pnv7.Ycau_Ngoaingu_23.name,
        "Ycau_CNTT_24": pnv7.Ycau_CNTT_24.name,
    }
    doc.render(queryset7)
    doc.save('thu_word/'+ str(pnv7.id)+ '.MTCV_'+ str(pnv7.Ten_vitri_full)+'.docx')

    return render(request, 'mota_cv/t7.html', {'Fmtcv': pnv7, 'queryset2':queryset7})


def view_motacv_chitiet7(request, id):
    pnv7 = Mota_Cv7.objects.get(id=id)
    doc = DocxTemplate("word_template/M_motacongviec7.docx")
    queryset7 = {
        "Ten_Nhom_CV": pnv7.Ten_Nhom_CV,
        "Ten_vitri_full": pnv7.Ten_vitri_full,
        "bo_phan" : pnv7.bo_phan,
        "don_vi": pnv7.don_vi,
        "Captren": pnv7.Captren,
        "diadiem_lv": pnv7.don_vi.diachi,
        "Mucdich_cv": pnv7.Mucdich_cv,
        "Qhe_captren": pnv7.Qhe_captren,
        "Qhe_cungcap": pnv7.Qhe_cungcap,
         "Qhe_capduoi": pnv7.Qhe_capduoi,
        "Qhe_nn_xahoi": pnv7.Qhe_nn_xahoi,
        "Qhe_khachhang": pnv7.Qhe_khachhang,
         "Nh_vu_ket_qua": pnv7.Nh_vu_ket_qua,
        "Trach_nhiem": pnv7.Trach_nhiem,
        "Ptien_laodong": pnv7.Ptien_laodong,
        "Yeu_to_1_trinh_do": pnv7.Yeu_to_1_trinh_do.name,
        "Yeu_to_2_Ky_nang": pnv7.Yeu_to_2_Ky_nang.name,
        "Yeu_to_3_Trach_nhiem": pnv7.Yeu_to_3_Trach_nhiem.name,
        "Yeu_to_4_Anh_huong": pnv7.Yeu_to_4_Anh_huong.name,
        "Yeu_to_5_Sangtao": pnv7.Yeu_to_5_Sangtao.name,
        "Yeu_to_6_Giaotiep": pnv7.Yeu_to_6_Giaotiep.name,
        "Yeu_to_7_DK_lamviec": pnv7.Yeu_to_7_DK_lamviec.name,
        "ten_nghe_NNDH": pnv7.ten_nghe_NNDH.name,
        "Donvi_Captren": pnv7.Donvi_Captren,
        "Yeu_to_khac": pnv7.Yeu_to_khac.name,
        "Ycau_Ngoaingu_23": pnv7.Ycau_Ngoaingu_23.name,
        "Ycau_CNTT_24": pnv7.Ycau_CNTT_24.name,
    }
    doc.render(queryset7)
    doc.save('thu_word/'+ str(pnv7.id)+ '.MTCV_'+ str(pnv7.Ten_vitri_full)+'.docx')
    return HttpResponseRedirect('http://127.0.0.1:8000/dinhgia7/')
    return render(request, 'mota_cv/t7.html', {'Fmtcv': pnv7, 'queryset2':queryset7})


#------------------List dinh giá------------
def dinhgia_list(request):
    form = list_dinhgia_cv(request.POST or None)
    queryset = Mota_Cv.objects.all()
   # queryset = Mota_Cv.objects.filter(don_vi_id=10)
    total = Mota_Cv.objects.filter(don_vi_id=5).aggregate(Sum('ycau_k_nghiem_22_id'))
    context = {'queryset': queryset,'form':form,'total':total}
    if request.method == 'POST':
        don_vi=form['don_vi'].value()
        bo_phan =form['bo_phan'].value()
        Ten_Nhom_CV=form['Ten_Nhom_CV'].value()
        #queryset = Mota_Cv.objects.all()
        queryset = Mota_Cv.objects.filter(Ten_Nhom_CV__icontains=form['Ten_Nhom_CV'].value())
        #if (don_vi != ''):
            #queryset = Mota_Cv.objects.filter(don_vi_id=don_vi).filter(bo_phan_id=bo_phan)
         #   queryset = Mota_Cv.objects.filter(Q(don_vi_id=don_vi)|Q(bo_phan_id=bo_phan))

        if form['Xuất_Excel'].value() == True:
            responese = HttpResponse(content_type='application/ms-excel')
            responese['Content-Disposition'] = 'attachment; filename=Danh sách dinhgia'+ '.xls'
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
            ws.write(3,2,'ĐỊNH GIÁ GIA TRỊ CÔNG VIỆC',TIEUDE)
            row_num = 5
            for_left = xlwt.easyxf("font: bold 1, color blue; borders: top single, bottom double, left double, right double; align: horiz left")
            TABLE_HEADER = xlwt.easyxf(
                'font: bold 1, color blue, name Tahoma, height 220;'
                'align: vertical center, horizontal center, wrap on;'
                'borders: top double, bottom double, left double, right double;'
                'pattern: pattern solid, pattern_fore_colour yellow, pattern_back_colour dark_red_ega;'
                                       )
              #----Định dạng chiều rộng cột
            ws.col(0).width = 2000
            ws.col(1).width = 4000
            ws.col(2).width = 2000
            ws.col(3).width = 2000
            ws.col(4).width = 2200
            ws.col(5).width = 2000
            ws.col(6).width = 2000
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

            columns =['Số TT','Chức vụ','Đơn vị', 'Bộ phân', '1.1 M.ảh SXKD', '1.2 M.ảh N.sự', '2.1 Tr-độ CM', '2.2 K.nghiệm<', '2.3 M.Ng.ngữ', '2.4 M.CNTT',
                      '3.1 M.Kế hoạch', '3.2 M.Stạo', '3.3 M.Đlập', '3.4 M.Gtiếp', '3.5 M.Cgđộ', '4.1 M. đhại', '4.2 M. rro',
                      ('Nhóm lương'), 'điểm',
                      ]
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            #----Định dạng chữ
            font_style= xlwt.XFStyle()
            font_style.font.italic = False
            for_left = xlwt.easyxf("font: color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            rows= queryset.values_list('id', 'Ten_Nhom_CV', 'Don_vi.Ten_DV', 'bo_phan_ten_bp', 'muc_ah_cty_11', 'muc_ah_nv_12',
                                       'ycau_trinhdocm_21', 'ycau_k_nghiem_22','ycau_Ngoaingu_23', 'ycau_CNTT_24', 'ycau_kehoach_31',
                                       'ycau_sangtao_32','ycau_doclap_33','ycau_giaotiep_34','ycau_cuongdo_35',  'mt_laodong_41', 'muc_rui_ro_42',
                                       'ycau_kynang_khac', 'tong_diem')
            for row in rows:
                row_num +=1
                for col_num in range(len(row)):
                    ws.write(row_num,col_num, str(row[col_num]), for_left)
            wb.save(responese)
            return responese
    context = {'queryset': queryset,'form':form,'total':total}
    return render(request,'mota_cv/dinhgia_list1.html', context)

#-------update định giá----
def update_dinhgia(request, id):
    if request.method == 'POST':
        dv = Mota_Cv.objects.get(pk=id)
        fmdv = dinhgiaUpdateForm(request.POST, instance=dv)
        if fmdv.is_valid():
            fmdv.save()
    else:
        dv = Mota_Cv.objects.get(pk=id)
        fmdv = dinhgiaUpdateForm(instance=dv)
    return render(request,'mota_cv/dinhgia_up-2.html', {'form': fmdv})

# ------Del định giá-------
def del_dinhgia(request, id):
    dv = Mota_Cv7.objects.get(pk=id)
    if request.method == 'POST':
        dv.delete()
        return HttpResponseRedirect('/dinhgia7/')
    return render(request, 'mota_cv/Dinhgia_delete.html')
        #return redirect('/')

#----------Mô tả chi tiết....
def view_motacv_chitiet(request, id):
    pnv = Mota_Cv.objects.get(id=id)

    doc = DocxTemplate("word_template/M_motacongviec.docx")
    queryset2 = {
        "Ten_Nhom_CV": pnv.Ten_Nhom_CV,
        "bo_phan" : pnv.bo_phan,
        "don_vi": pnv.don_vi,
        "Captren": pnv.Captren,
        "diadiem_lv": pnv.diadiem_lv,
        "Mucdich_cv": pnv.Mucdich_cv,
        "Qhe_captren": pnv.Qhe_captren,
        "Qhe_cungcap": pnv.Qhe_cungcap,
        "Qhe_nn_xahoi": pnv.Qhe_nn_xahoi,
        "Qhe_khachhang": pnv.Qhe_khachhang,
         # "Nh_vu_ket_qua": pnv.Nh_vu_ket_qua,
        "Trach_nhiem": pnv.Trach_nhiem,
        "Ptien_laodong": pnv.Dieu_kienlaodong,
        "Dieu_kienlaodong": pnv.Ptien_laodong,
        "muc_ah_cty_11": pnv.muc_ah_cty_11.name,
        "muc_ah_nv_12": pnv.muc_ah_nv_12.name,
        "ycau_trinhdocm_21": pnv.ycau_trinhdocm_21.name,
        "ycau_k_nghiem_22": pnv.ycau_k_nghiem_22.name,
        "ycau_Ngoaingu_23": pnv.ycau_Ngoaingu_23.name,
        "ycau_CNTT_24": pnv.ycau_CNTT_24.name,
        "ycau_kehoach_31": pnv.ycau_kehoach_31.name,
        "ycau_sangtao_32": pnv.ycau_sangtao_32.name,
        "ycau_doclap_33": pnv.ycau_doclap_33.name,
        "ycau_giaotiep_34": pnv.ycau_giaotiep_34.name,
        "ycau_cuongdo_35": pnv.ycau_cuongdo_35.name,
        "mt_laodong_41": pnv.mt_laodong_41.name,
        "muc_rui_ro_42": pnv.muc_rui_ro_42.name,

                }
    doc.render(queryset2)
    doc.save('thu_word/MTCV_'+ str(pnv.Ten_Nhom_CV)+'.docx')

    return render(request, 'mota_cv/t2.html', {'Fmtcv': pnv, 'queryset2':queryset2})

#-----------update motả công việc
@login_required(login_url='/dangnhap/')
def update_mota(request, id):
    pnv = Mota_Cv.objects.get(pk=id)
    fmnv = motacongviec_Form(instance=pnv)
    if request.method == 'POST':
        fmnv = motacongviec_Form(request.POST,request.FILES, instance=pnv)
        data = request.POST
        print('data:', data)
        if fmnv.is_valid():
            fmnv.save()
       # return redirect('employees')
    else:
        pnv = Mota_Cv.objects.get(pk=id)
        fmnv = motacongviec_Form(instance=pnv)

    return render(request,'mota_cv/mota_dinhgia_up.html', {'fmnv': fmnv})

#-----------
def dm_vitri(request):
    form = Chucdanh_form(request.POST or None)
    truy_van = Mota_Cv7.objects.all()
    context = {'students': truy_van, 'form': form, }
    return render(request,"mota_cv/chuc_danh.html",context)


#--------------CHỨC DANH CÔNG VIỆC-------------------------------------------------------
def dm_chucdanh(request):
    Nhanvien_dg_nangluc = request.GET.get('Nhanvien_dg_nangluc')
    form = Chucdanh_form(request.POST or None)
    danhgia_nangluc_list = Chuc_danh.objects.all()
    context = {'students': danhgia_nangluc_list, 'form': form, }
    return render(request,"mota_cv/chuc_danh.html",context)

@csrf_exempt
def Insertchucdanh(request):
    Ten=request.POST.get("Ten")
    Chuc_trach=request.POST.get("TC_daotao")
    tu_danhgia_dapung=request.POST.get("tu_danhgia_dapung")
    try:
        student=Chuc_danh(Ten=Ten,Chuc_trach=Chuc_trach,tu_danhgia_dapung=tu_danhgia_dapung)
        student.save()
        stuent_data={"id":student.id,"start_date":student.start_date,"error":False,"errorMessage":"Thêm dữ liệu thành công"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Không thêm được"}
        return JsonResponse(stuent_data,safe=False)

@csrf_exempt
def update_chucdanh(request):
    data=request.POST.get("data")
    dict_data=json.loads(data)
    try:
        for dic_single in dict_data:
            student=Chuc_danh.objects.get(id=dic_single['id'])
            student.TC_daotao=dic_single['TC_daotao']
            student.TC_kthuc_kn=dic_single['TC_kthuc_kn']
            student.save()
        stuent_data={"error":False,"errorMessage":"Cập nhật Thành công"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Không cập nhật được"}
        return JsonResponse(stuent_data,safe=False)

@csrf_exempt
def delete_chucdanh(request):
    id=request.POST.get("id")
    try:
        student=Chuc_danh.objects.get(id=id)
        student.delete()
        stuent_data={"error":False,"errorMessage":"Xóa hoàn thành"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Xóa không được"}
        return JsonResponse(stuent_data,safe=False)

#--------------fINISH CHỨC DANH CÔNG VIỆC-------------------------------------------------------

