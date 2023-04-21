from django import forms
from .models import Dinhbien_HC, Dinhbien_ca, tonghopdinhbien

#Chương trình định biên hành chính
class list_dinhbien_hc(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = Dinhbien_HC
        fields = '__all__'
        widgets = {
            'don_vi': forms.Select(attrs={'class':'form-select'}),
            'bo_phan': forms.Select(attrs={'class':'form-select'}),

        }
        help_texts = {
            'chuc_vu':('Chức vụ hoặc vị trí công việc'),
            'don_vi':('Ghi tên đơn vị quản lý trực tiếp chức danh, công việc '),
            'bo_phan':('Ghi tên bộ phận quản lý trực tiếp chức danh, công việc '),
            'to_nhom':('Ghi tên Tổ quản lý trực tiếp chức danh, công việc '),

        }
        labels = {
            'chucdanh': ('Chức vụ:'),'don_vi':('Đơn vị:'),'bo_phan':('Bộ phận:'),'to_nhom': ('Tổ'),
            'Noi_dung_cviec': ('Nội dung công việc'),
            'khoiluong_nam':('Khối lượng công việc 1 năm(phút)'),
            'sophut_th_1lan': ('Thời gian yêu cầu 1 đơn vị tính (phút) '),
            'tan_xuat_lviec': ('Tần suất thực hiện công việc(ngày/tuần/tháng/năm)'),
            'Tong_phut_1nam': ('Tổng thời lao động trong năm (phút)'),
            'dinhbienhc': ('Lao động định biên hành chính'),
        }



#Chương trình định biên ca, kíp
class Form_dinhbien_ca(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = Dinhbien_ca
        fields = '__all__'

        widgets = {
            'don_vi': forms.Select(attrs={'class':'form-select'}),
            'bo_phan': forms.Select(attrs={'class':'form-select'}),
        }
        help_texts = {
            'chuc_vu':('Chức vụ hoặc vị trí công việc'),
            'don_vi':('Ghi tên đơn vị quản lý trực tiếp chức danh, công việc '),
            'bo_phan':('Ghi tên bộ phận quản lý trực tiếp chức danh, công việc '),
            'to_nhom':('Ghi tên Tổ quản lý trực tiếp chức danh, công việc '),

        }
        labels = {
            'chucdanh': ('Chức vụ:'),'don_vi':('Đơn vị:'),'bo_phan':('Bộ phận:'),'to_nhom': ('Tổ'),


            'Noi_dung_cviecca': ('Nội dung công việc trong ca:'),
            'laodong_ca_1':('Bố trí lao động trong ca 1 (người)'),
            'laodong_ca_2': ('Bố trí lao động trong ca 2 (người)'),
            'laodong_ca_3': ('Bố trí lao động trong ca 3 (người)'),

            'khoiluongsp_ca_1':('Khối lượng các sản phẩm trong ca 1'),
            'khoiluongsp_ca_2':('Khối lượng các sản phẩm trong ca 2'),
            'khoiluongsp_ca_3':('Khối lượng các sản phẩm trong ca 3'),

            'sophut_th_1lanc': ('Thời gian yêu cầu 1 đơn vị tính (phút) '),

            'Thoigian_yc_ca_1': ('Tổng thời yêu cầu trong ca 1 (phút) '),
            'Thoigian_yc_ca_2': ('Tổng thời yêu cầu trong ca 2 (phút)'),
            'Thoigian_yc_ca_3': ('Tổng thời yêu cầu trong ca 3 (phút)'),

            'Tong_phut_1namc': ('Tổng thời lao động trong năm (phút)'),
            'dinhbienca': ('Lao động định biên'),
        }

   #Chương trình tổng hợp định biên
class Form_dinhbien(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = tonghopdinhbien
        fields = '__all__'
        widgets = {
            'don_vi': forms.Select(attrs={'class':'form-select'}),
            'bo_phan': forms.Select(attrs={'class':'form-select'}),
            'to_nhom': forms.Select(attrs={'class':'form-select'}),
            'chucdanh_dinhbien': forms.TextInput(attrs={'class':'form-control'}),
        }