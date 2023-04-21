from django.forms import ModelForm
from django import forms
from .models import Don_vi, Bo_phan, To_nhom, Nang_luc_2, KPI_list, Vanban
from django.forms.widgets import NumberInput

from django.template.defaulttags import widthratio


from django import forms
from . models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Don_vi
        fields = '__all__'


#------------------Tạo form dơn vị..............
class DonviForm(forms.ModelForm):
    class Meta:
        model = Don_vi
        fields = '__all__'


#------------------Tạo form Update Đơn vị..............
class DonviUpdateForm(forms.ModelForm):
    class Meta:
        model = Don_vi
        fields = '__all__'


#--------------------CHƯƠNG TRÌNH HIỂN THỊ ĐƠN VỊ............................................
class Don_vi_SearchForm(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = Don_vi
        fields = ['Ten_DV', 'diachi']

#--------------------CHƯƠNG TRÌNH HIỂN THỊ BỘ PHẬN............................................
class Bo_phanForm(forms.ModelForm):
   class Meta:
     model = Bo_phan
     fields = '__all__'
#--------------------CHƯƠNG TRÌNH HIỂN THỊ Bộ PHẬN............................................
class Bo_phanSearchForm(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = Bo_phan
        fields = ['ten_bp', 'don_vi']

#--------------------CHƯƠNG TRÌNH HIỂN THỊ TỔ............................................
class To_nhomForm(forms.ModelForm):
    class Meta:
        model = To_nhom
        fields = '__all__'

class To_Form(forms.ModelForm):
    class Meta:
        model = To_nhom
        fields = '__all__'
 #--------------------CHƯƠNG TRÌNH HIỂN THỊ Bộ PHẬN............................................
class To_nhomSearchForm(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = To_nhom
        fields = ['ten_to', 'bo_phan']
        widgets = {
        'ten_to': forms.TextInput(attrs={'class':'form-control'}),
        'bo_phan': forms.Select(attrs={'class':'form-select'}),
        }

    #********>>>>>>> Đây là chương trình THÊM/SỬA/XÓA KPI ......................................
class Nangluc_SearchForm(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = Nang_luc_2
        fields = ['name', 'loai_nang_luc', 'tochuc_Sudung', 'ho_congviec']
        widgets = {
        'namne': forms.TextInput(attrs={'class':'form-control'}),
        'loai_nang_luc': forms.Select(attrs={'class':'form-select'}),
        }

class form_nangluc(forms.ModelForm):
    class Meta:
        model = Nang_luc_2
        fields = '__all__'

        labels = {
            'name':('Tên năng lực'), 'loai_nang_luc':('Loại Năng lực'),'tochuc_Sudung': ('Tổ chức sử dụng'),
            'NL_muc_1':('Năng lực mức 1: Năng lực làm việc kém'),'NL_muc_2':(' Mức 2: Năng lực làm việc cơ bản'),    'NL_muc_3':('Mức 3: Năng lực làm việc Khá'),
            'NL_muc_4':('Mức 4: Năng lực làm việc Giỏi'),    'NL_muc_5':('Mức 5: Năng lực làm việc Xuất sắc'),
            'image':('Hình ảnh'), 'ho_congviec':('Nhóm công việc sử dụng'),'label':('Gắn nhãn') , 'su_dung':('Sử dụng') ,
            'MoTa_nangluc': ('Mô tả Năng lực'), 'ngay_tao': ('Ngày tạo'), 'ma_nangluc': ('Mã Năng lực'),
        }
        widgets = {
              'ngay_tao': forms.DateInput(format=('%d-%m-%Y'),
                                       attrs={'class':'myDateClass',
                                              'placeholder':'Chọn ngày'}),

            'tochuc_Sudung': forms.Select(attrs={'class':'form-select'}),
            'ho_congviec': forms.Select(attrs={'class':'form-select'}),
            'NL_muc_1':forms.Textarea(attrs={'rows':3}),
            'NL_muc_2':forms.Textarea(attrs={'rows':3}),
            'NL_muc_3':forms.Textarea(attrs={'rows':5}),
            'NL_muc_4':forms.Textarea(attrs={'rows':5}),
            'NL_muc_5':forms.Textarea(attrs={'rows':9}),
            'MoTa_nangluc': forms.Textarea(attrs={'rows':3}),
            'sudung': forms.RadioSelect(),
            }

        help_texts = {
            'name':('Tên năng lực'),

        }






class KPI_SearchForm(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = KPI_list
        fields = ['name', 'loai_kpi']
        widgets = {
        'namne': forms.TextInput(attrs={'class':'form-control'}),
        'loai_kpi': forms.Select(attrs={'class':'form-select'}),
        }

class form_kpi(forms.ModelForm):
    class Meta:
        model = KPI_list
        fields = '__all__'
        labels = {
            'name':('Tên KPI'), 'moTa_kpi':('Mô tả  KPI'),'loai_kpi': ('Loại KPI'),
            'kpo':('Tên KPO'),'tochuc_Sudung': ('Tổ chức sử dụng'),
            'tan_xuat_d_gia':('Tần xuất đánh giá (tháng/năm) '),
            'ma_kpi':('Mã KPI'),'chi_tieu':('Chỉ tiêu'), 'donvi_tinh':('Đơn vị tính'),
            'ti_trong': ('Tỉ trọng'),'ho_congviec':('Nhóm công việc sử dụng'),'tochuc_Sudung':('Tổ chức Sử dụng'),
            'ngaytao': ('Ngày tạo'), 'ngay_update': ('Ngày cập nhật'),'label':('Gắn nhãn'), 'Su_dung':('Sử dụng')
        }

        widgets = {
            'ngay_tao': forms.DateInput(format=('%d-%m-%Y'),
                                       attrs={'class':'myDateClass','type':'date',
                                              'placeholder':'Chọn ngày'}),

            'tochuc_Sudung': forms.Select(attrs={'class':'form-select'}),
            'loai_kpi': forms.Select(attrs={'class':'form-select'}),
            'ho_congviec': forms.Select(attrs={'class':'form-select'}),
            'tan_xuat_d_gia': forms.Select(attrs={'class':'form-select'}),
             'label':forms.Select(attrs={'class':'form-select'}),
             'donvi_tinh':forms.Select(attrs={'class':'form-select'}),
             'moTa_kpi': forms.Textarea(attrs={'rows':2}),
             'Su_dung': forms.RadioSelect(),

            }


class VanbanUpdateForm(forms.ModelForm):
    class Meta:
        model = Vanban
        fields = ['name', 'ma_vanban','image','file_name','MoTa_vanban', 'slug', 'label', 'loai_vanban','su_dung','tochuc_Sudung']

        labels = {
            'name':('Tên văn bản'), 'ma_vanban':('Mã văn bản'),'image': ('Hình ảnh'),
            'file_name':('Tên tập tin'),
            'Currently': ('Hiện hữu'),
            'MoTa_vanban':('Mô tả văn bản '),
            'ngay_tao':('Ngày tạo'),
            'loai_vanban': ('Loại văn bản'), 'su_dung': ('Còn sử dụng'),
            'tochuc_Sudung': ('Tổ chức, đơn vị sử dụng'),
            'label': ('nhãn hiệu'),
            'image': ('Hình ảnh văn bản '),
        }
        widgets = {
            'ngay_tao': forms.DateInput(format=('%d-%m-%Y'),
                                       attrs={'class':'myDateClass','type':'date',
                                              'placeholder':'Chọn ngày'}),

            'tochuc_Sudung': forms.Select(attrs={'class':'form-select'}),
            'loai_vanban': forms.Select(attrs={'class':'form-select'}),
            'label':forms.Select(attrs={'class':'form-select'}),
             'MoTa_vanban': forms.Textarea(attrs={'rows':5}),
            'sudung': forms.RadioSelect(),

            }

        help_texts = {
            'name':('Tên văn bản'),
            'file_name':('Tên tập tin'),
            'MoTa_vanban':('Mô tả tòm tắt nội dung văn bản '),
        }

