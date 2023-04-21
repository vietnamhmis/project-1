


from django.test import TestCase

#lúc 7h00, ngày 13/2 ket thúc
# http://127.0.0.1:8000/dgnlnv/
# ]]]




    def g_Diem_dat(self):
        Diem_dat_p = self.TenNangluc_congviec.Muc_quantrong_nluc * self.Ketqua_danhgia
        return Diem_dat_p


   # def save(self, *args, **kwarg):
     #   self.Diem_dat = self.g_Diem_dat
       # super(Danhgia_nluc, self).save(*args, **kwarg)



   # def save(self, *args, **kwargs):
      #  if self.Diem_dat > 0:
          # self.Diem_dat = self.Ketqua_danhgia * self.TenNangluc_congviec. Muc_quantrong_nluc
       # else:
            #self.Diem_dat = 0
        #super().save(*args, **kwargs)







  def g_Diem_dat(self):
        Diem_dat_p = self.TenNangluc_congviec.Muc_quantrong_nluc * self.Ketqua_danhgia
        return Diem_dat_p


    def save(self, *args, **kwarg):
        self.Diem_dat = self.g_Diem_dat
        super(Danhgia_nluc, self).save(*args, **kwarg)


from .models import Danhgia_nluc, Danhgia_nluc_thu, StudentData

#
    Nhan_viens = Danhgia_nluc.objects.all()
    for Nhanvien in Nhan_viens:
        khoa_hoc = Danhgia_nluc.objects.update_or_create(
            Diem_dat = 12
            )

def HomePage(request):
    Nhanvien_dg_nangluc = request.GET.get('Nhanvien_dg_nangluc')
    form = Danhgia_nangluc_form(request.POST or None)
    danhgia_nangluc_list = StudentData.objects.all()[1:10]
    context = {'students': danhgia_nangluc_list, 'form': form, }
    if request.method == 'POST':
        Landanhgia_nagluc = form['Landanhgia_nagluc'].value()
        Nhanvien_dg_nangluc = form['Nhanvien_dg_nangluc'].value()
        TenNangluc_congviec = form['TenNangluc_congviec'].value()
        if (Landanhgia_nagluc != ''):
            danhgia_nangluc_list = StudentData.objects.filter(
                Landanhgia_nagluc__icontains=form['Landanhgia_nagluc'].value(),
            )
        if (Nhanvien_dg_nangluc != ''):
            # queryset = queryset.filter(chucdanh_CV_id=chucdanh_CV,nangluc_cv_id = nangluc_cv)
            danhgia_nangluc_list = StudentData.objects.filter(Nhanvien_dg_nangluc_id=Nhanvien_dg_nangluc)

    chucdanh_CV2 = Nhan_vien.objects.filter(don_vi_id=7)
    context = {'Nhanvien_duoc_dg_nangluc': chucdanh_CV2, "productss": danhgia_nangluc_list, 'students': danhgia_nangluc_list, 'form': form}

    Diem_kq = Danhgia_nluc.objects.aggregate(Count('Ketqua_danhgia'))

    from django.db.models import Sum
    total_tu_dg = (danhgia_nangluc_list.aggregate(total=Sum('tu_danhgia_dapung', field="tu_danhgia_dapung*3"))['total'])
    total_ql = (danhgia_nangluc_list.aggregate(total=Sum('Quanly_danhgia', field="Quanly_danhgia*1"))['total'])
    total_chung = (danhgia_nangluc_list.aggregate(total=Sum('Ketqua_danhgia', field="Ketqua_danhgia*1"))['total'])


    total_mucqt = (danhgia_nangluc_list.aggregate(total=Sum('TenNangluc_congviec__Muc_quantrong_nluc',
                                                  field="TenNangluc_congviec__Muc_quantrong_nluc"))['total'])

    total_tt = (danhgia_nangluc_list.aggregate(total=Sum('TenNangluc_congviec__Muc_thanhthao_nluc',
                                                  field="TenNangluc_congviec.Muc_thanhthao_nluc"))['total'])

    total_diemchuan = (danhgia_nangluc_list.aggregate(total=Sum('Diem_tieuchuan',
                                                   field="Diem_tieuchuan"))['total'])

    total_diemcdat = (danhgia_nangluc_list.aggregate(total=Sum('Diem_dat',
                                                   field="Diem_dat*10"))['total'])

    total_diem_danhgia = (danhgia_nangluc_list.aggregate(total=Sum('Diem_dat',
                                                   field="Diem_dat*10"))['total'])

    #ketqua_nangluc = (total_diemcdat/total_diemchuan )
    ketqua_nangluc = 1

    if form['Xuất_Excel'].value() == True:
        responese = HttpResponse(content_type='application/ms-excel')
        responese['Content-Disposition'] = 'attachment; filename=Danh_gia_NL_'+'.xls'
        #responese['Content-Disposition'] = 'attachment; filename=' + Nhanvien_dg_nangluc + '_KhungNL.xls'
        #responese['Content-Disposition'] = 'attachment; filename='+ Nhanvien_dg_nangluc + '.xls'
       # responese['Content-Disposition'] = 'attachment; filename=str(Nhanvien_dg_nangluc)'+'d.xls'
