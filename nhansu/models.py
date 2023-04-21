from django.contrib.auth.decorators import login_required
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
#from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.
#----------

class trinh_do_qlnn(models.Model):
    #MA_TRINH_DO_qlnn = models.CharField(max_length=20, blank=False, null=True)
    TEN_TRINH_DO = models.CharField(max_length=50, blank=False, null=True)
    def __str__(self):
        return self.TEN_TRINH_DO

class trinh_do_ct(models.Model):
    #MA_TRINH_DO_ct = models.CharField(max_length=20, blank=False, null=True)
    TEN_TRINH_DO = models.CharField(max_length=50, blank=False, null=True)
    def __str__(self):
        return self.TEN_TRINH_DO

class Trinhdovh(models.Model):
   # MA_TRINH_DO_VAN_HOA = models.CharField(max_length=20, blank=False, null=True)
    TEN_TRINH_DO = models.CharField(max_length=50, blank=False, null=True)
    def __str__(self):
        return self.TEN_TRINH_DO

class Trinhdo(models.Model):
    #MA_TRINH_DO_CM = models.CharField(max_length=50, blank=False, null=True)
    TEN_TRINH_DO = models.CharField(max_length=50, blank=False, null=True)
    def __str__(self):
        return self.TEN_TRINH_DO

class Thanhphan_gd(models.Model):
   # MATP = models.CharField(max_length=50, blank=False, null=True)
    THANH_PHAN = models.CharField(max_length=50, blank=False, null=True)
    def __str__(self):
        return self.THANH_PHAN

class Ton_giao(models.Model):
    #MA_TON_GIAO = models.CharField(max_length=5, blank=False, null=True)
    TEN_TON_GIAO = models.CharField(max_length=50, blank=False, null=True, default="Không" )
    def __str__(self):
        return self.TEN_TON_GIAO
class Tinh_que(models.Model):
    Ma_tinh =  models.CharField(max_length=2, blank=True, null=True)
    TEN_TINH    = models.CharField(max_length=25, blank=True, null=True)
    def __str__(self):
        return self.TEN_TINH

class Tinh_sinh(models.Model):
    Ma_tinh =  models.CharField(max_length=2, blank=True, null=True)
    TEN_TINH = models.CharField(max_length=25, blank=True, null=True)
    def __str__(self):
        return self.TEN_TINH

class Tinh(models.Model):
    Ma_tinh =  models.CharField(max_length=2, blank=True, null=True)
    TEN_TINH = models.CharField(max_length=25, blank=True, null=True)
    def __str__(self):
        return self.TEN_TINH
class Quan_huyen(models.Model):
    ma_huyen     =models.CharField(max_length=2, blank=True, null=True)
    Tinh_thanh   =    models.ForeignKey(Tinh, on_delete=models.CASCADE)
    Ten_quan     = models.CharField(max_length=30, blank=True, null=True)
    def __str__(self):
        return self.Ten_quan
class Phuong_xa(models.Model):
    ma_xa     =models.CharField(max_length=5, blank=True, null=True)
    Quan_huyen  =    models.ForeignKey(Quan_huyen, on_delete=models.CASCADE, blank=True, null=True)
    Tinh_thanh   =   models.ForeignKey(Tinh, on_delete=models.CASCADE, blank=True, null=True)
    Ten_xa      = models.CharField(max_length=30, blank=False, null=True)
    def __str__(self):
        return self.Ten_xa

class Tinh_HK(models.Model):
    Ma_tinh =  models.CharField(max_length=2, blank=True, null=True)
    TEN_TINH = models.CharField(max_length=25, blank=True, null=True)
    def __str__(self):
        return self.TEN_TINH

class Quan_huyen_HK(models.Model):
    ma_huyen     =models.CharField(max_length=2, blank=True, null=True)
    Tinh_thanh   =    models.ForeignKey(Tinh, on_delete=models.CASCADE)
    Ten_quan     = models.CharField(max_length=30, blank=True, null=True)
    def __str__(self):
        return self.Ten_quan

class Phuong_xa_HK(models.Model):
    ma_xa     =models.CharField(max_length=5, blank=True, null=True)
    Quan_huyen  =    models.ForeignKey(Quan_huyen, on_delete=models.CASCADE, blank=True, null=True)
    Tinh_thanh   =   models.ForeignKey(Tinh, on_delete=models.CASCADE, blank=True, null=True)
    Ten_xa      = models.CharField(max_length=30, blank=False, null=True)
    def __str__(self):
        return self.Ten_xa

class Dan_toc(models.Model):
    MA_DAN_TOC = models.CharField(max_length=5, blank=False, null=True)
    TEN_DAN_TOC = models.CharField(max_length=50, blank=False, null=True)
    def __str__(self):
        return self.TEN_DAN_TOC


