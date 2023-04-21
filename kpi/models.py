from django.db import models
from django.conf import settings
from mota_cv.models import Mota_Cv
from nhansu.models import Don_vi,Bo_phan,To_nhom
from enroll.models import Nhan_vien
from django.shortcuts import reverse

#m J_query

#----------https://www.youtube.com/watch?v=Qc5NnpxFbBo&t=4s-






#-------------------------------------------end--

class Product(models.Model):
    FILLOW = 1
    FOOD = 2
    TOYS = 3
    PRODUCT_TYPES = (
        (FILLOW, 'Pillow'),
        (FOOD, 'Food'),
        (TOYS, 'Toys'),
    )
    name            = models.CharField(max_length=50)
    dateadded       = models.DateField(blank=True, null=True)
    productcode     = models.CharField(max_length=30, blank=True)
    price           = models.DecimalField(max_digits=5, decimal_places=2)
    quantity        = models.IntegerField(blank=True, null=True)
    category_type   = models.PositiveSmallIntegerField(choices=PRODUCT_TYPES, blank=True, null=True)

    class Meta:
        db_table = "myapp_product"




#Thu7 ----Jquery
class Task(models.Model):
    owner = models.CharField(max_length = 150)
    name = models.CharField(max_length = 150)
    task_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#Thư fiter

