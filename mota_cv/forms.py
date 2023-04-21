from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from nhansu.models import Bo_phan, To_nhom
from django.utils.translation import gettext_lazy as _


class Chucdanh_form(forms.ModelForm):
    class Meta:
        model = Chuc_danh
        fields = '__all__'
        #------Nhóm 7 yếu tố-----------
class motacongviec_Form7yt(forms.ModelForm):
    class Meta:
        model = Mota_Cv7
        fields = '__all__'
        help_texts = {
            'Ten_Nhom_CV': ('Vị trí công việc'),
            'don_vi':('Ghi tên đơn vị quản lý trực tiếp VTCV '),
            'bo_phan': ('Ghi tên bộ phận quản lý trực tiếp VTCV '),
            'to_nhom':('Ghi tên Tổ quản lý VTCV '),

        }
        labels = {
            'Ten_Nhom_CV': ('Chức vụ:'),'don_vi':('Đơn vị:'),'bo_phan':('Bộ phận:'),'to_nhom': ('Tổ'),  'Mucdich_cv':('Mục đích công việc'),
            'ma_tenvitri': ('Mã vị trí:'),
            'Ten_vitri_full': ('Chức vụ, vị trí đầy đủ'),
            'Ten_theoluong':  ('Tên vị trí theo bảng lương'),
            'ten_nghe_NNDH': ('Nghề công việc NN Độc hại nguy hiểm theo qui định của Nhà nước'),
            'Phan_loai': ('Phân loại'),
            'Yeu_to_1_trinh_do':('I.TRÌNH ĐỘ /THỜI GIAN ĐÀO TẠO'),
            'Yeu_to_2_Ky_nang':('II. KỸ NĂNG /KINH NGHIỆM LÀM VIỆC'),
            'Yeu_to_3_Trach_nhiem':('III.TRÁCH NHIỆM CỦA CÔNG VIỆC'),
            'Yeu_to_4_Anh_huong':('IV. MỨC ĐỘ ẢNH HƯỞNG CỦA CÔNG VIỆC'),
            'Yeu_to_5_Sangtao':('V. SÁNG TẠO, ĐỔI MỚI CỦA CÔNG VIỆC'),
            'Yeu_to_6_Giaotiep':(' VI.GIAO TIẾP, PHỐI HỢP LÀM VIỆC'),
            'Yeu_to_7_DK_lamviec':('VII.ĐIỀU KIỆN LÀM VIỆC'),
            'Ycau_Ngoaingu_23':('VIII. KỸ NĂNG NGOẠI NGỮ:'),
            'Ycau_CNTT_24':('VIII. KỸ NĂNG CNTT'),
            'Yeu_to_khac': ('KỸ NĂNG KHÁC PHẨM CHẤT CẦN THIẾT CHO CÔNG VIỆC'),
            'Captren': ('Cấp trên:'),
            'diadiem_lv':('Địa điểm làm việc'),
            'Qhe_captren': ('Quan hệ cấp trên'),
            'Qhe_cungcap': ('Quan hệ cùng cấp'),
            'Qhe_capduoi':('Quan hệ cấp dưới'),
            'Qhe_nn_xahoi':('Quan hệ xã hội'),
            'Qhe_khachhang':('Quan hệ khách hàng'),
            'Nh_vu_ket_qua': ('Nhiệm vụ'),
            'Trach_nhiem': ('Trách nhiệm'),
            'Mucdo_anhhuong': ('Mức độ ảnh hưởng'),
            'Ptien_laodong': ('Phương tiện lao động'),
            'Dieu_kienlaodong': ('Điều kiện lao động'),
            'ycau_kynang_khac': ('Kỹ năng khác phục vụ công việc'),
            'tong_diem': ('Tổng điểm')

}
        widgets = {
            'Ten_Nhom_CV': forms.TextInput(attrs={'placeholder': 'Ghi chức vụ/ vụ trí/chức danh công việc mô tả ','class':'form-select'}),
            'don_vi':forms.Select(attrs={'placeholder': 'Chọn đơn vị trực thuộc','class':'form-select'}),
            'bo_phan': forms.Select(attrs={'placeholder': 'Ghi bộ phân đơn vị trực thuộc TD, Phòng/NM/XN/TN../TT','class':'form-select'}),
            'to_nhom': forms.Select(attrs={'placeholder': 'Ghi đơn vị trực thuộc bộ phân, ex: xưởng/tổ','class':'form-select'}),
            'chuc_danh':forms.Select(attrs={'placeholder': 'Chức danh công việc','class':'form-select'}),


            'ma_tenvitri': forms.TextInput(attrs={'class':'form-control'}),
            'Ten_vitri_full': forms.TextInput(attrs={'class':'form-control'}),
            'Ten_theoluong': forms.TextInput(attrs={'class':'form-control'}),
            'ten_nghe_NNDH': forms.TextInput(attrs={'class':'form-control'}),
            'Phan_loai': forms.Select(attrs={'class':'form-control'}),

            'Captren': forms.TextInput(attrs={ 'row':5, 'placeholder':
            'Ghi tên Vị trí cấp trên quản lý trực tiếp VTCV>','class': 'form-control'}),
            'diadiem_lv': forms.TextInput(attrs={'class':'form-control','placeholder': 'Ghi cụ thể địa chỉ làm việc của Vị trí mô tả',}),

             'Qhe_captren':forms.Textarea(attrs={'rows':3, 'class':'form-control',
                                                  'placeholder':'Ghi những liên hệ chính với chức danh/đơn vị nào? '
                                                                'Để giải quyết vấn đề cụ thể gì?'}),
            'Qhe_capduoi':forms.Textarea(attrs={'rows':3, 'class':'form-control',
                                                  'placeholder':'Ghi những liên hệ chính với chức danh/đơn vị nào?'
                                                                ' Để giải quyết vấn đề cụ thể gì?'}),



            'Mucdich_cv':forms.Textarea(attrs={'rows':5, 'class':'form-control','placeholder':'Nêu mục đích chung mà vị trí này tồn tại để đáp ứng, trả lời cho câu hỏi “vị trí này tồn tại để làm gì cho công ty?". '
                                                                                       'Đây chính là các chức năng chính yếu và kết quả tương ứng của'
                                                                                       ' vị trí này. Mục tiêu phải tương ứng với các chức năng '
                                                                                       'và nhiệm vụ mà vị trí đảm nhận. Nêu tối đa 02 mục tiêu chính '
                                                                                       'yếu cho mỗi vị trí công việc. KHÔNG CHÉP LẠI CÁC CHỨC NĂNG '
                                                                                       'Ở MỤC DƯỚI.Ví dụ, đối với vị trí Trưởng phòng '
                                                                                       'nhân sự có chức năng đề xuất chính sách nhân sự, theo dõi và tư vấn thực hiện chính sách thì mục tiêu '
                                                                                       'có thể là “Bảo đảm chất lượng và số lượng nguồn nhân lực cho công ty thông qua việc thực hiện các chính sách nhân '
                                                                                       'sự phù hợp với nhu cầu quản lý và hiệu quả nhất”'}),
            'Qhe_nn_xahoi':forms.Textarea(attrs={'rows':3, 'class':'form-control', 'placeholder':'Ghi những liên hệ chính với chức danh/đơn vị nào? Để giải quyết vấn đề cụ thể gì?'}),
            'Qhe_khachhang':forms.Textarea(attrs={'rows':3, 'class':'form-control',
                                                  'placeholder':'Ghi những liên hệ chính với Vị trí/đơn vị nào?'
                                                                ' Để giải quyết vấn đề cụ thể gì?'}),

            'Nh_vu_ket_qua':forms.Textarea(attrs={'rows':5, 'class':'form-control', 'placeholder':'Ghi đầy đủ, cụ thể và theo trình tự các nội dung công việc của chức danh công việc đang đảm nhận'}),
            'Trach_nhiem': forms.Textarea(attrs={'rows':5, 'placeholder': 'Ghi mức độ trách nhiệm cao nhất đối với kết quả công việc, '
                                                                'Nêu quyền hạn ra quyết định của vị trí liên quan tới sử dụng nhân sự, '
                                                                'thu chi tài chính, quyết định kinh doanh hoặc sản xuất. '
                                                                'KHÔNG LẶP LẠI CÁC NHIỆM VỤ ĐÃ NÊU Ở MỤC TRÊN''- Nhân viên kinh doanh: quyền thương '
                                                                'lượng với khách hàng và quyết định giá trong phạm vi quy định của công ty '
                                                                'và chịu trách nhiệm về hiệu quả kinh doanh'  
                                                                'Kiểm soát chất lượng: quyền dừng sản xuất khi phát hiện lỗi hệ thống trong sản phẩm'
                                                                '- Trưởng phòng HC: quyền đại diện công ty khi làm việc với cơ quan công quyền địa phương và chịu'
                                                                ' trách nhiệm với thông tin cung cấp'
                                                                'tính mạng con người, tài sản và phương tiện làm việc, '
                                                                'Ghi mức độ trách nhiệm cao nhất đối với kết quả công việc, '
                                                                'tính mạng con người, tài sản và phương tiện làm việc',}),

            'Mucdo_anhhuong': forms.TextInput(attrs={'class':'form-control','placehoder':'Lựa chọn mức độ ảnh hưởng đến công ty/đơn vị',}),
            'Ptien_laodong': forms.TextInput(attrs={'placeholder': 'Ghi tên máy móc, thiết bị, dụng cụ đo kiểm, đồ nghề chính yếu để thực hiện các nhiệm vụ nêu trên','class':'form-control'}),
            'Dieu_kienlaodong': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ghi loại điều kiện lao động phù hợp với lựa chọn mục 4.1 và 4.2'}),
            'Yeu_to_1_trinh_do': forms.Select(attrs={'class':'form-select'}),
            'Yeu_to_2_Ky_nang': forms.Select(attrs={'class':'form-select'}),
            'Yeu_to_3_Trach_nhiem': forms.Select(attrs={'class':'form-select'}),
            'Yeu_to_4_Anh_huong': forms.Select(attrs={'class':'form-select'}),
            'Yeu_to_5_Sangtao': forms.Select(attrs={'class':'form-select'}),
            'Yeu_to_6_Giaotiep': forms.Select(attrs={'class':'form-select'}),
            'Yeu_to_7_DK_lamviec': forms.Select(attrs={'class':'form-select'}),

           'Ycau_Ngoaingu_23': forms.Select(attrs={'class':'form-select'}),
            'Ycau_CNTT_24': forms.Select(attrs={'class':'form-select'}),
            'Yeu_to_khac': forms.Select(attrs={'row':5,'class':'form-select'}),

        }