class Quocgia(models.Model):
    MA_QUOC_GIA_NGUON_GOC = models.CharField(max_length=5, blank=False, null=True)
    TEN_QUOC_GIA = models.CharField(max_length=50, blank=False, null=True)
    def __str__(self):
        return self.TEN_QUOC_GIA

class Don_vi(models.Model):
    objects = None
    Khoi_SXKD = (
			('sx', 'Sản xuất' ),
			('vp', 'Văn phòng'),
            ('kd', 'Kinh doanh'),
            ('BT', 'QLDA-BOT'),
			)

    ma_DV       = models.CharField(max_length=7, blank=True, null=True)
    Ten_DV      = models.CharField(max_length=50, blank=True, null=True)
    diachi      = models.CharField(max_length=100, blank=True, null=True)
    khoi_SXKD   = models.CharField(max_length=10, blank=True, null=True, choices=Khoi_SXKD)
    nv_dv       = models.FileField(upload_to='CNNV_dv', blank=True, null=True)
    so_nhanvien = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.Ten_DV


class Bo_phan(models.Model):
    ma_bp       = models.CharField(max_length=7, blank=False, null=True)
    ten_bp      = models.CharField(max_length=50, blank=True, null=True)
    don_vi      = models.ForeignKey(Don_vi,on_delete=models.CASCADE, blank=True)
    nv_bp       = models.FileField(upload_to='CNNV_bp', null=True, blank=True)
    def __str__(self):
        return self.ten_bp

class To_nhom(models.Model):
    ma_to       = models.CharField(max_length=7, blank=True, null=False)
    ten_to      = models.CharField(max_length=50, blank=True, null=False)
   # don_vi = models.ForeignKey(Don_vi, on_delete=models.CASCADE, blank=True, null=False)
    bo_phan     = models.ForeignKey(Bo_phan, on_delete=models.CASCADE, blank=True, null=False)
    nv_tn       = models.FileField(upload_to='CNNV_tn', blank=True)
    def __str__(self):
        return self.ten_to

class Ten_ngheDH(models.Model):
    ma_nghe         = models.CharField(max_length=15)
    name            = models.CharField(max_length=155)
    dacdiem_nghe    = models.CharField(max_length=155)
    loai_dh         = models.CharField(max_length=155)
    vanban_qd      = models.CharField(max_length=155)
    def __str__(self):
        return self.name
    class meta:
        db_table ="ten_nghe_doc_hai"

class coso_KCB(models.Model):
    ma_ckcb        = models.CharField(max_length=5, blank=True, null=True)
    ten_benhvien   = models.CharField(max_length=90, blank=True, null=True)
    dangki_KCB      = models.CharField(max_length=130, blank=True, null=True)
    Ghichu         = models.CharField(max_length=150, blank=True, null=True)
    def __str__(self):
        return self.ten_benhvien


class Loai_laodong(models.Model):
    ma_loai_laodong = models.CharField(max_length=6, null=False, blank=False)
    name        = models.CharField(max_length=170, null=False, blank=False)

    def __str__(self):
       return self.name
#------------------Tiêu chuẩn định giá 4 yếu tố---------------------
class Muc_ah_cty_11(models.Model):
    name        = models.CharField(max_length=175, null=False, blank=False)
    titrong     = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)
    def __str__(self):
       return self.name

class Muc_ah_nv_12(models.Model):
    name        = models.CharField(max_length=270, null=False, blank=False)
    titrong     = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)
    def __str__(self):
       return self.name

class Ycau_trinhdocm_21(models.Model):
    name        = models.CharField(max_length=270, null=False, blank=False)
    titrong     = models.IntegerField(null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)
    def __str__(self):
       return self.name

class Ycau_k_nghiem_22(models.Model):
    name        = models.CharField(max_length=270, null=False, blank=False)
    titrong     = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)
    def __str__(self):
       return self.name

class Ycau_Ngoaingu_23(models.Model):
    name        = models.CharField(max_length=170, null=False, blank=False)
    titrong     = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)
    def __str__(self):
       return self.name

class Ycau_CNTT_24(models.Model):
    name        = models.CharField(max_length=270, null=False, blank=False)
    titrong     = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)
    def __str__(self):
       return self.name

class Ycau_kehoach_31(models.Model):
    name        = models.CharField(max_length=270, null=False, blank=False)
    titrong     = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)
    def __str__(self):
       return self.name

class Ycau_sangtao_32(models.Model):
    name        = models.CharField(max_length=270, null=False, blank=False)
    titrong     = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)
    def __str__(self):
       return self.name

