from django.test import TestCase
    def save(self, *args, **kwargs):
        self.Tile_hoanthanh = int(self.Ketqua_danhgia) / int(self.Ten_kpi.chi_tieu)

        self.Diem_congviec = int(self.Tile_hoanthanh)

        self.Diem_trongso = int(self.Diem_congviec) * int(self.Ten_kpi.ti_trong)

        super(Danhgia_KPI, self).save(*args, **kwargs)




# Create your tests here.
    path('dg_kpi/', views.danhgia_kpi_view,name="danhgia_kpi_view"),
    path('dg_kpi/insert_student', views.Insert_kpi,name="insert_kpi"),
    path('dg_kpi/update_kpi', views.update_kpi,name="update_kpi"),
    path('dg_kpi/delete_kpi', views.delete_kpi,name="delete_kpi"),


#-------------------Quản lý  update năng lực---------Danhgia_nangluc_quanly.html-----------------------------------------------------
def danhgia_kpi_view(request): #Danhgia_nangluc_quanly.html
    Nhanvien_dg_KPI = request.GET.get('Nhanvien_dg_KPI')
    form = Danhgia_nangluc_form(request.POST or None)
    danhgia_nangluc_list = Danhgia_nluc.objects.all()[1:10]
    context = {'students': danhgia_nangluc_list, 'form': form, }

    if request.method == 'POST':
        Landanhgia_KPI = form['Landanhgia_KPI'].value()
        Nhanvien_dg_KPI = form['Nhanvien_dg_KPI'].value()
        Ten_kpi = form['Ten_kpi'].value()

        if (Landanhgia_KPI != ''):
            danhgia_nangluc_list = Danhgia_nluc.objects.filter(
                Landanhgia_KPI__icontains=form['Landanhgia_KPI'].value(),
                Nhanvien_dg_KPI_id=Nhanvien_dg_KPI,
            )
    chucdanh_CV2 = Nhan_vien.objects.filter(don_vi_id=7)
    context = {'Nhanvien_duoc_dg_nangluc': chucdanh_CV2, "productss": danhgia_nangluc_list, 'students': danhgia_nangluc_list, 'form': form}

    Diem_kq = Danhgia_nluc.objects.aggregate(Count('Ketqua_danhgia'))
    from django.db.models import Sum

    total_tu_dg = (danhgia_nangluc_list.aggregate(total=Sum('tu_danhgia_dapung', field="tu_danhgia_dapung*3"))['total'])
    total_ql = (danhgia_nangluc_list.aggregate(total=Sum('Quanly_danhgia', field="Quanly_danhgia*10"))['total'])
    total_chung = (danhgia_nangluc_list.aggregate(total=Sum('Ketqua_danhgia', field="Ketqua_danhgia"))['total'])

    total_mucqt = (danhgia_nangluc_list.aggregate(total=Sum('Ten_kpi__Muc_quantrong_nluc',
                                                  field="Ten_kpi__Muc_quantrong_nluc"))['total'])
    total_tt = (danhgia_nangluc_list.aggregate(total=Sum('Ten_kpi__Muc_thanhthao_nluc',
                                                  field="Ten_kpi.Muc_thanhthao_nluc"))['total'])
    total_diemchuan = (danhgia_nangluc_list.aggregate(total=Sum('Ten_kpi__Diem_tieuchuan',
                                                   field="Ten_kpi__Diem_tieuchuan * 2"))['total'])
    total_Diem_tu_danhgia = (danhgia_nangluc_list.aggregate(total=Sum('Diem_tu_danhgia',
                                                   field="Diem_tu_danhgia*1"))['total'])
    total_diemcdat = (danhgia_nangluc_list.aggregate(total=Sum('Diem_dat',
                                                   field="Diem_dat"))['total'])

    if total_diemcdat and total_diemchuan:
        ketqua_nangluc = round((total_diemcdat/total_diemchuan ),2)
    else:
        ketqua_nangluc =0


    if form['Xuất_Excel'].value() == True:
        responese = HttpResponse(content_type='application/ms-excel')
        responese['Content-Disposition'] = 'attachment; filename=Danh_gia_NL_'+'.xls'
        #responese['Content-Disposition'] = 'attachment; filename=' + Nhanvien_dg_KPI + '_KhungNL.xls'
        #responese['Content-Disposition'] = 'attachment; filename='+ Nhanvien_dg_KPI + '.xls'
       # responese['Content-Disposition'] = 'attachment; filename=str(Nhanvien_dg_KPI)'+'d.xls'
