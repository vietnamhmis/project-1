from django.test import TestCase

# Create your tests here.
#from dbview.models import DbView
#pip install django-database-view

#pip install xhtml2pdf
#pip install= --pre xhtml2pdf
#

    def save(self, *args, **kwargs):
        if self.Bac_2:
            CL_Luong_moi_PA_1 = self.Bac_2 * self.Nhom_luong.luong_toi_thieu - self.Luong_cu
            CL_Luong_BHXH_PA_1 = self.Bac_2 * self.Nhom_luong.luong_toi_thieu - self.Luong_BHXH_cu

        super(Phuongan_luong, self).save(*args, **kwargs)


    def save(self, *args, **kwargs):

        self.CL_Luong_moi_PA_1 = 0
        for i in range(2):
            a = int(self.Bac_1)
            if a >  self.CL_Luong_moi_PA_1:
                 self.CL_Luong_moi_PA_1 = a
            else:
                self.CL_Luong_moi_PA_1 =1
        super(Phuongan_luong, self).save(*args, **kwargs)




  Congviec_nanglucs = Congviec_nangluc.objects.all()
  Danhgia_nlucs = Congviec_nangluc.objects.all()

  for Danhgia_nluc in Danhgia_nlucs:
      khoa_hoc = Danhgia_nluc.objects.get_or_create(
          Diem_tieuchuan = Danhgia_nluc.TenNangluc_congviec.Diem_tieuchuan,
          Diem_dat = Danhgia_nluc.TenNangluc_congviec.Diem_tieuchuan, # Tạm lấy điểm đạt băng điểm ti6u chuẩn
)


#

 if form['Xuất_Excel'].value() == True:
        responese = HttpResponse(content_type='application/ms-excel')
        responese['Content-Disposition'] = 'attachment; filename=DS_HDLD_'+'.xls'
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

        rows1 = 1
        rows2 = 2
        rows3 = qs.values_list('Ho_ten__don_vi__Ten_DV')[1]
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
        columns = ['Số TT', 'Họ tên', 'Đơn vị', 'Chức danh/vị trí', 'Hợp đồng', 'Ngày ký','Đến ngày',
                   'Hệ số lương', 'bậc','Mức lương', ]
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
        # ----Định dạng chữ
        font_style = xlwt.XFStyle()
        font_style.font.italic = False


        rows = qs.values_list('Ho_ten__ho_lot_thuong_dung', 'Ho_ten__don_vi__Ten_DV',
                                                'Ho_ten__vitri_CV__Ten_Nhom_CV',
                                                'Loai_hd',
                                                'Tu_ngay',

                                                'Den_ngay',
                                                'Heso', 'Bac', 'Muc_luong',
                                                )


        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
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



        ws.write(row_num + 3, 1, 'Ngày .... tháng 12 năm 2022', for_foot_ng)
        ws.write(row_num + 4, 1, 'Người phê duyệt', TABLE_HEADER2)
        ws.write(row_num + 3, 3, 'Ngày .... tháng 12 năm 2022', for_foot_ng)
        ws.write(row_num + 4, 3, 'Người đánh giá', TABLE_HEADER2)
        ws.write(row_num + 3, 7, 'Ngày ... tháng 12 năm 2022', for_foot_ng)
        # ws.write_merge(row_num + 18,row_num + 19, row_num + 20,row_num + 21,  'Người được đánh giá', TABLE_HEADER2)
        ws.write(row_num + 4, 7, 'Người được đánh giá', TABLE_HEADER2)
        wb.save(responese)
        return responese