class Ycau_doclap_33(models.Model):
    name        = models.CharField(max_length=270, null=False, blank=False)
    titrong     = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)
    def __str__(self):
       return self.name

class Ycau_cuongdo_35(models.Model):
    name        = models.CharField(max_length=270, null=False, blank=False)
    titrong     = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)
    def __str__(self):
       return self.name
class Ycau_giaotiep_34(models.Model):
    name        = models.CharField(max_length=270, null=False, blank=False)
    titrong     = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)
    def __str__(self):
       return self.name

class Mt_laodong_41(models.Model):
    name        = models.CharField(max_length=270, null=False, blank=False)
    titrong     = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)
    def __str__(self):
       return self.name

class Muc_rui_ro_42(models.Model):
    name        = models.CharField(max_length=270, null=False, blank=False)
    titrong     = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)
    def __str__(self):
       return self.name

#------------------Finnish_Tiêu chuẩn định giá 4 yếu tố---------------------

#------------------Tiêu chuẩn định giá 7yếu tố---------------------
class Yeu_to_1_trinh_do(models.Model):
    name        = models.CharField(max_length=270, null=False, blank=False)
    titrong     = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)
    def __str__(self):
       return self.name

class Yeu_to_2_Ky_nang(models.Model):
    name        = models.CharField(max_length=270, null=False, blank=False)
    titrong     = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)
    def __str__(self):
       return self.name
class Yeu_to_3_Trach_nhiem(models.Model):
    name        = models.CharField(max_length=270, null=False, blank=False)
    titrong     = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)
    def __str__(self):
       return self.name

class Yeu_to_4_Anh_huong(models.Model):
    name        = models.CharField(max_length=270, null=False, blank=False)
    titrong     = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)
    def __str__(self):
       return self.name

class Yeu_to_5_Sangtao(models.Model):
    name        = models.CharField(max_length=270, null=False, blank=False)
    titrong     = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)
    def __str__(self):
       return self.name

class Yeu_to_6_Giaotiep(models.Model):
    name        = models.CharField(max_length=270, null=False, blank=False)
    titrong     = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)
    def __str__(self):
       return self.name

class Yeu_to_7_DK_lamviec(models.Model):
    name        = models.CharField(max_length=270, null=False, blank=False)
    titrong     = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)


    def __str__(self):
       return self.name

class Yeu_to_khac(models.Model):
    name        = models.CharField(max_length=470, null=False, blank=False)
    titrong     = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)

    def __str__(self):
       return self.name

class TK_ngach(models.Model):
    nhom        = models.IntegerField(null=True, blank=True)
    diem        = models.IntegerField(null=True, blank=True)
    heso_gian   = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    lan_gian    = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    di_tk       = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    bac_1       = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    bac_2       = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    bac_3       = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    bac_4       = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    bac_5       = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)

    heso_gian_BHXH   = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    lan_gian_BHXH    = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    di_tk_BHXH       = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    bac_1_BHXH       = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    bac_2_BHXH       = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    bac_3_BHXH       = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    bac_4_BHXH       = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    bac_5_BHXH       = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)

    def __str__(self):
       return str(self.nhom)



#------------------Finnish_Tiêu chuẩn định giá 7 yếu tố---------------------



class Product(models.Model):
    category = models.CharField(max_length=100, null=False, blank=False)
    num_of_products = models.IntegerField()

    Ten_DV      = models.CharField(max_length=50, blank=True, null=True)
    diachi      = models.CharField(max_length=100, blank=True, null=True)

    nv_dv       = models.FileField(upload_to='CNNV_dv')
    so_nhanvien = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return f'{self.category} - {self.num_of_products}'



