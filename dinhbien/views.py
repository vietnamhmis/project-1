from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.db.models import Count
from django.db.models.functions import Round

from .models import *
from .forms import *
import datetime
import xlwt

import tempfile
from django.db.models import Sum, Avg, Max, Min, Count, Q


#>>>>>>>>>>>: Chương trình định biên hành chính:---

#------: Hiển thị định biên hành chính:
def dinhbien_hc_list(request):
    form = list_dinhbien_hc(request.POST or None)
    queryset = Dinhbien_HC.objects.all() [1:10]
    context = {'queryset': queryset,'form':form,}

    if request.method == 'POST':
        don_vi=form['don_vi'].value()
        bo_phan =form['bo_phan'].value()
        #chuc_vu =form['chuc_vu'].value()
        #queryset = mota_cv.objects.all()
        if (don_vi != ''):
            queryset = Dinhbien_HC.objects.filter(don_vi_id=don_vi).filter(bo_phan_id=bo_phan)
           # queryset = Dinhbien_HC.objects.filter(Q(don_vi_id=don_vi)|Q(bo_phan_id=bo_phan))

#--- Xuất ecxel--------
        if form['Xuất_Excel'].value() == True:
            responese = HttpResponse(content_type='application/ms-excel')
            responese['Content-Disposition'] = 'attachment; filename=Định biên lao động Hành chính'+ \
                    str(datetime.datetime.now())+'.xls'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('nhanvien')
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            font_style.font.shadow = True
            ws.write(0,0,'   TỔNG CÔNG TY XI MĂNG VIỆT NAM')
            ws.write(0,7,'   CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM',font_style )
            ws.write(1,7,'           Độc lập-Tự do-Hạnh phúc')
            ws.write(1,0,'CÔNG TY CỔ PHẦN XI MĂNG HÀ TIÊN 1',font_style)

            TIEUDE = xlwt.easyxf(
                'font: color RED, bold 1, name Tahoma, height 320;'
                'align: vertical center, horizontal center, wrap on;'
                'pattern:pattern_back_colour dark_red_ega;'
                                       )
            ws.write(3,7,'BIỂU XÁC ĐỊNH NỘI DUNG CÔNG VIỆC CỦA CÁC CHỨC DANH  LÀM VIỆC THEO GIỜ HÀNH-CHÍNH',TIEUDE)
            row_num = 50
            for_left = xlwt.easyxf("font: bold 1, color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            TABLE_HEADER = xlwt.easyxf(
                'font: bold 1, color blue, name Tahoma, height 220;'
                'align: vertical center, horizontal center, wrap on;'
                'borders: top double, bottom double, left double, right double;'
                'pattern: pattern solid, pattern_fore_colour yellow, pattern_back_colour dark_red_ega;'
                                       )
              #----Định dạng chiều rộng cột
            ws.col(0).width = 1000
            ws.col(1).width = 1500
            ws.col(2).width = 2000
            ws.col(3).width = 1000
            ws.col(4).width = 2200
            ws.col(5).width = 2000
            ws.col(6).width = 2000
            ws.col(7).width = 20000
            ws.col(8).width = 2200
            ws.col(9).width = 2000
            ws.col(10).width = 4000

            columns =['Số TT','Đơn vị', 'Bộ phân', 'tổ', 'Chức vụ', 'ĐV tính', 'Tần xuất', 'Nội dung công việc', 'Khối lượng năm', 'số phút/lần','Tổng phút/năm',
                      ]
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            #----Định dạng chữ
            font_style= xlwt.XFStyle()
            font_style.font.italic = False
            for_left = xlwt.easyxf("font: color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            rows= queryset.values_list('id', 'don_vi', 'bo_phan', 'to_nhom', 'chuc_vu',
                                       'donvi_tinh', 'tan_xuat_lviec','Noi_dung_cviec', 'khoiluong_nam', 'sophut_th_1lan', 'Tong_phut_1nam',
                                 )
            for row in rows:
                row_num +=1
                for col_num in range(len(row)):
                    ws.write(row_num,col_num, str(row[col_num]), for_left)
            wb.save(responese)
            return responese
          #--- Finish Xuất ecxel--------
    context = {'queryset': queryset,'form':form,}
    return render(request,'dinhbien/dinhbien_hc_list1.html', context)
