from django import forms
from .models import bangluong, hd_laodong, luongthang, Chamcongchitiet, Phuongan_luongbhxh

from django.utils.translation import gettext_lazy as _

from enroll.models import Nhan_vien

class Phuongan_luong_f(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = Phuongan_luongbhxh
        fields = '__all__'
        help_texts = {
            'Nhanvien': ('Nhân viên'),

        }
        labels = {
            'Nhanvien': ('Nhân viên'),

        }

class Phuongan_luong(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = Phuongan_luongbhxh
        fields =['Nhom_luong', 'Nhanvien']

        labels = {
            'Nhom_luong': ('Nhóm lương'),
            'Nhanvien': ('Nhân viên'),

        }

class bangluong_list_f(forms.ModelForm):
    class Meta:
        model = bangluong
        fields = '__all__'
        help_texts = {
            'chuc_vu': _('Chức vụ hoặc vị trí công việc'),

        }
        labels = {
            'Nhom_luong': ('Nhóm lương'),
            'Heso': ('Hệ số lương'),
            'bac': ('Bậc lương'),
        }

class nangluong(forms.ModelForm):
    Xuất_Word = forms.BooleanField(required=False)
    class Meta:
        model = hd_laodong
        #model = Nhan_vien
        fields = [
           'So_hopdong', 'Ho_ten',  'Loai_hd', 'Tu_ngay', 'Den_ngay', 'Ht_traluong','bangluong',  'Bac','Muc_luong',
        ]
        widgets = {
            'Tu_ngay': forms.DateInput(format=('%d-%m-%Y'),
                                       attrs={'class':'myDateClass',
                                              'placeholder':'Select a date'}),
        }
        help_texts = {
            'chuc_vu': _('Chức vụ hoặc vị trí công việc'),
           # 'Loai_hd': ('Chọn loại hình thức nâng lương: Định kì, Đột xuất, Đặc cách'),
            'Tu_ngay': ('Ngày hưởng lương mới:'),
            'Den_ngay': ('Đến ngày:'),
        }
        labels = {
            'Ho_ten': ('Họ và tên:'),
           # 'Loai_hd': ('Hình thức nâng lương:'),
            'Tu_ngay': ('Ngày hưởng lương mới:'),
            'Den_ngay': ('Ngày nâng lương lần sau:'),
            'bangluong': ('Bảng lương'),
            'Nhom_luong': ('Nhóm lương:'),
            'bac': ('Bậc lương:'),
        }


class nhanvien_hopdong(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    Xuất_Word = forms.BooleanField(required=False)
    class Meta:
        model = hd_laodong
        fields = [
            'Ho_ten' ,
        ]


class hd_laodong_list_f(forms.ModelForm):
    Xuất_Word = forms.BooleanField(required=False)
    class Meta:
        model = hd_laodong
        fields = [
           'So_hopdong', 'Ho_ten',  'Loai_hd', 'Tu_ngay', 'Den_ngay', 'Ht_traluong','bangluong', 'Heso', 'Bac','Muc_luong',
        ]
        widgets = {
            'Heso': forms.Select(attrs={'class':'form-select'}),

            'Tu_ngay': forms.DateInput(format=('%d-%m-%Y'),
                                         attrs={'class': 'form-control','placeholder': 'Nhập ngày hết hạn hợp đồng','type': 'date'}),

            'Den_ngay': forms.DateInput(format=('%d-%m-%Y'),
                                         attrs={'placeholder': 'Nhập ngày hết hạn hợp đồng','type': 'date'}),
        }
        help_texts = {
            'chuc_vu': _('Chức vụ hoặc vị trí công việc'),
            'Loai_hd': ('Chọn hợp đồng lao động: Có thời hạn, không xác định thời theo Điều 20 BLLĐ'),
            'Tu_ngay': ('Hợp đồng có hiệu lực từ ngày:'),
            'Den_ngay': ('Đến ngày:'),
            'Ht_traluong': ('Chọn Hình thức trả lương: Theo Điều 96 BLLĐ'),
        }
        labels = {
            'So_hopdong': ('Số Hợp đồng lao động'),
            'Ho_ten': ('Họ và tên:'),
            'Loai_hd': ('Loại hợp đồng lao động:'),
            'Tu_ngay': ('Hợp đồng có hiệu lực từ ngày:'),
            'Den_ngay': ('Đến ngày:'),
            'Ht_traluong': ('Hình thức trả lương:'),
            'bangluong': ('Bảng lương'),
            'Nhom_luong': ('Nhóm lương:'),
            'Heso': ('Hệ số lương:'),
            'bac': ('Bậc lương:'),
            'Muc_luong': ('Mức lương hàng tháng:'),
            'Phucap_kn': ('Phụ cấp kiêm nhiệm:'),
            'Phucap_khac': ('Phụ cấp khác:'),
        }


class ketthuc_laodong_f(forms.ModelForm):
    Xuất_Word = forms.BooleanField(required=False)
    class Meta:
        model = hd_laodong
        fields = [
           'So_hopdong', 'Ho_ten',  'Loai_hd', 'Heso', 'Bac','Muc_luong',
        ]
        widgets = {
            'Tu_ngay': forms.DateInput(format=('%d-%m-%Y'),
                                       attrs={'class':'myDateClass',
                                              'placeholder':'Select a date'}),
        }
        help_texts = {
            'chuc_vu': _('Chức vụ hoặc vị trí công việc'),
            'Loai_hd': ('Chọn hợp đồng lao động: Có thời hạn, không xác định thời theo Điều 20 BLLĐ'),
            'Tu_ngay': ('Hợp đồng có hiệu lực từ ngày:'),

        }
        labels = {
            'So_hopdong': ('Số Hợp đồng lao động'),
            'Ho_ten': ('Họ và tên:'),
            'Loai_hd': ('Loại hợp đồng lao động:'),
            'Tu_ngay': ('Hợp đồng có hiệu lực từ ngày:'),
                  }

class luongthang_Form(forms.Form):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = luongthang

        fields = ( 'don_vi', 'bo_phan',  'Nam', 'Thang_tra_luong',)

        widgets = {
        'Nam': forms.Select(attrs={'class':'form-select'}),
        'Thang_tra_luong': forms.Select(attrs={'class':'form-select'}),
        'bo_phan': forms.Select(attrs={'class':'form-select'}),
        }

        help_texts = {
            'Muc_luongBHXH': ('Lương BHXH'),

        }
        labels = {
            'Thang_tra_luong': ('Tháng trả lương'),
            'hoten_nhanvien': ('Họ và tên:'),
            'Heso': ('Hệ số lương:'),

            'Muc_luong': ('Mức lương hàng tháng:'),
            'Phucap_kn': ('Phụ cấp kiêm nhiệm:'),
            'Phucap_khac': ('Phụ cấp khác:'),

        }

class luongthang_searchForm(forms.Form):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = luongthang
        fields = ('Thang_tra_luong', 'Nam', 'hoten_nhanvien',)
        widgets = {
        'Nam': forms.Select(attrs={'class':'form-select'}),
        'thang': forms.Select(attrs={'class':'form-select'}),
        'Nhan_vien': forms.Select(attrs={'class':'form-select'}),
        }

        help_texts = {
            'Thang_tra_luong': ('Tháng trả lương'),

        }
        labels = {
            'Thang_tra_luong': ('Tháng trả lương'),
            'hoten_nhanvien': ('Họ và tên:'),
            'Nam': ('Năm trả lươn lương:'),
        }

class hop_dong_form(forms.Form):
    Hoten_nhanvien = forms.CharField(label="Họ tên Nhân viên")
    tuthang = forms.IntegerField (label='Từ tháng')
    denthang = forms.IntegerField (label='Đến tháng')


class Chamcong_f(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = Chamcongchitiet

        fields = ( 'don_vi', 'bo_phan', 'to_nhom', 'Nam', 'thang',)
        widgets = {
        'Nam': forms.Select(attrs={'class':'form-select'}),
        'thang': forms.Select(attrs={'class':'form-select'}),
        'bo_phan': forms.Select(attrs={'class':'form-select'}),
        }
        help_texts = {
            'Nhan_vien': ('Chọn tên CBCNV'),

            'thang': ('Tháng chấm công'),
            'Nam': ('Năm chấm công'),
        }
        labels = {
            'thang': ('Tháng chấm công'),
            'Nhanvien': ('Họ và tên:'),
            'Nam': ('Năm chấm công:'),
        }


class luongthang_f(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = luongthang

        fields = ( 'don_vi', 'bo_phan', 'to_nhom', 'Nam', 'Thang_tra_luong',)
        widgets = {
        'Nam': forms.Select(attrs={'class':'form-select'}),
        'Thang_tra_luong': forms.Select(attrs={'class':'form-select'}),
        'bo_phan': forms.Select(attrs={'class':'form-select'}),
        }
        help_texts = {
            'Nhan_vien': ('Chọn tên CBCNV'),

            'Thang_tra_luong': ('Tháng chấm công'),
            'Nam': ('Năm chấm công'),
        }
        labels = {
            'Thang_tra_luong': ('Tháng chấm công'),
            'Nhanvien': ('Họ và tên:'),
            'Nam': ('Năm chấm công:'),
        }