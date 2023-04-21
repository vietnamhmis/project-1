from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView

from .forms import BHXHTN_SearchForm, Form_bhxh, BHYT_SearchForm
from .models import BHXHTN

import datetime
import xlwt
# Create your views here.


#>>>>>>>>>>>: Chương trình :



@login_required
def list_bhxhtn(request):
    form = BHXHTN_SearchForm(request.POST or None)
    queryset = BHXHTN.objects.all()[1:100]
    context = {'queryset': queryset,'form':form,}
    if request.method == 'POST':
        #XA_NK=form['XA_NK'].value()
        queryset = BHXHTN.objects.filter(
            HOTEN__icontains=form['HOTEN'].value(),
            SOBHXH__icontains=form['SOBHXH'].value(),
            SOBL__icontains=form['SOBL'].value(),
            NGAYSINH__range=[
							form['NGAYSINH_tu'].value(),
							form['NGAYSINH_den'].value()
						]

        )


       # if (XA_NK != ''):
           # queryset = queryset.filter(vitri_CV_id=XA_NK)
        if form['Xuất_Excel'].value() == True:
            responese = HttpResponse(content_type='application/ms-excel')
            responese['Content-Disposition'] = 'attachment; filename=DS BHXHTN_D03'+ \
                    str(datetime.datetime.now())+'.xls'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('nhanvien')

            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            font_style.font.shadow = True
            ws.write(0,1,'CÔNG TY TNHH ',font_style )
            ws.write(1,1,'TƯ VẤN BẢO HIỂM HUY HOANG',font_style)
            ws.write(0,5,'CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM',font_style )
            ws.write(0,11,'Mẫu D03TS')
            ws.write(1,11,'505 QĐ-BHXH')
            ws.write(1,5,'           Độc lập-Tự do-Hạnh phúc')

            ws.write(2,1,'Mã đơn vị BHXH cấp',font_style)
            ws.write(2,3,'Mã số thuế:',font_style)
            ws.write(3,1,'ĐC:96 D, Đường số 8, Thủ Đức',font_style)
            ws.write(4,1,'ĐT: 091266432')
            ws.write(4,2,'Email: huyhoang@gmail.com')
            ws.write(5,2,'Đối tượng tham gia(ghi loại đối tượng tham gia BHYT (người nghèo, người có công, trẻ em dưới 6 tuổi, hộ gia đình ...); Mã đối tượng:')
            ws.write(5,9,' Lương cơ sở:1.490.000 đồng')
            ws.write(6,2,'Nguồn đóng:cơ quan LĐTBXH, cơ quan TC')
            ws.write(6,9,' Tỷ lệ NSNN hỗ trợ theo quy định (70% đối với hộ cận nghèo, 30% đối với học sinh sinh viên)%')

            TIEUDE = xlwt.easyxf(
                'font: color RED, bold 1, name Tahoma, height 220;'
                'align: vertical center, horizontal center, wrap on;'
                'pattern:pattern_back_colour dark_red_ega;'
                                       )
            ws.write(4,5,'DANH SÁCH NGƯỜI CHỈ THAM GIA BHYT ',TIEUDE)

            row_num = 8
            for_left = xlwt.easyxf("font: bold 1, color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            TABLE_HEADER = xlwt.easyxf(
                'font: bold 1, color blue, name Tahoma, height 220;'
                'align: vertical center, horizontal center, wrap on;'
                'borders: top double, bottom double, left double, right double;'
                'pattern: pattern solid, pattern_fore_colour yellow, pattern_back_colour dark_red_ega;'
                                       )
              #----Định dạng chiều rộng cột
            ws.col(0).width = 1000
            ws.col(1).width = 4500
            ws.col(2).width = 2500
            ws.col(3).width = 3000
            ws.col(4).width = 2500
            ws.col(5).width = 4000
            ws.col(6).width = 2000
            ws.col(7).width = 4000
            ws.col(8).width = 3500
            ws.col(9).width = 3500
            ws.col(10).width = 2000
            ws.col(11).width = 2000
            ws.col(12).width = 2000
            columns =['Số TT', 'Họ và tên','Mã BHXH',  'Ngày sinh', 'Giới tính', 'Địa chỉ cư trú','Nơi đăng ký KCB', 'Ngày biên lai', 'Tiền lương hưu, trợ cấp TN, TS'
                    'NS địa phương','HTrợ khác', 'Thời gian tham gia từ tháng','số tháng', 'Ghi chú']
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            #----Định dạng chữ
            font_style= xlwt.XFStyle()
            font_style.font.italic = False
            for_left = xlwt.easyxf("font: color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            rows= queryset.values_list('id', 'HOTEN','SOBHXH','NGAYSINH', 'GIOITINH', 'DIACHI','MA_BV', 'NGAYBL', 'ML_dong','TYLE_NSNN','TUTHANG','SOTHANG','GHICHU')
            for row in rows:
                row_num +=1
                for col_num in range(len(row)):
                    ws.write(row_num,col_num, str(row[col_num]), for_left)
            wb.save(responese)
            return responese
        total_queryset = queryset.count()
        context = {'queryset': queryset,'form':form,}
    return render(request,'bhxh/bhxhtn_list.html', context)



def bhxh_profile(request, id):
    fmnv = BHXHTN.objects.get(id=id)

    return render(request, 'bhxh/bhxhtn_tokhai.html', {'f_bh':fmnv})



@login_required(login_url='/dangnhap/')

def update_bhxh(request, id):
    if request.method == 'POST':
        dv = BHXHTN.objects.get(pk=id)
        fmhd = Form_bhxh(request.POST, instance=dv)
        if fmhd.is_valid():
            fmhd.save()
    else:
        dv = BHXHTN.objects.get(pk=id)
        fmhd = Form_bhxh(instance=dv)
    return render(request,'bhxh/bhxhtn_update.html', {'form': fmhd})

# This functions will delete/xóa- ok
def delete_BHXH(request, id):
    pnv = BHXHTN.objects.get(pk=id)
    if request.method == 'POST':
        pnv.delete()
        return HttpResponseRedirect('/bhxhtn/')
    return render(request, 'bhxh/bhxh_delete.html')
        #return redirect('/')

##********>>>>>>> kết thúc chương trình THÊM/SỬA/XÓA NHÂN VIÊN:>>>>>>>>>>>>>>>>>>>>
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
    return render(request, 'bsc/list_choise_diaphuong.html', context)