class list_dinhgia_cv7(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = Mota_Cv
        fields = ['don_vi', 'bo_phan', 'Ten_Nhom_CV']
        widgets = {

            'don_vi': forms.Select(attrs={'class':'form-select'}),
        }

class dinhgiaUpdateForm7(forms.ModelForm):
    class Meta:
        model = Mota_Cv7
        fields = ['id', 'Ten_Nhom_CV','mota_Cong_viec', 'don_vi', 'bo_phan', 'to_nhom',
                   'Yeu_to_1_trinh_do', 'Yeu_to_2_Ky_nang','Yeu_to_3_Trach_nhiem', 'Yeu_to_4_Anh_huong',
                  'Yeu_to_5_Sangtao', 'Yeu_to_6_Giaotiep', 'Yeu_to_7_DK_lamviec', 'tong_diem7', 'Nhom_luong']
        labels = {
            'Ten_Nhom_CV': ('Chức vụ:'),'don_vi':('Đơn vị:'),'bo_phan':('Bộ phận:'),'to_nhom': ('Tổ'),
            'Yeu_to_1_trinh_do':('1.Trình độ /Thời gian đào tạo'),
            'Yeu_to_2_Ky_nang':('2. Kỹ năng /Kinh nghiệm làm việc'),
            'Yeu_to_3_Trach_nhiem':('3.Trách nhiệm của công việc'),
            'Yeu_to_4_Anh_huong':('4. Mức độ ảnh hưởng của công việc'),
            'Yeu_to_5_Sangtao':('5. Sáng tạo, đổi mới của công việc'),
            'Yeu_to_6_Giaotiep':(' 6.Giao tiếp, phối hợp làm việc'),
            'Yeu_to_7_DK_lamviec':('7.Điều kiện làm việc'),
            'mota_Cong_viec': ('Mô tả công việc'),
            'tong_diem7': ('Tổng điểm'),
            'Nhom_luong': ('Nhóm lương') ,
        }


        help_texts = {
            'Ten_Nhom_CV': _('Chức vụ hoặc vị trí công việc'),
        }
        error_messages = {
            'name': {
                'max_length': _("Vượt quá ký tư cho phép rồi"),
            },
        }
        widgets = {
            'Ten_Nhom_CV': forms.TextInput(attrs={'class':'form-control','ROWS':'1'}),
            'Yeu_to_1_trinh_do': forms.Select(attrs={'class':'form-select'}),
            'Yeu_to_2_Ky_nang': forms.Select(attrs={'class':'form-select'}),
            'Yeu_to_3_Trach_nhiem': forms.Select(attrs={'class':'form-select'}),
            'Yeu_to_4_Anh_huong': forms.Select(attrs={'class': 'form-select'}),
            'Yeu_to_5_Sangtao': forms.Select(attrs={'class':'form-select'}),
            'Yeu_to_6_Giaotiep': forms.Select(attrs={'class':'form-select'}),
            'Yeu_to_7_DK_lamviec': forms.Select(attrs={'class':'form-select'}),
            'mota_Cong_viec': forms.ClearableFileInput(attrs={'multiple': True}),
            'don_vi':forms.Select(attrs={'class':'form-select'}),
            'bo_phan': forms.Select(attrs={'class':'form-select'}),

        }


class motacongviec_Form2(forms.ModelForm):
    class Meta:
        model = Mota_Cv
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bo_phan'].queryset = Bo_phan.objects.none()
        if 'don_vi' in self.data:
            try:
                don_vi_id = int(self.data.get('don_vi'))
                self.fields['bo_phan'].queryset = Bo_phan.objects.filter(don_vi_id=don_vi_id).order_by('ten_bp')

            except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['bo_phan'].queryset = self.instance.don_vi.bo_phan_set.order_by('ten_bp')


        widgets = {
            'Ten_Nhom_CV': forms.Select(attrs={'placeholder': 'Ghi chức vụ/ vụ trí/chức danh','class':'form-select'}),
            'bo_phan': forms.Select(attrs={'placeholder': 'Ghi bộ phân đơn vị trực thuộc công ty, TD, Phòng/NM/XN/TN../TT','class':'form-select'}),
            'to_nhom': forms.Select(attrs={'placeholder': 'Ghi bđơn vị trực thuộc bộ phân, ex: xưởng/tổ','class':'form-select'}),

            'ma_tenvitri': forms.TextInput(attrs={'class':'form-control'}),
            'Ten_vitri_full': forms.TextInput(attrs={'class':'form-control'}),
            'Ten_theoluong': forms.TextInput(attrs={'class':'form-control'}),
            'ten_nghe_NNDH': forms.TextInput(attrs={'class':'form-control'}),
            'Phan_loai': forms.TextInput(attrs={'class':'form-control'}),

            'Captren': forms.Textarea(attrs={'placeholder': 'Cấp trên trực tiếp điều hành','class': 'form-control account__input-text'}),
            'diadiem_lv': forms.TextInput(attrs={'placeholder': 'Ghi nơi làm việc','class':'form-control'}),
            'Qhe_captren': forms.TextInput(attrs={'class':'form-control'}),
            'Qhe_cungcap': forms.TextInput(attrs={'class':'form-control'}),
            'Qhe_capduoi': forms.TextInput(attrs={'class':'form-control'}),

            'Qhe_nn_xahoi': forms.TextInput(attrs={'class':'form-control'}),
            'Qhe_khachhang': forms.TextInput(attrs={'class':'form-control'}),
            'Nh_vu_ket_qua': forms.Textarea(attrs={'placeholder': 'Nhiệm vụ Ghi đầy đủ, cụ thể và theo trình tự các nội dung công việc của chức danh công việc đang đảm nhận','class': 'form-control account__input-text'}),
           'Trach_nhiem': forms.Textarea(attrs={'placeholder': 'Ghi mức độ trách nhiệm cao nhất đối với kết quả công việc, tính mạng con người, tài sản và phương tiện làm việc','class': 'form-control'}),
            'Mucdo_anhhuong': forms.TextInput(attrs={'placehoder':'Ghi mức độ ảnh hưởng đến công ty/đơn vị','class':'form-control'}),
            'Ptien_laodong': forms.TextInput(attrs={'placeholder': 'Ghi tên máy móc, thiết bị, dụng cụ đo kiểm, đồ nghề chính yếu để thực hiện các nhiệm vụ nêu trên','class':'form-control'}),
            'Dieu_kienlaodong': forms.TextInput(attrs={'class':'form-control'}),

            'muc_ah_cty_11': forms.Select(attrs={'class':'form-select'}),
            'muc_ah_nv_12': forms.Select(attrs={'class':'form-select'}),
            'ycau_trinhdocm_21': forms.Select(attrs={'class':'form-select'}),
            'ycau_k_nghiem_22': forms.Select(attrs={'class':'form-select'}),
            'ycau_Ngoaingu_23': forms.Select(attrs={'class':'form-select'}),
            'ycau_CNTT_24': forms.Select(attrs={'class':'form-select'}),
            'ycau_kehoach_31': forms.Select(attrs={'class':'form-select'}),
            'ycau_sangtao_32': forms.Select(attrs={'class':'form-select'}),
            'ycau_doclap_33': forms.Select(attrs={'class':'form-select'}),
            'ycau_cuongdo_35': forms.Select(attrs={'class':'form-select'}),
            'ycau_giaotiep_34': forms.Select(attrs={'class':'form-select'}),
            'mt_laodong_41': forms.Select(attrs={'class':'form-select'}),
            'muc_rui_ro_42': forms.Select(attrs={'class':'form-select'}),
        }


      #------Nhóm 4 yếu tố-----------
class list_dinhgia_cv(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = Mota_Cv
        fields = ['don_vi', 'bo_phan', 'Ten_Nhom_CV']
        widgets = {

            'don_vi': forms.Select(attrs={'class':'form-select'}),
        }

class list_dinhgia_cv(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = Mota_Cv
        fields = ['don_vi', 'bo_phan', 'Ten_Nhom_CV']
        widgets = {
           # 'don_vi': forms.TextInput(attrs={'class':'form-control'}),
            #'bo_phan': forms.TextInput(attrs={'class':'form-control'}),
           # 'to_nhom': forms.NumberInput(attrs={'class':'form-control'}),

            'don_vi': forms.Select(attrs={'class':'form-select'}),
        }

class dinhgiaUpdateForm(forms.ModelForm):
    class Meta:
        model = Mota_Cv
        fields = ['id', 'Ten_Nhom_CV','mota_Cong_viec', 'don_vi', 'bo_phan', 'to_nhom','muc_ah_cty_11', 'muc_ah_nv_12','ycau_trinhdocm_21', 'ycau_k_nghiem_22',
                  'ycau_Ngoaingu_23', 'ycau_CNTT_24', 'ycau_kehoach_31', 'ycau_sangtao_32','ycau_doclap_33', 'ycau_giaotiep_34','ycau_cuongdo_35', 'mt_laodong_41', 'muc_rui_ro_42']

        labels = {
            'Ten_Nhom_CV': ('Chức vụ:'),'don_vi':('Đơn vị:'),'bo_phan':('Bộ phận:'),'to_nhom': ('Tổ'),
            'muc_ah_cty_11':('I.MỨC ĐỘ TÁC ĐỘNG CỦA CÔNG VIỆC: 1.1 Đến kết quả hoạt động kinh doanh'),
            'muc_ah_nv_12':('1.2 Đến công việc của người khác'),
            'ycau_trinhdocm_21':('II.YÊU CẦU VỀ NĂNG LỰC ĐỂ THỰC HIỆN CÔNG VIỆC: 2.1 Đến kết quả hoạt động kinh doanh'),
            'ycau_k_nghiem_22':('2.2 Về kinh nghiệm:'),
            'ycau_Ngoaingu_23':('2.3 Về trình độ Ngoại ngữ'),
            'ycau_CNTT_24':('2.4 Về trình độ CNTT'),
            'ycau_kehoach_31':('III.ĐẶC TÍNH CỦA CÔNG VIỆC: 3.1 Tính kế hoạch'),
            'ycau_sangtao_32':('3.2.Tính ổn định và sáng tạo'),
            'ycau_doclap_33':('3.3. Tính độc lập'),
            'ycau_giaotiep_34':('3.4 Mức độ phối hợp và kỹ năng giao tiếp'),
            'ycau_cuongdo_35':('3.5. Cường độ lao động'),
            'mt_laodong_41':(' IV. ĐIỀU KIỆN LÀM VIỆC: 4.1.Tính ổn định và sáng tạo'),
            'muc_rui_ro_42':('4.2 Mức độ rủi ro nghề nghiệp'),
            'mota_Cong_viec': ('Mô tả công việc'),
        }

        help_texts = {
            'Ten_Nhom_CV': _('Chức vụ hoặc vị trí công việc'),
        }
        error_messages = {
            'name': {
                'max_length': _("Vượt quá ký tư cho phép rồi"),
            },
        }

        widgets = {

            'Ten_Nhom_CV': forms.TextInput(attrs={'class':'form-control','ROWS':'1'}),

            'muc_ah_cty_11': forms.Select(attrs={'class':'form-select', 'ROWS':'1'}),
            'muc_ah_nv_12': forms.Select(attrs={'class':'form-select'}),
            'ycau_trinhdocm_21': forms.Select(attrs={'class':'form-select'}),
            'ycau_k_nghiem_22': forms.Select(attrs={'class':'form-select'}),
            'ycau_Ngoaingu_23': forms.Select(attrs={'class':'form-select'}),
            'ycau_CNTT_24': forms.Select(attrs={'class':'form-select'}),
            'ycau_kehoach_31': forms.Select(attrs={'class':'form-select'}),
            'ycau_sangtao_32': forms.Select(attrs={'class':'form-select'}),
            'ycau_doclap_33': forms.Select(attrs={'class':'form-select'}),
            'ycau_giaotiep_34': forms.Select(attrs={'class': 'form-select'}),
            'ycau_cuongdo_35': forms.Select(attrs={'class':'form-select'}),
            'mt_laodong_41': forms.Select(attrs={'class':'form-select'}),
            'muc_rui_ro_42': forms.Select(attrs={'class':'form-select'}),
            'mota_Cong_viec': forms.ClearableFileInput(attrs={'multiple': True}),

        }

class motacongviec_Form(forms.ModelForm):
    class Meta:
        model = Mota_Cv
        fields = '__all__'
        help_texts = {
            'Ten_Nhom_CV': _('Chức vụ hoặc vị trí công việc'),
            'don_vi': _('Ghi tên đơn vị quản lý trực tiếp chức danh, công việc '),
            'bo_phan': _('Ghi tên bộ phận quản lý trực tiếp chức danh, công việc '),
            'to_nhom':_('Ghi tên Tổ quản lý trực tiếp chức danh, công việc '),

        }
        labels = {
            'Ten_Nhom_CV': ('Chức vụ:'),'don_vi':('Đơn vị:'),'bo_phan':('Bộ phận:'),'to_nhom': ('Tổ'),  'Mucdich_cv':('Mục đích công việc'),

            'ma_tenvitri': ('Mã vị trí:'),
            'Ten_vitri_full': ('Chức vụ, vị trí đầy đủ'),
            'Ten_theoluong':  ('Tên vị trí theo bảng lương'),
            'ten_nghe_NNDH': ('Nghề công việc NN Độc hại nguy hiểm theo qui định của Nhà nước'),
            'Phan_loai': ('Phân loại'),

            'muc_ah_cty_11':('I.MỨC ĐỘ TÁC ĐỘNG CỦA CÔNG VIỆC: 1.1 Đến kết quả hoạt động kinh doanh'),
            'muc_ah_nv_12':('1.2 Đến công việc của người khác'),


            'ycau_trinhdocm_21':('II.YÊU CẦU VỀ NĂNG LỰC ĐỂ THỰC HIỆN CÔNG VIỆC: 2.1 Đến kết quả hoạt động kinh doanh'),
            'ycau_k_nghiem_22':('2.2 Về kinh nghiệm:'),
            'ycau_Ngoaingu_23':('2.3 Về trình độ Ngoại ngữ'),
            'ycau_CNTT_24':('2.4 Về trình độ CNTT'),
            'ycau_kehoach_31':('III.ĐẶC TÍNH CỦA CÔNG VIỆC: 3.1 Tính kế hoạch'),
            'ycau_sangtao_32':('3.2.Tính ổn định và sáng tạo'),
            'ycau_doclap_33':('3.3. Tính độc lập'),
            'ycau_giaotiep_34': ('3.4 Mức độ phối hợp và kỹ năng giao tiếp'),
            'ycau_cuongdo_35':('3.5 Cường độ lao động'),

            'mt_laodong_41':(' IV. ĐIỀU KIỆN LÀM VIỆC: 4.1.Môi trường làm việc'),
            'muc_rui_ro_42':('4.2 Mức độ rủi ro nghề nghiệp'),

            'Captren': ('Cấp trên:'),
            'diadiem_lv':('Địa điểm làm việc'),
            'Qhe_captren': ('Quan hệ cấp trên'),
            'Qhe_cungcap': ('Quan hệ cùng cấp'),
            'Qhe_capduoi':('Quan hệ cấp dưới'),
            'Qhe_nn_xahoi':('Quan hệ xã hội'),
            'Qhe_khachhang':('Quan hệ khách hàng'),
            'Nh_vu_ket_qua': ('Nhiệm vụ'),

            'Trach_nhiem': ('Trách nhiệm'),

            'Mucdo_anhhuong': ('Mức độ ảnh hưởng'),
            'Ptien_laodong': ('Phương tiện lao động'),
            'Dieu_kienlaodong': ('Điều kiện lao động'),
            'ycau_kynang_khac': ('Kỹ năng khác phục vụ  công việc'),
            'tong_diem': ('Tổng điểm')

}
        widgets = {
            'Ten_Nhom_CV': forms.TextInput(attrs={'placeholder': 'Ghi chức vụ/ vụ trí/chức danh công việc mô tả ','class':'form-select'}),
            'bo_phan': forms.Select(attrs={'placeholder': 'Ghi bộ phân đơn vị trực thuộc công ty, TD, Phòng/NM/XN/TN../TT','class':'form-select'}),
            'to_nhom': forms.Select(attrs={'placeholder': 'Ghi đơn vị trực thuộc bộ phân, ex: xưởng/tổ','class':'form-select'}),


            'ma_tenvitri': forms.TextInput(attrs={'class':'form-control'}),
            'Ten_vitri_full': forms.TextInput(attrs={'class':'form-control'}),
            'Ten_theoluong': forms.TextInput(attrs={'class':'form-control'}),
            'ten_nghe_NNDH': forms.TextInput(attrs={'class':'form-control'}),
            'Phan_loai': forms.Select(attrs={'class':'form-control'}),

            'Captren': forms.TextInput(attrs={'placeholder': 'Ghi tên Vị trí cấp trên quản lý trực tiếp VTCV>','class': 'form-control'}),
            'diadiem_lv': forms.TextInput(attrs={'class':'form-control','placeholder': 'Ghi cụ thể địa chỉ làm việc của Vị trí mô tả',}),
            'Qhe_captren': forms.TextInput(attrs={'class':'form-control-lg', 'placeholder':'Ghi những liên hệ chính với chức danh/đơn vị nào? Để giải quyết vấn đề cụ thể gì?'}),
            'Qhe_cungcap': forms.TextInput(attrs={'class':'form-control-lg','placeholder':'Ghi những liên hệ chính với chức danh/đơn vị nào? Để giải quyết vấn đề cụ thể gì?'}),
            'Qhe_capduoi': forms.TextInput(attrs={'class':'form-control-lg','placeholder':'Ghi những liên hệ chính với chức danh/đơn vị nào? Để giải quyết vấn đề cụ thể gì?'}),
            'Mucdich_cv':forms.Textarea(attrs={'class':'form-control-lg','placeholder':'Nêu mục đích chung mà vị trí này tồn tại để đáp ứng, trả lời cho câu hỏi “vị trí này tồn tại để làm gì cho công ty?". '
                                                                                       'Đây chính là các chức năng chính yếu và kết quả tương ứng của'
                                                                                       ' vị trí này. Mục tiêu phải tương ứng với các chức năng '
                                                                                       'và nhiệm vụ mà vị trí đảm nhận. Nêu tối đa 02 mục tiêu chính '
                                                                                       'yếu cho mỗi vị trí công việc. KHÔNG CHÉP LẠI CÁC CHỨC NĂNG '
                                                                                       'Ở MỤC DƯỚI.Ví dụ, đối với vị trí Trưởng phòng '
                                                                                       'nhân sự có chức năng đề xuất chính sách nhân sự, theo dõi và tư vấn thực hiện chính sách thì mục tiêu '
                                                                                       'có thể là “Bảo đảm chất lượng và số lượng nguồn nhân lực cho công ty thông qua việc thực hiện các chính sách nhân '
                                                                                       'sự phù hợp với nhu cầu quản lý và hiệu quả nhất”'}),
            'Qhe_nn_xahoi': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ghi những liên hệ chính với chức danh/đơn vị nào? Để giải quyết vấn đề cụ thể gì?'}),
            'Qhe_khachhang': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ghi những liên hệ chính với Vị trí/đơn vị nào? Để giải quyết vấn đề cụ thể gì?'}),

            'Nh_vu_ket_qua': forms.Textarea(attrs={'placeholder': 'Ghi đầy đủ, cụ thể và theo trình tự các nội dung công việc của chức danh công việc đang đảm nhận','class': 'form-control account__input-text'}),
            #' 'Nh_vu_ket_qua':forms.CharField(widget=CKEditorUploadingWidget),

            'Trach_nhiem': forms.Textarea(attrs={'placeholder': 'Ghi mức độ trách nhiệm cao nhất đối với kết quả công việc, '
                                                                'Nêu quyền hạn ra quyết định của vị trí liên quan tới sử dụng nhân sự, '
                                                                'thu chi tài chính, quyết định kinh doanh hoặc sản xuất. '
                                                                'KHÔNG LẶP LẠI CÁC NHIỆM VỤ ĐÃ NÊU Ở MỤC TRÊN''- Nhân viên kinh doanh: quyền thương '
                                                                'lượng với khách hàng và quyết định giá trong phạm vi quy định của công ty '
                                                                'và chịu trách nhiệm về hiệu quả kinh doanh'  
                                                                'Kiểm soát chất lượng: quyền dừng sản xuất khi phát hiện lỗi hệ thống trong sản phẩm'
                                                                '- Trưởng phòng HC: quyền đại diện công ty khi làm việc với cơ quan công quyền địa phương và chịu'
                                                                ' trách nhiệm với thông tin cung cấp'
                                                                'tính mạng con người, tài sản và phương tiện làm việc, '
                                                                'Ghi mức độ trách nhiệm cao nhất đối với kết quả công việc, '
                                                                'tính mạng con người, tài sản và phương tiện làm việc','class': 'form-control'}),
            #'Trach_nhiem': forms.CharField(widget=CKEditorUploadingWidget),


            'Mucdo_anhhuong': forms.TextInput(attrs={'class':'form-control','placehoder':'Lựa chọn mức độ ảnh hưởng đến công ty/đơn vị',}),
            'Ptien_laodong': forms.TextInput(attrs={'placeholder': 'Ghi tên máy móc, thiết bị, dụng cụ đo kiểm, đồ nghề chính yếu để thực hiện các nhiệm vụ nêu trên','class':'form-control'}),
            'Dieu_kienlaodong': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ghi loại điều kiện lao động phù hợp với lựa chọn mục 4.1 và 4.2'}),


            'muc_ah_cty_11': forms.Select(attrs={'class':'form-select'}),
            'muc_ah_nv_12': forms.Select(attrs={'class':'form-control-lg'}),

            'ycau_trinhdocm_21': forms.Select(attrs={'class':'form-select'}),
            'ycau_k_nghiem_22': forms.Select(attrs={'class':'form-control'}),
            'ycau_Ngoaingu_23': forms.Select(attrs={'class':'form-control'}),
            'ycau_CNTT_24': forms.Select(attrs={'class':'form-control'}),
            'ycau_kehoach_31': forms.Select(attrs={'class':'form-control'}),
            'ycau_sangtao_32': forms.Select(attrs={'class':'form-control'}),
            'ycau_doclap_33': forms.Select(attrs={'class':'form-control'}),
            'ycau_giaotiep_34': forms.Select(attrs={'class': 'form-control'}),
            'ycau_cuongdo_35': forms.Select(attrs={'class':'form-control'}),

            'mt_laodong_41': forms.Select(attrs={'class':'form-control'}),
            'muc_rui_ro_42': forms.Select(attrs={'class':'form-control'}),
        }

class Choise_DV_Form(forms.ModelForm):
    class Meta:
        model = Mota_Cv
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bo_phan'].queryset = Bo_phan.objects.none()
        self.fields['to_nhom'].queryset = To_nhom.objects.none()
        if 'don_vi' in self.data:
            try:
                don_vi_id = int(self.data.get('don_vi'))
                self.fields['bo_phan'].queryset = Bo_phan.objects.filter(don_vi_id=don_vi_id).order_by('ten_bp')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['bo_phan'].queryset = self.instance.don_vi.bo_phan_set.order_by('ten_bp')
        if 'bo_phan' in self.data:
            try:
                bo_phan_id = int(self.data.get('bo_phan'))
                self.fields['to_nhom'].queryset = To_nhom.objects.filter(bo_phan_id=bo_phan_id).order_by('ten_to')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['to_nhom'].queryset = self.instance.bo_phan.to_nhom_set.order_by('ten_to')