class Tochuc_Sudung_KPI_NL(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
       return self.name

class Ho_congviec(models.Model):
    ma_ho_cv = models.CharField(max_length=10, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
       return self.name

class Loai_nangluc(models.Model): # Năng lực chung, Quản lý, Chuyên môn:
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
       return self.name


class Nang_luc_2(models.Model):
    class Meta:
       # unique_together = ('ma_nangluc') #
        # Đổi tên table db_table = 'khung_nangluc
        ordering= ['loai_nang_luc', 'ma_nangluc']
    LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),
    ('I', 'info'),
    ('W', 'warning'),
    ('S', 'success'),
    ('g', 'good')
)
    name            = models.CharField(max_length=70, null=True, blank=True)
    ma_nangluc      = models.CharField( max_length=4, null= True, blank=True)
    image           = models.ImageField(null= True, blank=True)
    MoTa_nangluc    = models.CharField(max_length=4000, null=False, blank=False)
    NL_muc_1         = models.CharField(max_length=4000, null=False, blank=False)
    NL_muc_2         = models.CharField(max_length=8000, null=False, blank=False)
    NL_muc_3         = models.CharField(max_length=10000, null=False, blank=False)
    NL_muc_4         = models.CharField(max_length=10000, null=False, blank=False)
    NL_muc_5         = models.CharField(max_length=10000, null=False, blank=False)
    ngay_tao         = models.DateField(blank=True,null=True)
    slug            = models.SlugField(null=True, blank=True)
    label           = models.CharField(choices=LABEL_CHOICES, max_length=1,null=True, blank=True)
    loai_nang_luc   = models.ForeignKey(Loai_nangluc, on_delete=models.SET_NULL, null=True, blank=True)
    su_dung         = models.BooleanField(default=False)
    tochuc_Sudung   = models.ForeignKey(Tochuc_Sudung_KPI_NL,on_delete=models.SET_NULL, null=True, blank=True)
    ho_congviec   = models.ForeignKey(Ho_congviec,on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
       return self.name

#----------------------------
class Loai_vanban(models.Model): # Năng lực chung, Quản lý, Chuyên môn:
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
       return self.name

class Vanban(models.Model):
    class Meta:
       # unique_together = ('ma_nangluc') #
        # Đổi tên table db_table = 'khung_nangluc
        ordering= ['id','loai_vanban', 'name']
    LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),
    ('I', 'info'),
    ('W', 'warning'),
    ('S', 'success'),
    ('g', 'good')
)

    name           = models.CharField(max_length=70, null=True, blank=True)
    ma_vanban      = models.CharField( max_length=4, null= True, blank=True)
    image          = models.ImageField(null= True, blank=True)
    file_name      = models.FileField(null= True, blank=True)
    MoTa_vanban    = models.CharField(max_length=4000, null=False, blank=False)

    ngay_tao         = models.DateField(blank=True,null=True)
    slug            = models.SlugField(null=True, blank=True)
    label           = models.CharField(choices=LABEL_CHOICES, max_length=1,null=True, blank=True)
    loai_vanban     = models.ForeignKey(Loai_vanban, on_delete=models.SET_NULL, null=True, blank=True)
    su_dung         = models.BooleanField(default=False)
    tochuc_Sudung   = models.ForeignKey(Tochuc_Sudung_KPI_NL,on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
       return self.name


#------------------------------------------------KPI:
class Loai_kpi(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
       return self.name

class Donvi_tinh(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    def __str__(self):
       return self.name

class Tieuchuan_KPI(models.Model):
    name        = models.CharField(max_length=20, null=False, blank=False)
    Gioihanduoi = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    Diem_chitieu_tang = models.IntegerField()
    Diem_chitieu_giam = models.IntegerField()
    def __str__(self):
       return self.name

class Nhom_KPI(models.Model):
    name        = models.CharField(max_length=90, null=False, blank=False)
    def __str__(self):
       return self.name


class KPI_list(models.Model):
    class Meta:
        ordering= ['loai_kpi', 'ma_kpi']
    LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),
    ('I', 'info'),
    ('W', 'warning'),
    ('S', 'success'),
    ('G', 'good')
)
    Tan_xuat = (
         ('Tháng', 'Tháng'),
         ('Quý', 'Quý'),
         ('Quý', 'Năm'),
          )

    name            = models.CharField(max_length=400, null=True, blank=True)
    kpo             = models.CharField(max_length=100, null=True, blank=True)
    ma_kpi          = models.CharField( max_length=4, null= True, blank=True)
    moTa_kpi        = models.CharField(max_length=1000, null=True, blank=False)
    tan_xuat_d_gia  = models.CharField(default="Tháng",max_length=20, blank=True, null=True, choices= Tan_xuat)
    chi_tieu        = models.DecimalField(max_digits=7, decimal_places=1)
    donvi_tinh      = models.ForeignKey(Donvi_tinh, on_delete=models.CASCADE, null=True, blank=True)
    ngaytao         = models.DateField(auto_now_add=True)
    ngay_update     = models.DateField(auto_now=True)

    slug             = models.SlugField(null=True, blank=True)
    label            = models.CharField(choices=LABEL_CHOICES, max_length=1,null=True, blank=True)
    loai_kpi        = models.ForeignKey(Loai_kpi, on_delete=models.SET_NULL, null=True, blank=True)
    tochuc_Sudung   = models.ForeignKey(Tochuc_Sudung_KPI_NL,on_delete=models.SET_NULL, null=True, blank=True)
    Su_dung         = models.BooleanField(default=False)
    ho_congviec     = models.ForeignKey(Ho_congviec,on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
       return self.name