#------: Finish-Hiển thị định biên hành chính:


#------: Update định biên hành chính:
def update_dinhbienhc(request, id):
    if request.method == 'POST':
        dv = Dinhbien_HC.objects.get(pk=id)
        fmdv = list_dinhbien_hc(request.POST, instance=dv)
        if fmdv.is_valid():
            fmdv.save()
    else:
        dv = Dinhbien_HC.objects.get(pk=id)
        fmdv = list_dinhbien_hc(instance=dv)
    return render(request,'dinhbien/dinhbien_hc_uppdate.html', {'form': fmdv})

# This functions will delete/xóa
def del_dinhbienhc(request, id):
    dv = Dinhbien_HC.objects.get(pk=id)
    if request.method == 'POST':
        dv.delete()
        return HttpResponseRedirect('/dinhbienhc/')
    return render(request, 'dinhbien/Dinhbien_hc_del.html')
        #return redirect('/')
#------: Finish Update định biên hành chính:


#------: Add Định biên hành chính:
def add_dinhbiehc(request):
    if request.method == 'POST':
        fm = list_dinhbien_hc(request.POST or None)
        if fm.is_valid():
            fm.save()
        fm = list_dinhbien_hc()
    else:
        fm = list_dinhbien_hc()
    total_CViec = Dinhbien_HC.objects.count()

    context = {'form': fm, 'total_CViec':total_CViec,}
    return render(request, 'dinhbien/Dinhbien_hc_add.html', context)
#------: Finish Update định biên hành chính:




#------: Hiển thị định biên ca,kíp:
def dinhbien_ca_list(request):
    form = Form_dinhbien_ca(request.POST or None)
    queryset = Dinhbien_ca.objects.all()
    context = {'queryset': queryset,'form':form,}

    if request.method == 'POST':
        don_vi=form['don_vi'].value()
        bo_phan =form['bo_phan'].value()
        #chuc_vu =form['chuc_vu'].value()
        #queryset = mota_cv.objects.all()
        if (don_vi != ''):
            #queryset = mota_cv.objects.filter(don_vi_id=don_vi).filter(bo_phan_id=bo_phan)
            queryset = Dinhbien_ca.objects.filter(Q(don_vi_id=don_vi)|Q(bo_phan_id=bo_phan))