#===============================================================================================================
        wb = xlwt.Workbook(encoding='utf-8')
        #ws = wb.add_sheet(str(Nhanvien_dg_KPI))
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

        rows1 = danhgia_nangluc_list.values_list('Nhanvien_dg_KPI__ho_lot_thuong_dung')[1]
        rows2 = danhgia_nangluc_list.values_list('Nhanvien_dg_KPI__vitri_CV__Ten_Nhom_CV')[1]
        rows3 = danhgia_nangluc_list.values_list('Nhanvien_dg_KPI__bo_phan__ten_bp')[1]
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


        rows = danhgia_nangluc_list.values_list('Ten_kpi__stt', 'Ten_kpi__nangluc_cv__ma_nangluc',
                                                'Ten_kpi__nangluc_cv__name',
                                                'Ten_kpi__Muc_quantrong_nluc',
                                                'Ten_kpi__Muc_thanhthao_nluc',
                                                'Ten_kpi__Diem_tieuchuan',
                                                'tu_danhgia_dapung', 'Quanly_danhgia', 'Ketqua_danhgia',
                                                'Diem_dat', 'Ketqua_tile')


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

        ws.write(row_num + 1, 6, total_tu_dg, TABLE_HEADER)# Tự đánh giá
        ws.write(row_num + 1, 7, total_ql, TABLE_HEADER) #Cấp trên đánh giá
        ws.write(row_num + 1, 8, total_chung, TABLE_HEADER) #Kết quả thống nhất

        ws.write(row_num + 1, 9, total_diemcdat, TABLE_HEADER) #Điểm đánh giá
        ws.write(row_num + 1, 10, ketqua_nangluc, TABLE_HEADER)

        ws.write(row_num + 3, 1, 'Ngày .... tháng ...năm 2023', for_foot_ng)
        ws.write(row_num + 4, 1, 'Người phê duyệt', TABLE_HEADER2)
        ws.write(row_num + 3, 3, 'Ngày .... tháng ...năm 2023', for_foot_ng)
        ws.write(row_num + 4, 3, 'Người đánh giá', TABLE_HEADER2)
        ws.write(row_num + 3, 7, 'Ngày ... tháng ....năm 2023', for_foot_ng)
        # ws.write_merge(row_num + 18,row_num + 19, row_num + 20,row_num + 21,  'Người được đánh giá', TABLE_HEADER2)
        ws.write(row_num + 4, 7, 'Người được đánh giá', TABLE_HEADER2)
        wb.save(responese)
        return responese

    if form['Xuất_Word'].value() == True:

        doc = DocxTemplate("word_template/M_danhgiangluc.docx")
        queryset5 = {
                  "Ho_ten":danhgia_nangluc_list.values_list('Nhanvien_dg_KPI__ho_lot_thuong_dung')[1] ,
                  "Chuc_danh":(danhgia_nangluc_list.values_list('Nhanvien_dg_KPI__vitri_CV__Ten_Nhom_CV'))[1] ,

                  "Don_vi":danhgia_nangluc_list.values_list('Nhanvien_dg_KPI__bo_phan__ten_bp')[1] ,
                  'total_diemchuan': total_diemchuan,
                  'total_diemcdat': total_diemcdat,
                  'tiledat' :ketqua_nangluc,

                   "productss": danhgia_nangluc_list,

                    }
        doc.render(queryset5)
        doc.save('thu_word/NL_'+ Nhanvien_dg_KPI + '.docx')

    context = {'Nhanvien_duoc_dg_nangluc': chucdanh_CV2, 'danhgia_nangluc_list1': danhgia_nangluc_list,
               "productss": danhgia_nangluc_list, 'students': danhgia_nangluc_list, 'form': form,
               'total_mucqt': total_mucqt, 'total_tt': total_tt,
               'total_diemchuan': total_diemchuan,

               'form': form, 'total_tu_dg': total_tu_dg,
               'total_ql': total_ql,
               'total_chung':total_chung,
               'total_Diem_tu_danhgia':total_Diem_tu_danhgia,
               'total_diemcdat': total_diemcdat,

               'ketqua_nangluc': ketqua_nangluc,


               }

    return render(request,"kpi_bsc/Danhgia_kpi_quanly.html",context)

@csrf_exempt#Danhgia_nangluc_aab.html
def Insert_kpi(request):
    Ten_kpi=request.POST.get("Ten_kpi")
    Quanly_danhgia=request.POST.get("Quanly_danhgia")
    tu_danhgia_dapung=request.POST.get("tu_danhgia_dapung")
    Ketqua_danhgia=request.POST.get("Ketqua_danhgia")

    try:
        student=Danhgia_nluc(Ten_kpi=Ten_kpi,Quanly_danhgia=Quanly_danhgia, tu_danhgia_dapung=tu_danhgia_dapung, Ketqua_danhgia=Ketqua_danhgia,)
        student.save()
        stuent_data={"id":student.id,"start_date":student.start_date,"error":False,"errorMessage":"Thêm dữ liệu thành công"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Không thêm được"}
        return JsonResponse(stuent_data,safe=False)


@csrf_exempt#Danhgia_nangluc_aab.html
def update_kpi(request):
    data=request.POST.get("data")
    dict_data=json.loads(data)
    try:
        for dic_single in dict_data:
            student=Danhgia_nluc.objects.get(id=dic_single['id'])
            #student.Ten_kpi=dic_single['Ten_kpi']
            student.Quanly_danhgia=dic_single['Quanly_danhgia']
            student.Ketqua_danhgia=dic_single['Ketqua_danhgia']
            #student.Diem_dat= student.Ketqua_danhgia * student.Ten_kpi.Muc_quantrong_nluc

            student.save()
        stuent_data={"error":False,"errorMessage":"Cập nhật Thành công"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Không cập nhật được"}
        return JsonResponse(stuent_data,safe=False)

@csrf_exempt#Danhgia_nangluc_aab.html
def delete_kpi(request):
    id=request.POST.get("id")
    try:
        student=Danhgia_nluc.objects.get(id=id)
        student.delete()
        stuent_data={"error":False,"errorMessage":"Xóa hoàn thành"}
        return JsonResponse(stuent_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Xóa không được"}
        return JsonResponse(stuent_data,safe=False)

#-------------------Kếtthúc Quản lý Đanh giá Năng lực----------------------------------------------------------

