from django import forms
from .models import BHXHTN


class BHXHTN_SearchForm(forms.ModelForm):
    class Meta:
        model = BHXHTN
        fields = ['HOTEN', 'SOBHXH',  'SOBL', ]
        widgets = {

                    }
        labels = {
            'SOBHXH': ('Số sổ BHXH:'),
            'HOTEN': ('Họ tên'),
         }

    Xuất_Excel = forms.BooleanField(required=False)



    NGAYSINH_tu=forms.DateField(
                    input_formats=['%d/%m/%Y'],
                    widget=forms.DateTimeInput(attrs={
                        'class': 'form-control datetimepicker-input',
                        'data-target': '#datetimepicker1'
                         })
    )
    NGAYSINH_den=forms.DateField(
                    input_formats=['%d/%m/%Y'],
                    widget=forms.DateTimeInput(attrs={
                        'class': 'form-control datetimepicker-input',
                        'data-target': '#datetimepicker1'
                         })
    )

#------------------------------------------------------------------------------------------------------------






















class Form_bhxh(forms.ModelForm):
    class Meta:
        model = BHXHTN
        fields = '__all__'
        widgets = {
            'NGAYSINH': forms.DateInput(format=('%m-%d-%Y'),attrs={'class': 'form-control','placeholder': 'Chọn ngày','type': 'date'}),
            'TUNGAY': forms.DateInput(format=('%d-%m-%Y'), attrs={'class': 'form-control','placeholder': 'Chọn ngày','type': 'date'}),
            'NGAYCMND': forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'form-control','placeholder': 'Chọn ngày','type': 'date'}),
            'NGAYBL': forms.DateInput(format=('%d-%m-%Y'), attrs={'class': 'form-control','placeholder': 'Chọn ngày','type': 'date'}),

        }
        labels = {
            'SOBHXH': ('Số sổ BHXH:'),'HOTEN':('Họ và tên:'),'NGAYSINH':('Ngày sinh:'),'GIOITINH': ('Giới tính'),  'SOBL':('Số biên lai'), 'SOKCB':('Số thẻ KCB:'),
             'NAMSINH': ('Số Thẻ Khám chữa bệnh:'),'NOIKHAI':('Nơi Khai:'),'tinh_thanh':('Tỉnh thành nơi khai:'),'quan_huyen': ('Quận/Huyện'),
            'phuong_xa':('Phường xã'), 'NOICAP': ('Nơi cấp CCCD/CMND:'),'MA_TINHCMT':('Tỉnh cấp CNND:'),'QUOCTICH':('Quốc tịch:'),'DANTOC': ('Dân tộc:'),

            'MA_BV': ('Mã bệnh viện:'),'TUNGAY': ('Từ ngày'),'ML':  ('Mức lương'),'TYLE_NSNN': ('Tỉ lệ Nhà nước'),'SOTHANG': ('Số tháng'),
            'DIACHI_LH': ('Địa chỉ liên hệ:'), 'DIACHI': ('Địa chỉ :'), 'TINH_LH': ('Tỉnh liên hệ'), 'HUYEN_LH': ('Huyện'), 'XA_LH': ('Xã liên hệ'),

            'MAPB': ('Mã :'),'MADT': ('Điện thoại'),'TUTHANG':  ('Từ tháng:'),'DENTHANG': ('Đến tháng'),'TYLE': ('Tỉ lệ'),
            'TYLEDONG': ('Tỉ lệ đóng:'), 'MLDK': ('Mức lương Đăng ký'),'HSL': ('Hệ số lương:'), 'HSL_DK': ('Hệ số lương Đăng ký'), 'TAMTRU': ('Tạm trú:'),
            'GHICHU': ('Ghi chú:'), 'GIAM_DO_CHET': ('Giảm do chết'), 'MA_TINH': ('Mã tỉnh'),'SDT': ('Số điện thoại'),
            'MA_CA':('Mã CA '), 'DIACHIHK':('Địa chỉ hộ khẩu'),

           }




from nhansu.models import Tinh, Quan_huyen, Phuong_xa

#---------------
class DiaphuongForm(forms.ModelForm):
    class Meta:
        model = BHXHTN
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quan_huyen'].queryset = Quan_huyen.objects.none()
        self.fields['phuong_xa'].queryset = Phuong_xa.objects.none()

       # self.fields['bo_phan'].queryset = Bo_phan.objects.none()
      #  self.fields['to_nhom'].queryset = To_nhom.objects.none()

        if 'tinh_thanh' in self.data:
            try:
                tinh_thanh_id = int(self.data.get('tinh_thanh'))
                self.fields['quan_huyen'].queryset = Quan_huyen.objects.filter(Tinh_thanh_id=tinh_thanh_id).order_by('Ten_quan')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['quan_huyen'].queryset = self.instance.quan_huyen.quan_huyen_set.order_by('Ten_quan')

        if 'quan_huyen' in self.data:
            try:
                quan_huyen_id = int(self.data.get('quan_huyen'))
                self.fields['phuong_xa'].queryset = Phuong_xa.objects.filter(quan_huyen_id=quan_huyen_id).order_by('Ten_xa')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['phuong_xa'].queryset = self.instance.phuong_xa.phuong_xa_set.order_by('Ten_xa')


class bhxh_Form(forms.ModelForm):
    class Meta:
        model = BHXHTN
        fields = '__all__'
        help_texts = {


        }
        labels = {

}
        widgets = {

        }

class BHYT_SearchForm(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = BHXHTN
        fields = ['HOTEN', 'SOBHXH', 'phuong_xa', 'SOBL']
        widgets = {
            'HOTEN': forms.TextInput(attrs={'class':'form-control'}),
            'SOBHXH': forms.TextInput(attrs={'class':'form-control'}),
            'SOBL': forms.TextInput(attrs={'class':'form-control'}),
            'XA_NK': forms.TextInput(attrs={'class':'form-control'}),
        }