#--- Xuất ecxel--------
        if form['Xuất_Excel'].value() == True:
            responese = HttpResponse(content_type='application/ms-excel')
            responese['Content-Disposition'] = 'attachment; filename=Danh sách dinhgia'+ \
                    str(datetime.datetime.now())+'.xls'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('nhanvien')
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            font_style.font.shadow = True
            ws.write(0,0,'   TỔNG CÔNG TY XI MĂNG VIỆT NAM')
            ws.write(0,6,'   CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM',font_style )
            ws.write(1,6,'           Độc lập-Tự do-Hạnh phúc')
            ws.write(1,0,'CÔNG TY CỔ PHẦN XI MĂNG HÀ TIÊN 1',font_style)

            TIEUDE = xlwt.easyxf(
                'font: color RED, bold 1, name Tahoma, height 320;'
                'align: vertical center, horizontal center, wrap on;'
                'pattern:pattern_back_colour dark_red_ega;'
                                       )
            ws.write(3,6,'BIỂU XÁC ĐỊNH NỘI DUNG CÔNG VIỆC CỦA CÁC CHỨC DANH  LÀM VIỆC THEO CA',TIEUDE)
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
            ws.col(1).width = 1000
            ws.col(2).width = 1000
            ws.col(3).width = 1000
            ws.col(4).width = 1200
            ws.col(5).width = 2000
            ws.col(6).width = 15000
            ws.col(7).width = 2000
            ws.col(8).width = 2200
            ws.col(9).width = 2000
            ws.col(10).width = 2000
            ws.col(11).width = 2000
            ws.col(12).width = 2200
            ws.col(13).width = 2000
            ws.col(14).width = 6000


            columns =['Số TT','Đơn vị', 'Bộ phân', 'tổ', 'Chức vụ', 'ĐV tính', 'Nội dung công việc',
                   'LĐ ca 1', 'LĐ ca 2', 'LĐ ca 3', 'phút/đvị',
                   'Phút/ca_1', 'Phút/ca_2', 'Phút/ca_3', 'Tong_phut_1namc'
                      ]
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            #----Định dạng chữ
            font_style= xlwt.XFStyle()
            font_style.font.italic = False
            for_left = xlwt.easyxf("font: color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            rows= queryset.values_list('id', 'don_vi', 'bo_phan', 'to_nhom', 'chuc_vu',
                                       'donvi_tinh',
                                       'Noi_dung_cviecca', 'laodong_ca_1', 'laodong_ca_2', 'laodong_ca_3', 'sophut_th_1lanc',
                                       'Thoigian_yc_ca_1', 'Thoigian_yc_ca_2', 'Thoigian_yc_ca_3', 'Tong_phut_1namc',
                                 )
            for row in rows:
                row_num +=1
                for col_num in range(len(row)):
                    ws.write(row_num,col_num, str(row[col_num]), for_left)
            wb.save(responese)
            return responese
          #--- Finish Xuất ecxel--------
    context = {'queryset': queryset,'form':form,}
    return render(request,'dinhbien/dinhbien_ca_list.html', context)
#------: Finish-Hiển thị định biên ca:


#------: Update định biên ca, kíp:
def update_dinhbienca(request, id):
    if request.method == 'POST':
        dv = Dinhbien_ca.objects.get(pk=id)
        fmdv = Form_dinhbien_ca(request.POST, instance=dv)
        if fmdv.is_valid():
            fmdv.save()
    else:
        dv = Dinhbien_ca.objects.get(pk=id)
        fmdv = Form_dinhbien_ca(instance=dv)
    return render(request,'dinhbien/dinhbien_ca_uppdate.html', {'form': fmdv})












# This functions will delete/xóa
def del_dinhbienca(request, id):
    dv = Dinhbien_ca.objects.get(pk=id)
    if request.method == 'POST':
        dv.delete()
        return HttpResponseRedirect('/dinhbienca/')
    return render(request, 'dinhbien/Dinhbien_ca_del.html')
        #return redirect('/')
#------: Finish Update định biên hành chính:


#------: Add Định biên ca kíp:
def add_dinhbienca(request):
    if request.method == 'POST':
        fm = Form_dinhbien_ca(request.POST or None)
        if fm.is_valid():
            fm.save()
        fm = Form_dinhbien_ca()
    else:
        fm = Form_dinhbien_ca()
    total_CViec = Dinhbien_ca.objects.count()

    context = {'form': fm, 'total_CViec':total_CViec,}
    return render(request, 'dinhbien/Dinhbien_ca_add.html', context)
#------: Finish Update định biên ca:





def dinhbien_th(request):
    form = Form_dinhbien(request.POST or None)
    queryset = tonghopdinhbien.objects.all()[1:50]

    bophan=tonghopdinhbien.objects.all().aggregate(sobp=Count('bo_phan__id'))
    to_nhom=tonghopdinhbien.objects.filter().aggregate(soto=Count('to_nhom__id'))
    chuc_vu=tonghopdinhbien.objects.filter().aggregate(soto=Count('chuc_vu__id'))

    context = {'queryset': queryset,'form':form,'bophan':bophan,'vitri_chucvu':to_nhom,'nhanvien':chuc_vu}

    if request.method == 'POST':
        don_vi=form['don_vi'].value()
        bo_phan =form['bo_phan'].value()
        chucdanh_dinhbien=form['chucdanh_dinhbien'].value()


        queryset = tonghopdinhbien.objects.filter(chucdanh_dinhbien__icontains=form['chucdanh_dinhbien'].value())
        if(chucdanh_dinhbien == ''):
            # queryset = tonghopdinhbien.objects.filter(don_vi_id=don_vi).filter(bo_phan_id=bo_phan)
           queryset = tonghopdinhbien.objects.filter(Q(don_vi_id=don_vi)|Q(bo_phan_id=bo_phan))
           context = {'queryset': queryset,'form':form,'bophan':bophan,'vitri_chucvu':to_nhom,'nhanvien':chuc_vu}