class Author(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Journal(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    categories = models.ManyToManyField(Category)
    publish_date = models.DateTimeField()

    views = models.IntegerField(default=0)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
# Finnish thử fiter

class Don_vi_tinh(models.Model):
    Don_vi_tinh     = models.TextField(max_length=15, blank=False, null=False)
    def __str__(self):
        return self.Don_vi_tinh



class Dmkpi_dv(models.Model):
    class Meta:
        ordering =["-id", "Ten_KPI"]

    Viencanh = (
         ('tc', 'VC Tài chính'),
         ('kh', 'VC Khách hàng'),
         ('nb', 'VC Quy trình nội bộ'),
         ('hh', 'VC Học hỏi, phát triển'),
          )
    Tan_xuat = (
         ('th', 'Tháng'),
         ('qu', 'Quý'),
         ('na', 'Năm'),
         )
    donvitinh = (
         ('dg', 'Tỷ đồng'),
         ('kwx', 'kwh/tấn xi măng'),
         ('kwc', 'kcal/kg clanhke'),
         ('kwx', 'tr.đồng/người'),
         ('kwx', 'Tấn'),
         ('kwx', 'ngày'),
         ('kg', 'kg'),
         ('sk', 'sk'),
         ('%', '%'),
          )

    Ma_KPo          = models.TextField(max_length=10, blank=True, null=True)
    Ten_KPo         = models.TextField(max_length=255, blank=False, null=False)
    Ten_KPI         = models.TextField(max_length=305, blank=False, null=False)
    Don_vi_tinh     = models.CharField(max_length=20, blank=False, null=True, choices= donvitinh)
    Chitieu_KPI     = models.IntegerField(blank=True)
    Ti_trong        = models.DecimalField(max_digits=5, decimal_places=1, blank=True)
    Cap_KPI         = models.IntegerField(blank=True, null=True)
    Vien_canh_cluoc = models.CharField(max_length=20, blank=False, null=True, choices= Viencanh)
    Tan_xuat_d_gia  = models.CharField(max_length=20, blank=False, null=True, choices= Tan_xuat)
    Dv_quanly_KPI   = models.ForeignKey(Don_vi, null=True, on_delete= models.SET_NULL)
    Ngay_update     = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.Ten_KPo


class dmkpi(models.Model):
    class Meta:
        ordering =["-id", "LoaiCV"]

    Tan_xuat = (
         ('th', 'Tháng'),
         ('qu', 'Quý'),
         ('na', 'Năm'),
          )
    donvitinh = (
         ('dg', 'Tỷ đồng'),
         ('kwx', 'kwh/tấn xi măng'),
         ('kwc', 'kcal/kg clanhke'),
         ('kwx', 'tr.đồng/người'),
         ('kwx', 'Tấn'),
         ('kwx', 'ngày'),
         ('kg', 'kg'),
         ('sk', 'sk'),
         ('%', '%'),
          )
    Ten_KPI         = models.CharField(max_length=500, blank=True, null=False)
    LoaiCV          = models.ForeignKey(Mota_Cv, null=True, on_delete= models.SET_NULL)
    Don_vi_tinh     = models.CharField(default="%",max_length=20, blank=False, null=True, choices= donvitinh)
    Tan_xuat_d_gia  = models.CharField(default="Tháng",max_length=20, blank=False, null=True, choices= Tan_xuat)
    Ti_trong        = models.DecimalField(max_digits=5, decimal_places=1)
    Ngaytao         = models.DateTimeField(auto_now_add=True)
    Ngay_update     = models.DateTimeField(auto_now=True)
    def __str__(self):
      return self.Ten_KPI


class List_kpi(models.Model):
    class Meta:
        ordering =["-id", "LoaiCV"]
    Tan_xuat = (
         ('th', 'Tháng'),
         ('qu', 'Quý'),
         ('na', 'Năm'),
          )
    donvitinh = (
         ('dg', 'Tỷ đồng'),
         ('kwx', 'kwh/tấn xi măng'),
         ('kwc', 'kcal/kg clanhke'),
         ('kwx', 'tr.đồng/người'),
         ('kwx', 'Tấn'),
         ('kwx', 'ngày'),
         ('kg', 'kg'),
         ('sk', 'sk'),
         ('%', '%'),
          )

    LoaiCV          = models.ForeignKey(Mota_Cv, null=True, on_delete= models.SET_NULL)
    Don_vi_tinh     = models.CharField(default="%",max_length=20, blank=False, null=True, choices= donvitinh)
    Tan_xuat_d_gia  = models.CharField(default="Tháng",max_length=20, blank=False, null=True, choices= Tan_xuat)
    Ti_trong        = models.DecimalField(max_digits=5, decimal_places=1)
    Ngaytao         = models.DateTimeField(auto_now_add=True)
    Ngay_update     = models.DateTimeField(auto_now=True)
    slug = models.SlugField()


class Phan_KPI(models.Model):
    Viencanh = (
         ('tc', 'VC Tài chính'),
         ('kh', 'VC Khách hàng'),
         ('nb', 'VC Quy trình nội bộ'),
         ('hh', 'VC Học hỏi, phát triển'),
          )
    Tan_xuat = (
         ('th', 'Tháng'),
         ('qu', 'Quý'),
         ('na', 'Năm')
          )
    Diem_manh     = models.TextField(max_length=10, blank=True, null=True)
    Nguoigiao       = models.CharField(max_length=5, blank=True, null=True)
    Nguoi_nhan      = models.ForeignKey(Nhan_vien, null=True, on_delete=models.SET_NULL)
    Ten_KPI         = models.ForeignKey(dmkpi, null=True, on_delete=models.SET_NULL)
    Ti_trong        = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    Chitieu         = models.IntegerField(blank=True, null=True)
    Ketqua_cn       = models.IntegerField(blank=True, null=True)
    ketqua_dv       = models.IntegerField(blank=True, null=True)
    ketqua_cuoi     = models.IntegerField(blank=True, null=True)
    ti_le_ht        = models.IntegerField(blank=True, null=True)
    diem_CV         = models.IntegerField(blank=True, null=True)
    diemtrongso     = models.IntegerField(blank=True, null=True)
    DVi_giao        = models.ForeignKey(Bo_phan, null=True, on_delete= models.SET_NULL)
    DVi_nhan        = models.ForeignKey(To_nhom,on_delete=models.CASCADE)
    Cap_KPI         = models.IntegerField(blank=True, null=True)
    Cviec_phan_KPI  = models.ForeignKey(Mota_Cv, null=True, on_delete= models.SET_NULL)
    Dv_quanly_KPI   = models.TextField(max_length=10, blank=False, null=False)
    KPI_cha         = models.IntegerField(blank=True)
    Vien_canh_cluoc = models.CharField(max_length=20, blank=False, null=True, choices= Viencanh)
    Mtieu_cluoc     = models.TextField(max_length=55, blank=True, null=True)
    Tan_xuat_d_gia  = models.CharField(max_length=20, blank=False, null=True, choices= Tan_xuat)
    Chi_tieu_c_bo   = models.TextField(max_length=5, blank=True, null=True)

    Don_vi_nhan_c_bo = models.TextField(max_length=5, blank=True, null=True)
    Don_vi_tinh     = models.ForeignKey(Don_vi_tinh, null=True, on_delete= models.SET_NULL)



class giao_KPI(models.Model):
    Viencanh = (
         ('tc', 'VC Tài chính'),
         ('kh', 'VC Khách hàng'),
         ('nb', 'VC Quy trình nội bộ'),
         ('hh', 'VC Học hỏi, phát triển'),
          )
    Tan_xuat = (
         ('th', 'Tháng'),
         ('qu', 'Quý'),
         ('na', 'Năm'),
          )
    Ky_giao_KPI     = models.TextField(max_length=10, blank=True, null=True)
    Nguoigiao       = models.CharField(max_length=5, blank=True, null=True)
    Nguoi_nhan      = models.ForeignKey(Nhan_vien, null=True, on_delete=models.SET_NULL)
    Ten_KPI         = models.ForeignKey(dmkpi, null=True, on_delete=models.SET_NULL)
    Ti_trong        = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    Chitieu         = models.IntegerField(blank=True, null=True)
    Ketqua_cn       = models.IntegerField(blank=True, null=True)
    ketqua_dv       = models.IntegerField(blank=True, null=True)
    ketqua_cuoi     = models.IntegerField(blank=True, null=True)
    ti_le_ht        = models.IntegerField(blank=True, null=True)
    diem_CV         = models.IntegerField(blank=True, null=True)
    diemtrongso     = models.IntegerField(blank=True, null=True)
    DVi_giao        = models.ForeignKey(Bo_phan, null=True, on_delete= models.SET_NULL)
    DVi_nhan        = models.ForeignKey(To_nhom,on_delete=models.CASCADE)
    Cap_KPI         = models.IntegerField(blank=True, null=True)
    Cviec_phan_KPI  = models.ForeignKey(Mota_Cv, null=True, on_delete= models.SET_NULL)
    Dv_quanly_KPI   = models.TextField(max_length=10, blank=False, null=False)
    KPI_cha         = models.IntegerField(blank=True)
    Vien_canh_cluoc = models.CharField(max_length=20, blank=False, null=True, choices= Viencanh)
    Mtieu_cluoc     = models.TextField(max_length=55, blank=True, null=True)
    Tan_xuat_d_gia  = models.CharField(max_length=20, blank=False, null=True, choices= Tan_xuat)
    Chi_tieu_c_bo   = models.TextField(max_length=5, blank=True, null=True)

    Don_vi_nhan_c_bo = models.TextField(max_length=5, blank=True, null=True)
    Don_vi_tinh     = models.ForeignKey(Don_vi_tinh, null=True, on_delete= models.SET_NULL)
#------------------------------------------------------------------------------