#===============================================================================================================
        wb = xlwt.Workbook(encoding='utf-8')
        #ws = wb.add_sheet(str(Nhanvien_dg_nangluc))
        ws = wb.add_sheet('ĐG')
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
        ws.write_merge(top_row, bottom_row, left_column, right_column, 'BIỂU ĐÁNH GIÁ NĂNG LỰC NHÂN SỰ', TIEUDEM)

        rows1 = danhgia_nangluc_list.values_list('Nhanvien_dg_nangluc__ho_lot_thuong_dung')[1]
        rows2 = danhgia_nangluc_list.values_list('Nhanvien_dg_nangluc__vitri_CV__Ten_Nhom_CV')[1]
        rows3 = danhgia_nangluc_list.values_list('Nhanvien_dg_nangluc__bo_phan__ten_bp')[1]
        row_phay = (", ",)

        ws.write(6, 2, "Họ tên:", TIEUDE1)
        ws.write(6, 3, rows1 +row_phay+ rows2, TIEUDE2)
        ws.write(7, 2, "Đơn vị:", TIEUDE1)
        ws.write(7, 3, rows3, TIEUDE2)

        row_num = 9

        TABLE_HEADER = xlwt.easyxf(
            'font: bold 1, color blue, name Tahoma, height 220;'
            'align: vertical center, horizontal center, wrap on;'
            'borders: top double, bottom double, left double, right double;'
            'pattern: pattern solid, pattern_fore_colour light_yellow, pattern_back_colour dark_red_ega;'
        )
        for_left = xlwt.easyxf(
                "font: color blue, name calibri, height 250; borders: left thin, right thin, top thin, bottom thin; pattern: pattern solid, fore_color white;")

        TABLE_row=xlwt.easyxf(
                'font: bold 1, color white, name calibri, height 250;'
                'align: vertical center, horizontal center, wrap on;'
                'borders: left thin, right thin, top thin, bottom thin;'
                'pattern: pattern solid, pattern_fore_colour green;'
            )

        ws.col(0).width = 1200
        ws.col(1).width = 2000
        ws.col(2).width = 8500
        ws.col(3).width = 1800
        ws.col(4).width = 2000
        ws.col(5).width = 1900
        ws.col(6).width = 1900
        ws.col(7).width = 2000
        ws.col(8).width = 2000
        ws.col(9).width = 1800
        # ------------------
        columns = ['Số TT', 'Mã NL', 'Tên năng lực', 'Mức độ quan trọng', 'Mức độ Thành thạo', 'Điểm tiêu chuẩn',' Tự đánh giá',
                   'Cấp trên đánh giá', 'Kết quả thống nhất','Điểm ĐG',  'Kết quả']
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
        # ----Định dạng chữ
        font_style = xlwt.XFStyle()
        font_style.font.italic = False


        rows = danhgia_nangluc_list.values_list('TenNangluc_congviec__stt', 'TenNangluc_congviec__nangluc_cv__ma_nangluc',
                                                'TenNangluc_congviec__nangluc_cv__name',
                                                'TenNangluc_congviec__Muc_quantrong_nluc',
                                                'TenNangluc_congviec__Muc_thanhthao_nluc',


                                                'TenNangluc_congviec__Diem_tieuchuan',
                                                'tu_danhgia_dapung', 'Quanly_danhgia', 'Ketqua_danhgia',
                                                'Diem_dat', 'Kha_nang_dapung')


        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                if (row[col_num]) != 0 and (row[col_num]) != 'I.NĂNG LỰC CHUNG' and (row[col_num]) != "II.NĂNG LỰC QUẢN LÝ" and (row[col_num]) != "III.NĂNG LỰC CHUYÊN MÔN"\
                            and (row[col_num]) != 'CH00' and (row[col_num]) != "QL00" and (row[col_num]) != "CM00":
                        ws.write(row_num, col_num, (row[col_num]),for_left)
                else:
                        ws.write(row_num, col_num, (row[col_num]),TABLE_row)


        print('Số cột', col_num)
        print('Số hàng', row_num)
        for_foot = xlwt.easyxf("font: color blue;  pattern: pattern solid, fore_color white;")
        for_foot_ng = xlwt.easyxf('font: color blue, name Tahoma, height 220;'
                                  'align: vertical center, horizontal center,')
        TABLE_HEADER2 = xlwt.easyxf(
            'font: bold 1, color blue, name Tahoma, height 160;'
            'align: vertical center, horizontal center;'
        )
        tam1=""

        top_row2 = row_num + 1
        bottom_row2 = row_num + 1
        left_column2 = 0
        right_column2 = 2
        ws.write_merge(top_row2, bottom_row2, left_column2, right_column2,  'TỔNG ĐIỂM', TABLE_HEADER)

        ws.write(row_num + 1, 3, total_mucqt, TABLE_HEADER)
        ws.write(row_num + 1, 4, total_tt, TABLE_HEADER)
        ws.write(row_num + 1, 5, total_diemchuan, TABLE_HEADER)

        ws.write(row_num + 1, 6, total_tt, TABLE_HEADER)
        ws.write(row_num + 1, 7, tam1, TABLE_HEADER)
        ws.write(row_num + 1, 8, tam1, TABLE_HEADER)
        ws.write(row_num + 1, 9, total_diemchuan, TABLE_HEADER)
        ws.write(row_num + 1, 10, ketqua_nangluc, TABLE_HEADER)

        ws.write(row_num + 3, 1, 'Ngày .... tháng 12 năm 2022', for_foot_ng)
        ws.write(row_num + 4, 1, 'Người phê duyệt', TABLE_HEADER2)
        ws.write(row_num + 3, 3, 'Ngày .... tháng 12 năm 2022', for_foot_ng)
        ws.write(row_num + 4, 3, 'Người đánh giá', TABLE_HEADER2)
        ws.write(row_num + 3, 7, 'Ngày ... tháng 12 năm 2022', for_foot_ng)
        # ws.write_merge(row_num + 18,row_num + 19, row_num + 20,row_num + 21,  'Người được đánh giá', TABLE_HEADER2)
        ws.write(row_num + 4, 7, 'Người được đánh giá', TABLE_HEADER2)
        wb.save(responese)
        return responese


    if form['Xuất_Word'].value() == True:

        doc = DocxTemplate("word_template/M_danhgiangluc.docx")
        queryset5 = {
                  "Ho_ten":danhgia_nangluc_list.values_list('Nhanvien_dg_nangluc__ho_lot_thuong_dung')[1] ,
                  "Chuc_danh":(danhgia_nangluc_list.values_list('Nhanvien_dg_nangluc__vitri_CV__Ten_Nhom_CV'))[1] ,

                  "Don_vi":danhgia_nangluc_list.values_list('Nhanvien_dg_nangluc__bo_phan__ten_bp')[1] ,
                  'total_diemchuan': total_diemchuan,
                  'total_diemcdat': total_diemcdat,
                  'tiledat' :98,

                   "productss": danhgia_nangluc_list,

                    }
        doc.render(queryset5)
        doc.save('thu_word/NL_'+ Nhanvien_dg_nangluc + '.docx')

    context = {'Nhanvien_duoc_dg_nangluc': chucdanh_CV2, 'danhgia_nangluc_list1': danhgia_nangluc_list,
               "productss": danhgia_nangluc_list, 'students': danhgia_nangluc_list, 'form': form,
               'total_mucqt': total_mucqt, 'total_tt': total_tt,
               'total_diemchuan': total_diemchuan,
               'total_diemcdat': total_diemcdat,
               'form': form, 'total_tu_dg': total_tu_dg,
               'total_ql': total_ql,
               'total_chung':total_chung,


               'ketqua_nangluc': ketqua_nangluc,}
    return render(request,"nangluc/Danhgia_nangluc_aaa.html",context)

@csrf_exempt
def InsertStudent(request):
    TenNangluc_congviec=request.POST.get("TenNangluc_congviec")
    Quanly_danhgia=request.POST.get("Quanly_danhgia")
    tu_danhgia_dapung=request.POST.get("tu_danhgia_dapung")
    try:
        student=StudentData(TenNangluc_congviec=TenNangluc_congviec,Quanly_danhgia=Quanly_danhgia,tu_danhgia_dapung=tu_danhgia_dapung)
        student.save()
        stuent_data={"id":student.id,"start_date":student.start_date,"error":False,"errorMessage":"Thêm dữ liệu thành công"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Không thêm được"}
        return JsonResponse(stuent_data,safe=False)


@csrf_exempt
def update_all(request):
    data=request.POST.get("data")
    dict_data=json.loads(data)
    try:
        for dic_single in dict_data:
            student=StudentData.objects.get(id=dic_single['id'])
            #student.TenNangluc_congviec=dic_single['TenNangluc_congviec']
            student.Quanly_danhgia=dic_single['Quanly_danhgia']
            student.tu_danhgia_dapung=dic_single['tu_danhgia_dapung']
            student.save()
        stuent_data={"error":False,"errorMessage":"Cập nhật Thành công"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Không cập nhật được"}
        return JsonResponse(stuent_data,safe=False)

@csrf_exempt
def delete_data(request):
    id=request.POST.get("id")
    try:
        student=StudentData.objects.get(id=id)
        student.delete()
        stuent_data={"error":False,"errorMessage":"Xóa hoàn thành"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Xỏa không được"}
        return JsonResponse(stuent_data,safe=False)
#lúc 7h00, ngày 13/2 ket thúc




#---------------thay thế13h400, 13/2
#def HomePage(request):
    #students=StudentData.objects.all()
  #  return render(request,"CRUDAPP/hhh.html",{"students":students})



def HomePage(request):
    Nhanvien_dg_nangluc = request.GET.get('Nhanvien_dg_nangluc')
    form = Danhgia_nangluc_form(request.POST or None)
    danhgia_nangluc_list = StudentData.objects.all()[1:10]
    context = {'students': danhgia_nangluc_list, 'form': form, }
    if request.method == 'POST':
        Landanhgia_nagluc = form['Landanhgia_nagluc'].value()
        Nhanvien_dg_nangluc = form['Nhanvien_dg_nangluc'].value()
        TenNangluc_congviec = form['TenNangluc_congviec'].value()
        if (Landanhgia_nagluc != ''):
            danhgia_nangluc_list = StudentData.objects.filter(
                Landanhgia_nagluc__icontains=form['Landanhgia_nagluc'].value(),
            )
        if (Nhanvien_dg_nangluc != ''):
            # queryset = queryset.filter(chucdanh_CV_id=chucdanh_CV,nangluc_cv_id = nangluc_cv)
            danhgia_nangluc_list = StudentData.objects.filter(Nhanvien_dg_nangluc_id=Nhanvien_dg_nangluc)

    chucdanh_CV2 = Nhan_vien.objects.filter(don_vi_id=7)
    context = {'Nhanvien_duoc_dg_nangluc': chucdanh_CV2, "productss": danhgia_nangluc_list, 'students': danhgia_nangluc_list, 'form': form}
    return render(request,"CRUDAPP/aaa.html",context)

@csrf_exempt
def InsertStudent(request):
    Quanly_danhgia=request.POST.get("Quanly_danhgia")
    TenNangluc_congviec=request.POST.get("TenNangluc_congviec")
    tu_danhgia_dapung=request.POST.get("tu_danhgia_dapung")
    try:
        student=StudentData(Quanly_danhgia=Quanly_danhgia,TenNangluc_congviec=TenNangluc_congviec,tu_danhgia_dapung=tu_danhgia_dapung)
        student.save()
        stuent_data={"id":student.id,"start_date":student.start_date,"error":False,"errorMessage":"Thêm dữ liệu thành công"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Không thêm được"}
        return JsonResponse(stuent_data,safe=False)


@csrf_exempt
def update_all(request):
    data=request.POST.get("data")
    dict_data=json.loads(data)
    try:
        for dic_single in dict_data:
            student=StudentData.objects.get(id=dic_single['id'])
            student.Quanly_danhgia=dic_single['Quanly_danhgia']
            #student.TenNangluc_congviec=dic_single['TenNangluc_congviec']
            student.tu_danhgia_dapung=dic_single['tu_danhgia_dapung']
            student.save()
        stuent_data={"error":False,"errorMessage":"Cập nhật Thành công"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Không cập nhật được"}
        return JsonResponse(stuent_data,safe=False)

@csrf_exempt
def delete_data(request):
    id=request.POST.get("id")
    try:
        student=StudentData.objects.get(id=id)
        student.delete()
        stuent_data={"error":False,"errorMessage":"Xóa hoàn thành"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Xỏa không được"}
        return JsonResponse(stuent_data,safe=False)

#-------------https://www.youtube.com/watch?v=Qc5NnpxFbBo&t=4s-------------------------------------------------------------
import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .models import Danhgia_nluc, Danhgia_nluc_thu, StudentData


#def HomePage(request):
    #students=StudentData.objects.all()
  #  return render(request,"CRUDAPP/hhh.html",{"students":students})


def HomePage(request):
    students=StudentData.objects.all()
    return render(request,"CRUDAPP/aaa.html",{"students":students})

@csrf_exempt
def InsertStudent(request):
    Quanly_danhgia=request.POST.get("Quanly_danhgia")
    TenNangluc_congviec=request.POST.get("TenNangluc_congviec")
    tu_danhgia_dapung=request.POST.get("tu_danhgia_dapung")

    try:
        student=StudentData(Quanly_danhgia=Quanly_danhgia,TenNangluc_congviec=TenNangluc_congviec,tu_danhgia_dapung=tu_danhgia_dapung)
        student.save()
        stuent_data={"id":student.id,"start_date":student.start_date,"error":False,"errorMessage":"Thêm dữ liệu thành công"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Không thêm được"}
        return JsonResponse(stuent_data,safe=False)


@csrf_exempt
def update_all(request):
    data=request.POST.get("data")
    dict_data=json.loads(data)
    try:
        for dic_single in dict_data:
            student=StudentData.objects.get(id=dic_single['id'])
            student.Quanly_danhgia=dic_single['Quanly_danhgia']
            #student.TenNangluc_congviec=dic_single['TenNangluc_congviec']
            student.tu_danhgia_dapung=dic_single['tu_danhgia_dapung']
            student.save()
        stuent_data={"error":False,"errorMessage":"Cập nhật Thành công"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Không cập nhật được"}
        return JsonResponse(stuent_data,safe=False)

@csrf_exempt
def delete_data(request):
    id=request.POST.get("id")
    try:
        student=StudentData.objects.get(id=id)
        student.delete()
        stuent_data={"error":False,"errorMessage":"Xóa hoàn thành"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Xỏa không được"}
        return JsonResponse(stuent_data,safe=False)

#---------------

import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .models import Danhgia_nluc, Danhgia_nluc_thu


#def HomePage(request):
    #students=StudentData.objects.all()
  #  return render(request,"CRUDAPP/hhh.html",{"students":students})

def HomePage(request):
    students=Danhgia_nluc_thu.objects.all()[1:10]
    return render(request,"CRUDAPP/hhh.html",{"students":students})


@csrf_exempt
def InsertStudent(request):
    Landanhgia_nagluc=request.POST.get("Landanhgia_nagluc")
    TenNangluc_congviec=request.POST.get("TenNangluc_congviec")
    tu_danhgia_dapung=request.POST.get("tu_danhgia_dapung")

    try:
        student=Danhgia_nluc_thu(Landanhgia_nagluc=Landanhgia_nagluc,TenNangluc_congviec=TenNangluc_congviec,tu_danhgia_dapung=tu_danhgia_dapung)
        student.save()
        stuent_data={"id":student.id,"created_at":student.created_at,"error":False,"errorMessage":"Thêm dữ liệu thành công"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Không thêm được"}
        return JsonResponse(stuent_data,safe=False)

@csrf_exempt
def update_all(request):
    data=request.POST.get("data")
    dict_data=json.loads(data)
    try:
        for dic_single in dict_data:
            student=Danhgia_nluc.objects.get(id=dic_single['id'])
            student.name=dic_single['name']
            student.email=dic_single['email']
            student.gender=dic_single['gender']
            student.save()
        stuent_data={"error":False,"errorMessage":"Cập nhật Thành công"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Không cập nhật được"}
        return JsonResponse(stuent_data,safe=False)

@csrf_exempt
def delete_data(request):
    id=request.POST.get("id")
    try:
        student=Danhgia_nluc_thu.objects.get(id=id)
        student.delete()
        stuent_data={"error":False,"errorMessage":"Xóa hoàn thành"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Xỏa không được"}
        return JsonResponse(stuent_data,safe=False)

# Create your tests here.

  # Năng lực: chung=1; quản lý =3; chuyên môn =2
       # Nang_luc_2s = Nang_luc_2.objects.filter(Q(loai_nang_luc_id=2)|Q(loai_nang_luc_id=0))
        #lấy năng lực Lãnh đạo là loại lao động
        # Mota_Cv7s = Mota_Cv7.objects.all()

       # Mota_Cv7s= Mota_Cv7.objects.filter (Q(Loai_laodong_id=3)|Q(Loai_laodong_id=4)|Q(Loai_laodong_id=5)|Q(Loai_laodong_id=6)|Q(Loai_laodong_id=7))
        # 1.Công nhân; 2.NV; 3.QLCTy; 4. GĐ, PGĐ; 5.QĐ; Trửởng TT;  6. Trưởng ca; 7,8.Tồ trưởng; 9Thư ký



class Congviec_nangluc(models.Model):
    name            = models.CharField(max_length=70, null=False, blank=False)
    chucdanh_CV           = models.ForeignKey(Mota_Cv7, null=True, on_delete=models.SET_NULL)
    nangluc_cv            = models.ForeignKey(Nang_luc_2, null=True, on_delete=models.SET_NULL)
    Muc_quantrong_nluc    = models.IntegerField(default=2)
    Muc_thanhthao_nluc    = models.IntegerField(default=3)
    Diem_tieuchuan        = models.IntegerField(default=2)
    def save(self):
        self.Diem_tieuchuan = self.Muc_quantrong_nluc * self.Muc_thanhthao_nluc
        return super(Congviec_nangluc, self).save()

    def __str__(self):
        return f"{self.nangluc_cv.name} of {self.chucdanh_CV.Ten_vitri_full}"


class danhgia_Nangluc_nv(models.Model):
    dotdanhgia_nagluc     = models.CharField(max_length=120, blank=True, null=True)
    Nhanvien_dg_nangluc   = models.ForeignKey(Nhan_vien, null=True, on_delete=models.SET_NULL)
    Quanly_dg_nangluc     = models.ForeignKey(Quanly, null=True, on_delete=models.SET_NULL)
    TenNangluc_congviec   = models.ForeignKey(Congviec_nangluc, null=True, on_delete=models.SET_NULL)
    tu_danhgia_dapung     = models.IntegerField(default=3)
    quanly_danhgia        = models.IntegerField(default=3)
    ketqua_danhgia        = models.IntegerField(default=3)
    Kha_nang_dapung       = models.IntegerField(default=3)
    Diem_manh             = models.CharField(max_length=120, blank=True, null=True)
    Diem_khacphuc         = models.CharField(max_length=120, blank=True, null=True)
    start_date            = models.DateTimeField(auto_now_add=True)















def add_khung_nangluc(request):
    ten_nhom_nangluc = Mota_Cv7.objects.all()

    if request.method == 'POST':
        data = request.POST

        Nang_luc_2s = Nang_luc_2.objects.filter(loai_nang_luc_id=3)
        Mota_Cv7s= Mota_Cv7.objects.all()

        for nangluc_cv in Nang_luc_2s:
            for chucdanh_CV in Mota_Cv7s:

                khoa_hoc = Congviec_nangluc.objects.create(
                    name=data['name'],
                    nangluc_cv=nangluc_cv,
                    Muc_quantrong_nluc=data['Muc_quantrong_nluc'],
                    Muc_thanhthao_nluc=data['Muc_thanhthao_nluc'],
                    Diem_tieuchuan=data['Diem_tieuchuan'],
                    chucdanh_CV = chucdanh_CV,
                )
        return redirect('list_nangluc_2')
    context = {'ten_nhom_nangluc': ten_nhom_nangluc}

    return render(request, 'nangluc/Congviec_nangluc_add.html')


@login_required
def Kequa_nangluc(request):
    Nhanvien_dg_nangluc = request.GET.get('Nhanvien_dg_nangluc')
    dgnl = Danhgia_nluc.objects.filter()
    # sumnl = Danhgia_nluc.objects.all().aggregate(Sum('Nhanvien_dg_nangluc')).values()
    sumnl = Danhgia_nluc.objects.filter(Nhanvien_dg_nangluc__don_vi_id=13).aggregate(
    Sum('Nhanvien_dg_nangluc')).values()
    # tdg=nl.annotate(tqldg=Sum('tu_danhgia_dapung'))
    #   qldg=nl.annotate(tqldg=Sum('Quanly_danhgia'))
    print(sumnl)
    context = {'nhanvien': dgnl, 'sumnl': sumnl}
    return render(request, 'nangluc/Ketqua_danhgia.html', context)




def Khung_nangluc_list(request):
    form = Khung_nangluc(request.POST or None)
    queryset = Congviec_nangluc.objects.filter(nangluc_cv_id =3)
    context = {'queryset': queryset, 'form': form, }

    if request.method == 'POST':
        nangluc_cv = form['nangluc_cv'].value()
        chucdanh_CV = form['chucdanh_CV'].value()
        name = form['name'].value()

        if (name != ''):
            queryset = Congviec_nangluc.objects.filter(
                name__icontains=form['name'].value(),
            )
        if (chucdanh_CV != ''):
            # queryset = queryset.filter(chucdanh_CV_id=chucdanh_CV,nangluc_cv_id = nangluc_cv)
            queryset = queryset.filter(chucdanh_CV_id=chucdanh_CV)

            print('chức danh công việc:''queryset')
        context = {'queryset': queryset, 'form': form, }
        #  queryset = Congviec_nangluc.objects.filter(Q(chucdanh_CV_id=chucdanh_CV)|Q( nangluc_cv_id =nangluc_cv)
        Diem_kq = Congviec_nangluc.objects.filter(chucdanh_CV_id=chucdanh_CV).aggregate(nv=Sum('Diem_tieuchuan'))
        print('Điểm:''Diem_kq')

        if form['Xuất_Excel'].value() == True:


            responese = HttpResponse(content_type='application/ms-excel')
            # responese['Content-Disposition'] = 'attachment; filename=Khung_Nang_luc'+'  '+'.xls'
            responese['Content-Disposition'] = 'attachment; filename=' + chucdanh_CV + '_KhungNL.xls'

            wb = xlwt.Workbook(encoding='utf-8')
            # wb.set_paper(9)
            # wb.repeat_rows(10, 10)

            ws = wb.add_sheet(str(chucdanh_CV))

            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            font_style.font.shadow = True
            ws.write(0, 1, '   UBND TP.HỒ CHÍ MINH')
            ws.write(0, 3, '   CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM', font_style)
            ws.write(1, 3, '           Độc lập-Tự do-Hạnh phúc')
            ws.write(1, 1, 'TỔNG CÔNG TY TM SÀI GÒN-TNHH MTV', font_style)

            TIEUDE = xlwt.easyxf(
                'font: color RED, bold 1, name calibri, height 520;'
                'align: vertical center, horizontal center, wrap on;'
                'pattern:pattern_back_colour dark_red_ega;'
            )
            TIEUDE2 = xlwt.easyxf(
                'font: color BLUE, bold 1, name Calibri, height 250;'

                'pattern:pattern_back_colour dark_red_ega;')


            top_row = 3
            bottom_row = 3
            left_column = 0
            right_column = 5
            ws.write_merge(top_row, bottom_row, left_column, right_column, 'PHIẾU TIÊU CHUẨN NĂNG LỰC', TIEUDE)

            rows1 = queryset.values_list('chucdanh_CV__Ten_Nhom_CV')[1]
            rows3 = queryset.values_list('chucdanh_CV__bo_phan__ten_bp')[1]
            rows4 = queryset.values_list('chucdanh_CV__id')[1]

            ws.write(5, 2, "Chức danh công việc:", TIEUDE2)
            ws.write(5, 3, rows1, TIEUDE2)
            ws.write(6, 2, "Đơn vị:", TIEUDE2)
            ws.write(6, 3, rows3, TIEUDE2)
            ws.write(7, 2, "Mã chức danh:", TIEUDE2)
            # ws.write(7,2,  rows4, TIEUDE2)
            row_num = 9
            for_left = xlwt.easyxf(
                "font: bold 1, color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            TABLE_HEADER = xlwt.easyxf(
                'font: bold 1, color blue, name calibri, height 250;'
                'align: vertical center, horizontal center, wrap on;'
                'borders: top double, bottom double, left double, right double;'
                'pattern: pattern solid, pattern_fore_colour yellow, pattern_back_colour dark_red_ega;'
            )
            # ----Định dạng chiều rộng cột
            ws.col(0).width = 2000
            ws.col(1).width = 2000
            ws.col(2).width = 10000
            ws.col(3).width = 4000
            ws.col(4).width = 4000
            ws.col(5).width = 4000
            ws.col(6).width = 6000

            columns = ['STT', 'Mã ', 'Tên năng lực', ' Mức độ quan trọng', 'Mức độ thành thạo', 'Điểm tiêu chuẩn', ]
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            # ----Định dạng chữ
            stt = 1
            font_style = xlwt.XFStyle()
            font_style.font.italic = False
            for_left = xlwt.easyxf(
                "font: color blue; borders: left thin, right thin, top thin, bottom thin; pattern: pattern solid, fore_color white;")
            rows = queryset.values_list('stt', 'nangluc_cv__ma_nangluc', 'nangluc_cv__name', 'Muc_quantrong_nluc',
                                        'Muc_thanhthao_nluc', 'Diem_tieuchuan', )
            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, (row[col_num]), for_left)
            # print('Số cột', col_num)
            # print('Số hàng', row_num)
            for_foot = xlwt.easyxf("font: color blue;  pattern: pattern solid, fore_color white;")
            for_foot_ng = xlwt.easyxf('font: color blue, name calibri, height 320;'
                                      'align: vertical center, horizontal center,')
            TABLE_HEADER2 = xlwt.easyxf(
                'font: bold 1, color blue, name calibri, height 220;'
                'align: vertical center, horizontal center;'
            )


            ws.write(row_num + 2, 2, 'TỔNG ĐIỂM', TABLE_HEADER)
            ws.write(row_num + 2, col_num, xlwt.Formula('sum(f10:f32))'), TABLE_HEADER)

            ws.write(row_num + 5, 1, 'Ngày ... tháng 12 năm 2022', for_foot_ng)
            ws.write(row_num + 6, 1, 'Người phê duyệt', TABLE_HEADER2)
            ws.write(row_num + 5, 3, 'Ngày .... tháng 12 năm 2022', for_foot_ng)
            ws.write(row_num + 6, 3, 'Người xem xét', TABLE_HEADER2)
            ws.write(row_num + 5, 5, 'Ngày ... tháng 12 năm 2022', for_foot_ng)
            # ws.write_merge(row_num + 18,row_num + 19, row_num + 20,row_num + 21,  'Người được đánh giá', TABLE_HEADER2)
            ws.write(row_num + 6, 5, 'Người thiết lập', TABLE_HEADER2)

            wb.save(responese)
            return responese

        total_queryset = queryset.count()
        context = {'queryset': queryset, 'form': form, }


    return render(request, 'nangluc/Khung_nangluc_list.html', context)



@login_required
def Danhgia_nangluc_list3(request):
    Nhanvien_dg_nangluc = request.GET.get('Nhanvien_dg_nangluc')
    form = Danhgia_nlform(request.POST or None)
    if Nhanvien_dg_nangluc == None:
        danhgia_nangluc_list = Danhgia_nluc.objects.all()
    else:
        danhgia_nangluc_list = Danhgia_nluc.objects.filter(Nhanvien_dg_nangluc__ho_lot_thuong_dung=Nhanvien_dg_nangluc)
    chucdanh_CV2 = Nhan_vien.objects.all()

    context = {'Nhanvien_duoc_dg_nangluc': chucdanh_CV2, 'danhgia_nangluc_list2': danhgia_nangluc_list, 'form': form}
    Diem_kq = Danhgia_nluc.objects.aggregate(Count('Ketqua_danhgia'))

    from django.db.models import Sum
    total_tu_dg = (danhgia_nangluc_list.aggregate(total=Sum('tu_danhgia_dapung', field="tu_danhgia_dapung*3"))['total'])
    total_ql = (danhgia_nangluc_list.aggregate(total=Sum('Quanly_danhgia', field="Quanly_danhgia*1"))['total'])

    total_mucqt = (danhgia_nangluc_list.aggregate(total=Sum('TenNangluc_congviec__Muc_quantrong_nluc',
                                                            field="TenNangluc_congviec__Muc_quantrong_nluc"))['total'])

    total_tt = (danhgia_nangluc_list.aggregate(total=Sum('TenNangluc_congviec__Muc_thanhthao_nluc',
                                                         field="TenNangluc_congviec.Muc_thanhthao_nluc"))['total'])

    total_diemchuan = (danhgia_nangluc_list.aggregate(total=Sum('Diem_tieuchuan',
                                                                field="TenNangluc_congviec.Muc_quantrong_nluc *self.TenNangluc_congviec.Muc_thanhthao_nluc"))[
        'total'])

    total_diemcdat = (danhgia_nangluc_list.aggregate(total=Sum('Diem_dat',
                                                               field="Diem_dat*1"))['total'])
    #ketqua_nangluc = total_diemcdat / total_diemchuan

    if form['Xuất_Excel'].value() == False:
        responese = HttpResponse(content_type='application/ms-excel')
        responese['Content-Disposition'] = 'attachment; filename=NS_DG' + '.xls'
        #responese['Content-Disposition'] = 'attachment; filename=' + Nhanvien_dg_nangluc + '_KhungNL.xls'

        #responese['Content-Disposition'] = 'attachment; filename='+ Nhanvien_dg_nangluc + '.xls'
       # responese['Content-Disposition'] = 'attachment; filename=str(Nhanvien_dg_nangluc)'+'d.xls'

#===============================================================================================================
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet(str(Nhanvien_dg_nangluc))
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        font_style.font.shadow = True
        ws.write(0, 1, 'UBND THÀNH PHỒ HỒ CHÍ MINH, Congty')
        ws.write(0, 4, '   CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM', font_style)
        ws.write(1, 4, '           Độc lập-Tự do-Hạnh phúc, Congty')
        ws.write(1, 0, 'TỔNG CÔNG TY TM SÀI GÒN- TNHH MTV', font_style)

        TIEUDE = xlwt.easyxf(
            'font: color RED, bold 1, name Arial, height 320;'
            'align: vertical center, horizontal center, wrap on;'
            'pattern:pattern_back_colour dark_red_ega;')

        TIEUDE2 = xlwt.easyxf(
            'font: color BLUE, bold 1, name Arial, height 250;'
            'pattern:pattern_back_colour dark_red_ega;')

        top_row = 4
        bottom_row = 4
        left_column = 0
        right_column = 9
        ws.write_merge(top_row, bottom_row, left_column, right_column, 'ĐÁNH GIÁ NĂNG LỰC', TIEUDE)

        rows1 = danhgia_nangluc_list.values_list('Nhanvien_dg_nangluc__ho_lot_thuong_dung')[1]
        rows2 = danhgia_nangluc_list.values_list('Nhanvien_dg_nangluc__vitri_CV__Ten_vitri_full')[1]
        rows3 = danhgia_nangluc_list.values_list('Nhanvien_dg_nangluc__bo_phan__ten_bp')[1]
        row_phay = (", ",)

        ws.write(5, 1, "Họ tên:", TIEUDE2)
        ws.write(5, 2, rows1 +row_phay+ rows2, TIEUDE2)
        ws.write(6, 1, "Đơn vị:", TIEUDE2)
        ws.write(6, 2, rows3, TIEUDE2)

        row_num = 9
        for_left = xlwt.easyxf(
            "font: bold 1, color blue; borders: top double, bottom double, left double, right double; align: horiz left")
        TABLE_HEADER = xlwt.easyxf(
            'font: bold 1, color blue, name Tahoma, height 220;'
            'align: vertical center, horizontal center, wrap on;'
            'borders: top double, bottom double, left double, right double;'
            'pattern: pattern solid, pattern_fore_colour light_yellow, pattern_back_colour dark_red_ega;'
        )

        ws.col(0).width = 1200
        ws.col(1).width = 2000
        ws.col(2).width = 7500
        ws.col(3).width = 1800
        ws.col(4).width = 2000
        ws.col(5).width = 1900
        ws.col(6).width = 1900
        ws.col(7).width = 2000
        ws.col(8).width = 2000
        ws.col(9).width = 1800
        # ------------------
        columns = ['Số TT', 'Mã NL', 'Tên năng lực', 'Mức độ quan trọng', 'Mức độ Thành thạo', ' Tự đánh giá',
                   'Cấp trên đánh giá', 'Kết quả Đánh giá', 'Điểm KQ tiêu chuẩn', 'Điểm  KQ đánh giá']
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
        # ----Định dạng chữ
        font_style = xlwt.XFStyle()
        font_style.font.italic = False
        for_left = xlwt.easyxf(
            "font: color blue; borders: left thin, right thin, top thin, bottom thin; pattern: pattern solid, fore_color white;")

        rows = danhgia_nangluc_list.values_list('TenNangluc_congviec__stt', 'TenNangluc_congviec__nangluc_cv__ma_nangluc',
                                                'TenNangluc_congviec__nangluc_cv__name',
                                                'TenNangluc_congviec__Muc_quantrong_nluc',
                                                'TenNangluc_congviec__Muc_thanhthao_nluc', 'Diem_dat', 'Diem_manh','Diem_khacphuc','Kha_nang_dapung',
                                                'Kha_nang_dapung')
        #'tu_danhgia_dapung','Quanly_danhgia', 'Ketqua_danhgia',
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
               # print(col_num)
                # ws.write(row_num,col_num, str(row[col_num]),  for_left)
                ws.write(row_num, col_num, (row[col_num]), for_left)

        print('Số cột', col_num)
        print('Số hàng', row_num)
        for_foot = xlwt.easyxf("font: color blue;  pattern: pattern solid, fore_color white;")
        for_foot_ng = xlwt.easyxf('font: color blue, name Tahoma, height 220;'
                                  'align: vertical center, horizontal center,')
        TABLE_HEADER2 = xlwt.easyxf(
            'font: bold 1, color blue, name Tahoma, height 160;'
            'align: vertical center, horizontal center;'
        )
        tam1=""
        ws.write(row_num + 2, 2, 'TỔNG ĐIỂM', TABLE_HEADER)
        ws.write(row_num + 2, 3, total_mucqt, TABLE_HEADER)
        ws.write(row_num + 2, 4, total_tt, TABLE_HEADER)
        ws.write(row_num + 2, 5, tam1, TABLE_HEADER)
        ws.write(row_num + 2, 6, tam1, TABLE_HEADER)
        ws.write(row_num + 2, 7, tam1, TABLE_HEADER)
        ws.write(row_num + 2, 8, tam1, TABLE_HEADER)
        ws.write(row_num + 2, 9, tam1, TABLE_HEADER)
        # ws.write(row_num + 2, col_num, xlwt.Formula('sum(j11:j35)'), TABLE_HEADER)
        # ws.write(row_num + 2, col_num -1, xlwt.Formula('sum(i11:i35)'), TABLE_HEADER)
        ws.write(row_num + 3, 2, 'MỨC ĐỘ ĐÁP ỨNG', TABLE_HEADER)
       # ws.write(row_num + 3, col_num,  TABLE_HEADER)

        ws.write(row_num + 5, 2, 'NHẬN XÉT CỦA NGƯỜI ĐÁNH GIÁ', TIEUDE2)
        ws.write(row_num + 6, 0, 'STT', TABLE_HEADER)
        ws.write(row_num + 6, 1, 'Mã số', TABLE_HEADER)
        ws.write(row_num + 6, 2, 'Tên năng lực', TABLE_HEADER)
        ws.write(row_num + 6, col_num, xlwt.Formula('sum(j11:j35)'), TABLE_HEADER)

        ws.write(row_num + 7, 0, '...', TABLE_HEADER)
        ws.write(row_num + 7, 1, '...', TABLE_HEADER)
        ws.write(row_num + 7, 2, '...', TABLE_HEADER)
        ws.write(row_num + 7, col_num, xlwt.Formula('sum(j11:k35)'), TABLE_HEADER)

        ws.write(row_num + 10, 1, 'Ngày .... tháng 12 năm 2022', for_foot_ng)
        ws.write(row_num + 11, 1, 'Người phê duyệt', TABLE_HEADER2)
        ws.write(row_num + 10, 3, 'Ngày .... tháng 12 năm 2022', for_foot_ng)
        ws.write(row_num + 11, 3, 'Người đánh giá', TABLE_HEADER2)
        ws.write(row_num + 10, 7, 'Ngày ... tháng 12 năm 2022', for_foot_ng)
        # ws.write_merge(row_num + 18,row_num + 19, row_num + 20,row_num + 21,  'Người được đánh giá', TABLE_HEADER2)
        ws.write(row_num + 11, 7, 'Người được đánh giá', TABLE_HEADER2)
        wb.save(responese)
        return responese
    context = {'Nhanvien_duoc_dg_nangluc': chucdanh_CV2, 'danhgia_nangluc_list2': danhgia_nangluc_list,
               'total_mucqt': total_mucqt, 'total_tt': total_tt,
               'total_diemchuan': total_diemchuan,
               'total_diemcdat': total_diemcdat,
            #   'ketqua_nangluc': ketqua_nangluc,
               'form': form, 'total_tu_dg': total_tu_dg, 'total_ql': total_ql}
    return render(request, 'nangluc/Danhgia_nangluc2.html', context)





=====================
#
@login_required
def Danhgia_nangluc_list_goc(request):
    Nhanvien_dg_nangluc = request.GET.get('Nhanvien_dg_nangluc')
    form = Danhgia_nlform(request.POST or None)

    if Nhanvien_dg_nangluc == None:
        danhgia_nangluc_list = Danhgia_nluc.objects.all()
    else:
        danhgia_nangluc_list = Danhgia_nluc.objects.filter(Nhanvien_dg_nangluc__ho_lot_thuong_dung=Nhanvien_dg_nangluc)
    chucdanh_CV2 = Nhan_vien.objects.all()
    # print(danhgia_nangluc_list)
    context = {'Nhanvien_duoc_dg_nangluc': chucdanh_CV2, 'danhgia_nangluc_list2': danhgia_nangluc_list, 'form': form}

    Diem_kq = Danhgia_nluc.objects.aggregate(Count('Ketqua_danhgia'))

    # print('Điểm:''Diem_kq').value()

    from django.db.models import Sum
    total_tu_dg = (danhgia_nangluc_list.aggregate(total=Sum('tu_danhgia_dapung', field="tu_danhgia_dapung*3"))['total'])
    total_ql = (danhgia_nangluc_list.aggregate(total=Sum('Quanly_danhgia', field="Quanly_danhgia*1"))['total'])

    total_mucqt = (danhgia_nangluc_list.aggregate(total=Sum('TenNangluc_congviec__Muc_quantrong_nluc',
                                                            field="TenNangluc_congviec__Muc_quantrong_nluc"))['total'])

    total_tt = (danhgia_nangluc_list.aggregate(total=Sum('TenNangluc_congviec__Muc_quantrong_nluc',
                                                         field="TenNangluc_congviec.Muc_quantrong_nluc *self.TenNangluc_congviec.Muc_thanhthao_nluc"))[
        'total'])

    total_diemchuan = (danhgia_nangluc_list.aggregate(total=Sum('Diem_tieuchuan',
                                                                field="TenNangluc_congviec.Muc_quantrong_nluc *self.TenNangluc_congviec.Muc_thanhthao_nluc"))[
        'total'])

    total_diemcdat = (danhgia_nangluc_list.aggregate(total=Sum('Diem_dat',
                                                               field="Diem_dat*1"))['total'])

    #ketqua_nangluc = total_diemcdat / total_diemchuan

    if form['Xuất_Excel'].value() == False:
        responese = HttpResponse(content_type='application/ms-excel')
        responese['Content-Disposition'] = 'attachment; filename=' + Nhanvien_dg_nangluc + '.xls'
        #responese['Content-Disposition'] = 'attachment; filename='+ Nhanvien_dg_nangluc + '.xls'
       # responese['Content-Disposition'] = 'attachment; filename=str(Nhanvien_dg_nangluc)'+'d.xls'

#===============================================================================================================

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet(str(Nhanvien_dg_nangluc))

        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        font_style.font.shadow = True
        ws.write(0, 1, 'UBND THÀNH PHỒ HỒ CHÍ MINH')
        ws.write(0, 4, '   CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM', font_style)
        ws.write(1, 4, '           Độc lập-Tự do-Hạnh phúc')
        ws.write(1, 0, 'TỔNG CÔNG TY TM SÀI GÒN- TNHH MTV', font_style)


        TIEUDE = xlwt.easyxf(
            'font: color RED, bold 1, name Arial, height 320;'
            'align: vertical center, horizontal center, wrap on;'
            'pattern:pattern_back_colour dark_red_ega;')

        TIEUDE2 = xlwt.easyxf(
            'font: color BLUE, bold 1, name Arial, height 250;'

            'pattern:pattern_back_colour dark_red_ega;')


        top_row = 4
        bottom_row = 4
        left_column = 0
        right_column = 9
        ws.write_merge(top_row, bottom_row, left_column, right_column, 'ĐÁNH GIÁ NĂNG LỰC', TIEUDE)


        rows1 = danhgia_nangluc_list.values_list('Nhanvien_dg_nangluc__ho_lot_thuong_dung')[1]
        rows2 = danhgia_nangluc_list.values_list('Nhanvien_dg_nangluc__vitri_CV__Ten_vitri_full')[1]
        rows3 = danhgia_nangluc_list.values_list('Nhanvien_dg_nangluc__bo_phan__ten_bp')[1]
        row_phay = (", ",)

        ws.write(5, 1, "Họ tên:", TIEUDE2)
        ws.write(5, 2, rows1 +row_phay+ rows2, TIEUDE2)
        ws.write(6, 1, "Đơn vị:", TIEUDE2)
        ws.write(6, 2, rows3, TIEUDE2)

        row_num = 9
        for_left = xlwt.easyxf(
            "font: bold 1, color blue; borders: top double, bottom double, left double, right double; align: horiz left")
        TABLE_HEADER = xlwt.easyxf(
            'font: bold 1, color blue, name Tahoma, height 220;'
            'align: vertical center, horizontal center, wrap on;'
            'borders: top double, bottom double, left double, right double;'
            'pattern: pattern solid, pattern_fore_colour light_yellow, pattern_back_colour dark_red_ega;'
        )

        ws.col(0).width = 1200
        ws.col(1).width = 2000
        ws.col(2).width = 7500
        ws.col(3).width = 1800
        ws.col(4).width = 2000
        ws.col(5).width = 1900
        ws.col(6).width = 1900
        ws.col(7).width = 2000
        ws.col(8).width = 2000
        ws.col(9).width = 1800
        # ------------------
        columns = ['Số TT', 'Mã NL', 'Tên năng lực', 'Mức độ quan trọng', 'Mức độ Thành thạo', ' Tự đánh giá',
                   'Cấp trên đánh giá', 'Kết quả Đánh giá', 'Điểm KQ tiêu chuẩn', 'Điểm  KQ đánh giá']
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
        # ----Định dạng chữ
        font_style = xlwt.XFStyle()
        font_style.font.italic = False
        for_left = xlwt.easyxf(
            "font: color blue; borders: left thin, right thin, top thin, bottom thin; pattern: pattern solid, fore_color white;")

        rows = danhgia_nangluc_list.values_list('TenNangluc_congviec__stt', 'TenNangluc_congviec__nangluc_cv__ma_nangluc',
                                                'TenNangluc_congviec__nangluc_cv__name',
                                                'TenNangluc_congviec__Muc_quantrong_nluc',
                                                'TenNangluc_congviec__Muc_thanhthao_nluc', 'Diem_dat', 'Diem_manh','Diem_khacphuc','Kha_nang_dapung',
                                                'Kha_nang_dapung')

        #'tu_danhgia_dapung','Quanly_danhgia', 'Ketqua_danhgia',
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                # ws.write(row_num,col_num, str(row[col_num]),  for_left)
                ws.write(row_num, col_num, (row[col_num]), for_left)

        print('Số cột', col_num)
        print('Số hàng', row_num)
        for_foot = xlwt.easyxf("font: color blue;  pattern: pattern solid, fore_color white;")
        for_foot_ng = xlwt.easyxf('font: color blue, name Tahoma, height 220;'
                                  'align: vertical center, horizontal center,')
        TABLE_HEADER2 = xlwt.easyxf(
            'font: bold 1, color blue, name Tahoma, height 160;'
            'align: vertical center, horizontal center;'
        )

        ws.write(row_num + 2, 2, 'TỔNG ĐIỂM', TABLE_HEADER)
        ws.write(row_num + 2, 3, total_mucqt, TABLE_HEADER)
        ws.write(row_num + 2, 4, total_tt, TABLE_HEADER)
        ws.write(row_num + 2, 5, total_tu_dg, TABLE_HEADER)
        ws.write(row_num + 2, 6, total_ql, TABLE_HEADER)
        ws.write(row_num + 2, 7, '..', TABLE_HEADER)
        ws.write(row_num + 2, 8, total_diemchuan, TABLE_HEADER)
        ws.write(row_num + 2, 9, total_diemcdat, TABLE_HEADER)

        #   ws.write(row_num + 2, col_num, xlwt.Formula('sum(j11:j35)'), TABLE_HEADER)
        #   ws.write(row_num + 2, col_num -1, xlwt.Formula('sum(i11:i35)'), TABLE_HEADER)

        ws.write(row_num + 3, 2, 'MỨC ĐỘ ĐÁP ỨNG', TABLE_HEADER)
       # ws.write(row_num + 3, col_num,  TABLE_HEADER)

        ws.write(row_num + 5, 2, 'NHẬN XÉT CỦA NGƯỜI ĐÁNH GIÁ', TIEUDE2)
        ws.write(row_num + 6, 0, 'STT', TABLE_HEADER)
        ws.write(row_num + 6, 1, 'Mã số', TABLE_HEADER)
        ws.write(row_num + 6, 2, 'Tên năng lực', TABLE_HEADER)
        ws.write(row_num + 6, col_num, xlwt.Formula('sum(j11:j35)'), TABLE_HEADER)

        ws.write(row_num + 7, 0, '...', TABLE_HEADER)
        ws.write(row_num + 7, 1, '...', TABLE_HEADER)
        ws.write(row_num + 7, 2, '...', TABLE_HEADER)
        ws.write(row_num + 7, col_num, xlwt.Formula('sum(j11:k35)'), TABLE_HEADER)

        ws.write(row_num + 10, 1, 'Ngày .... tháng 12 năm 2022', for_foot_ng)
        ws.write(row_num + 11, 1, 'Người phê duyệt', TABLE_HEADER2)
        ws.write(row_num + 10, 3, 'Ngày .... tháng 12 năm 2022', for_foot_ng)
        ws.write(row_num + 11, 3, 'Người đánh giá', TABLE_HEADER2)
        ws.write(row_num + 10, 7, 'Ngày ... tháng 12 năm 2022', for_foot_ng)
        # ws.write_merge(row_num + 18,row_num + 19, row_num + 20,row_num + 21,  'Người được đánh giá', TABLE_HEADER2)
        ws.write(row_num + 11, 7, 'Người được đánh giá', TABLE_HEADER2)
        wb.save(responese)
        return responese
    context = {'Nhanvien_duoc_dg_nangluc': chucdanh_CV2, 'danhgia_nangluc_list2': danhgia_nangluc_list,
               'total_mucqt': total_mucqt, 'total_tt': total_tt,
               'total_diemchuan': total_diemchuan,
               'total_diemcdat': total_diemcdat,
            #   'ketqua_nangluc': ketqua_nangluc,
               'form': form, 'total_tu_dg': total_tu_dg, 'total_ql': total_ql}
    return render(request, 'nangluc/Danhgia_nangluc2.html', context)






from django.views.generic.base import TemplateView

class CSVPageView(TemplateView):
    template_name = "nangluc/excel_home.html"


import xlwt
from django.http import HttpResponse
from django.contrib.auth.models import User

def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Username', 'First Name', 'Last Name', 'Email Address', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response


# excel_app/views.py
import xlwt
from django.http import HttpResponse

def export_styling_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Styling Data') # this will make a sheet named Users Data - First Sheet
    styles = dict(
        bold = 'font: bold 1',
        italic = 'font: italic 1',
        # Wrap text in the cell
        wrap_bold = 'font: bold 1; align: wrap 1;',
        # White text on a blue background
        reversed = 'pattern: pattern solid, fore_color blue; font: color white;',
        # Light orange checkered background
        light_orange_bg = 'pattern: pattern fine_dots, fore_color white, back_color orange;',
        # Heavy borders
        bordered = 'border: top thick, right thick, bottom thick, left thick;',
        # 16 pt red text
        big_red = 'font: height 320, color red;',
    )

    for idx, k in enumerate(sorted(styles)):
        style = xlwt.easyxf(styles[k])
        ws.write(idx, 0, k)
        ws.write(idx, 1, styles[k], style)

    wb.save(response)

    return response
from xlutils.copy import copy # http://pypi.python.org/pypi/xlutils
from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd
import xlwt
from django.http import HttpResponse
import os

def export_write_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    # EG: path = excel_app/sample.xls
    path = os.path.dirname(__file__)
    file = os.path.join(path, 'sample.xls')

    rb = open_workbook(file, formatting_info=True)
    r_sheet = rb.sheet_by_index(0)

    wb = copy(rb)
    ws = wb.get_sheet(0)

    row_num = 22 # index start from 0
    rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num])
    # wb.save(file) # will replace original file
    # wb.save(file + '.out' + os.path.splitext(file)[-1]) # will save file where the excel file is
    wb.save(response)
    return response