#--- Xuất ecxel--------
        if form['Xuất_Excel'].value() == True:
            responese = HttpResponse(content_type='application/ms-excel')
            responese['Content-Disposition'] = 'attachment; filename=Danh sách dinhgia'+ \
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
            ws.write(3,2,'BIỂU ĐỊNH BIÊN LAO ĐỘNG ',TIEUDE)
            row_num = 5
            for_left = xlwt.easyxf("font: bold 1, color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            TABLE_HEADER = xlwt.easyxf(
                'font: bold 1, color blue, name Tahoma, height 120;'
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


            columns =['Số TT', 'Chức vụ/Tổ', 'Đơn vị/Bộ phân', 'Định biên hiện hữu', 'LĐ hành chính',
                   'LĐ ca', 'ĐB LĐ Hành chính', 'LĐ ca',
                   'LĐ.HC.ĐB', 'LĐ. ca ĐB','Tổng ', 'CL.ĐB mới', 'Tổng phút/năm'
                      ]

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            #----Định dạng chữ
            font_style= xlwt.XFStyle()
            font_style.font.italic = False
            for_left = xlwt.easyxf("font: color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            rows= queryset.values_list('id', 'chuc_vu','to_nhom', 'don_vi', 'bo_phan',
                                       'dinhbien_hienco', 'laodong_hc_hienco',
                                       'laodong_ca_hienco', 'laodong_hc_dinhbien', 'laodong_ca_dinhbien', 'tong_dinhbien', 'chenhlech_dbien',
                                       'Tong_phut_1nam',
                                 )

            for row in rows:
                row_num +=1
                for col_num in range(len(row)):
                    ws.write(row_num,col_num, str(row[col_num]), for_left)
            wb.save(responese)
            return responese
          #--- Finish Xuất ecxel--------
    context = {'queryset': queryset,'form':form,}
    return render(request,'dinhbien/dinhbien_list.html', context)
#------: Finish-Hiển thị định biên ca:


@login_required(login_url='/dangnhap/')
def donvi_dinhbien(request, id):
    form = Form_dinhbien(request.POST or None)
    queryset_nvien_donvi = tonghopdinhbien.objects.filter(don_vi_id=id)
    context = {'queryset': queryset_nvien_donvi,'form':form,}
    return render(request,'dinhbien/dinhbien_list_to.html', context)

@login_required(login_url='/dangnhap/')
def bophan_dinhbien(request, id):
    form = Form_dinhbien(request.POST or None)
    queryset_nvien_bophan = tonghopdinhbien.objects.filter(bo_phan_id=id)
    context = {'queryset': queryset_nvien_bophan,'form':form,}
    return render(request,'dinhbien/dinhbien_list_to.html', context)

@login_required(login_url='/dangnhap/')
def tonhom_dinhbien(request, id):
    form = Form_dinhbien(request.POST or None)
    queryset_nvien_to = tonghopdinhbien.objects.filter(to_nhom_id=id)
    context = {'queryset': queryset_nvien_to,'form':form,}
    return render(request,'dinhbien/dinhbien_list_to.html', context)

@login_required(login_url='/dangnhap/')
def dinhbien_ca_chi_tiet(request, id):
    form = Form_dinhbien(request.POST or None)

    dinhbien_ca_chi_tiet = Dinhbien_ca.objects.filter(chuc_vu_id=id)

    queryset = Dinhbien_ca.objects.filter(chuc_vu_id=id)
    sum_phutnam = Dinhbien_ca.objects.filter(chuc_vu_id=id).aggregate(tong=Sum('Tong_phut_1namc'))
    laodong = Dinhbien_ca.objects.filter(chuc_vu_id=id).aggregate(tong=Sum('dinhbienca'))


    context = {'queryset': queryset,'form':form, 'sum_phutnam':sum_phutnam, 'laodong':laodong}

    if form['Xuất_Excel'].value() == True:
            responese = HttpResponse(content_type='application/ms-excel')
            responese['Content-Disposition'] = 'attachment; filename=NDCV_ca'+ \
                    str(datetime.datetime.now())+'.xls'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('nhanvien')
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            font_style.font.shadow = True
            ws.write(0,0,'   TỔNG CÔNG TY XI MĂNG VIỆT NAM')
            ws.write(0,6,'   CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM',font_style )
            ws.write(1,6,'           Độc lập-Tự do-Hạnh phúc')
            ws.write(1,0,'CÔNG TY CỔ PHẦN XI MĂNG HÀ TIÊN 1',font_style)

            TIEUDE = xlwt.easyxf(
                'font: color RED, bold 1, name Tahoma, height 320;'
                'align: vertical center, horizontal center, wrap on;'
                'pattern:pattern_back_colour dark_red_ega;'
                                       )
            ws.write(3,6,'BIỂU XÁC ĐỊNH NỘI DUNG CÔNG VIỆC CỦA CÁC CHỨC DANH  LÀM VIỆC THEO CA',TIEUDE)
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
            ws.col(1).width = 1000
            ws.col(2).width = 1000
            ws.col(3).width = 1000
            ws.col(4).width = 1200
            ws.col(5).width = 2000
            ws.col(6).width = 15000
            ws.col(7).width = 2000
            ws.col(8).width = 2200
            ws.col(9).width = 2000
            ws.col(10).width = 2000
            ws.col(11).width = 2000
            ws.col(12).width = 2200
            ws.col(13).width = 2000
            ws.col(14).width = 6000


            columns =['Số TT','Đơn vị', 'Bộ phân', 'tổ', 'Chức vụ', 'ĐV tính', 'Nội dung công việc',
                   'LĐ ca 1', 'LĐ ca 2', 'LĐ ca 3', 'phút/đvị',
                   'Phút/ca_1', 'Phút/ca_2', 'Phút/ca_3', 'Tong_phut_1namc','địnhbiên'
                      ]
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            #----Định dạng chữ
            font_style= xlwt.XFStyle()
            font_style.font.italic = False
            for_left = xlwt.easyxf("font: color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            rows= queryset.values_list('id', 'don_vi', 'bo_phan', 'to_nhom', 'chuc_vu',
                                       'donvi_tinh',
                                       'Noi_dung_cviecca', 'laodong_ca_1', 'laodong_ca_2', 'laodong_ca_3', 'sophut_th_1lanc',
                                       'Thoigian_yc_ca_1', 'Thoigian_yc_ca_2', 'Thoigian_yc_ca_3', 'Tong_phut_1namc','dinhbienca',
                                 )
            for row in rows:
                row_num +=1
                for col_num in range(len(row)):
                    ws.write(row_num,col_num, str(row[col_num]), for_left)

            wb.save(responese)
            return responese
          #--- Finish Xuất ecxel--------
    context = {'queryset': queryset,'form':form, 'sum_phutnam':sum_phutnam,'laodong':laodong}



    return render(request,'dinhbien/dinhbien_ca_list_cv.html', context)




@login_required(login_url='/dangnhap/')
def dinhbien_hc_chi_tiet(request, id):
    form = Form_dinhbien(request.POST or None)

    queryset = Dinhbien_HC.objects.filter(chuc_vu_id=id)
    sum_phutnam = Dinhbien_HC.objects.filter(chuc_vu_id=id).aggregate(Phút_năm=Sum('Tong_phut_1nam'))

    laodong = Dinhbien_HC.objects.filter(chuc_vu_id=id).aggregate(Lao_động=Sum('dinhbienhc'))

    context = {'queryset': queryset,'form':form, 'sum_phutnam':sum_phutnam, 'laodong':laodong}

    if form['Xuất_Excel'].value() == True:
            responese = HttpResponse(content_type='application/ms-excel')
            responese['Content-Disposition'] = 'attachment; filename=NDCV_hanhchinh'+ \
                    str(datetime.datetime.now())+'.xls'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('nhanvien')
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            font_style.font.shadow = True
            ws.write(0,0,'   TỔNG CÔNG TY XI MĂNG VIỆT NAM')
            ws.write(0,7,'   CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM',font_style )
            ws.write(1,7,'           Độc lập-Tự do-Hạnh phúc')
            ws.write(1,0,'CÔNG TY CỔ PHẦN XI MĂNG HÀ TIÊN 1',font_style)

            TIEUDE = xlwt.easyxf(
                'font: color RED, bold 1, name Calibri, height 220;'
                'align: vertical center, horizontal center, wrap on;'
                'pattern:pattern_back_colour dark_red_ega;'
                                       )
            ws.write(3,5,'BIỂU XÁC ĐỊNH NỘI DUNG CÔNG VIỆC CỦA CÁC CHỨC DANH  LÀM VIỆC THEO GIỜ HÀNH---CHÍNH',TIEUDE)
            row_num = 5
            for_left = xlwt.easyxf("font: bold 1, color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            TABLE_HEADER = xlwt.easyxf(
                'font: bold 1, color blue, name Calibri, height 180;'
                'align: vertical center, horizontal center, wrap on;'
                'borders: top double, bottom double, left double, right double;'
                'pattern: pattern solid, pattern_fore_colour yellow, pattern_back_colour dark_red_ega;'
                                       )
              #----Định dạng chiều rộng cột
            ws.col(0).width = 1000
            ws.col(1).width = 1500
            ws.col(2).width = 2000
            ws.col(3).width = 1000
            ws.col(4).width = 2200
            ws.col(5).width = 22000
            ws.col(6).width = 2000
            ws.col(7).width = 2000
            ws.col(8).width = 2200
            ws.col(9).width = 2000
            ws.col(10).width = 4000

            columns =['Số TT','Đơn vị', 'Bộ phân', 'tổ', 'Chức vụ',  'Nội dung công việc', 'ĐV tính', 'Tần xuất','Khối lượng năm', 'số phút/lần','Tổng phút/năm',
                      ]
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            #----Định dạng chữ
            font_style= xlwt.XFStyle()
            font_style.font.italic = True
            for_left = xlwt.easyxf("font: color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            rows= queryset.values_list('id', 'don_vi', 'bo_phan', 'to_nhom', 'chuc_vu','Noi_dung_cviec',
                                       'donvi_tinh', 'tan_xuat_lviec', 'khoiluong_nam', 'sophut_th_1lan', 'Tong_phut_1nam',
                                 )
            for row in rows:
                row_num +=1
                for col_num in range(len(row)):
                    ws.write(row_num,col_num, str(row[col_num]), for_left)
            wb.save(responese)
            return responese
          #--- Finish Xuất ecxel--------
    context = {'queryset': queryset,'form':form, 'sum_phutnam':sum_phutnam,'laodong':laodong}
    return render(request,'dinhbien/dinhbien_hc_list_cv.html', context)
#------: Finish-Hiển thị định biên hành chính: