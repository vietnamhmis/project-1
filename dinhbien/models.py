from django.db import models
from nhansu.models import Don_vi,Bo_phan,To_nhom

from django.db.models import Aggregate, Sum

from mota_cv.models import Mota_Cv


class Dinhbien_base(models.Model):
    Tan_xuat = (
         ('Ngày', 'Ngày'),
         ('Tuần', 'Tuần'),
         ('Tháng', 'Tháng'),
         ('Quý', 'Quý'),
         ('6 Tháng', '6 Tháng'),
         ('Năm', 'Năm'),
          )
    donvitinh = (
         ('Ngày', 'Ngày'),
         ('Lần', 'Lần'),
         ('Ca', 'Ca'),
         ('Hồ sơ', 'Hồ sơ'),
             )
    don_vi          = models.ForeignKey(Don_vi, null=True, on_delete= models.SET_NULL)
    bo_phan         = models.ForeignKey(Bo_phan, null=True, on_delete= models.SET_NULL)
    to_nhom         = models.ForeignKey(To_nhom,on_delete=models.CASCADE)

    chuc_vu         = models.ForeignKey(Mota_Cv,on_delete=models.CASCADE)
    donvi_tinh      = models.CharField(max_length=20, blank=False, null=True, choices= donvitinh)
    tan_xuat_lviec  = models.CharField(max_length=20, blank=False, null=True, choices= Tan_xuat)
    class Meta:
        abstract = True


class tonghopdinhbien(Dinhbien_base):
    chucdanh_dinhbien = models.CharField(max_length=90, blank=True, null=True)
    dinhbien_hienco     = models.IntegerField(blank=True, null=True)
    laodong_hc_hienco   = models.IntegerField(blank=True, null=True)
    laodong_ca_hienco   = models.IntegerField(blank=True, null=True)

    Lao_dong_ngoaids    = models.IntegerField(blank=True, null=True)
    laodong_hc_dinhbien = models.IntegerField(blank=True, null=True)
    laodong_ca_dinhbien = models.IntegerField(blank=True, null=True)
    tong_dinhbien       = models.IntegerField(blank=True, null=True)

    chenhlech_dbien     = models.IntegerField(blank=True, null=True)
    Tong_phut_1nam      = models.IntegerField(blank=True, null=True)
    ghichu              = models.CharField(max_length=500, blank=True, null=True)
    def __str__(self):
       return self.chucdanh_dinhbien



class Dinhbien_HC(Dinhbien_base):
    chucdanh        = models.ForeignKey(tonghopdinhbien, null=True, on_delete= models.SET_NULL)
    Noi_dung_cviec  = models.TextField(max_length=1000, blank=False, null=False)
    khoiluong_nam   = models.IntegerField(blank=True, null=True)
    sophut_th_1lan  = models.IntegerField(blank=True, null=True)
    Tong_phut_1nam  = models.IntegerField(blank=True, null=True)
    dinhbienhc      = models.DecimalField('đinhbiênhc', max_digits=5, decimal_places=2,blank=True, null=True)
    Ngaytao         = models.DateTimeField(auto_now_add=True)
    Ngay_update     = models.DateTimeField(auto_now=True)
   

    def __str__(self):
       return str(self.chucdanh)

class Dinhbien_ca(Dinhbien_base):
    chucdanh        = models.ForeignKey(tonghopdinhbien, null=True, on_delete= models.SET_NULL)
    Noi_dung_cviecca  = models.TextField(max_length=1000, blank=False, null=False)
    laodong_ca_1    = models.IntegerField(blank=True, null=True)
    laodong_ca_2    = models.IntegerField(blank=True, null=True)
    laodong_ca_3    = models.IntegerField(blank=True, null=True)

    khoiluongsp_ca_1  = models.IntegerField(editable=False)
    khoiluongsp_ca_2  = models.IntegerField(editable=False)
    khoiluongsp_ca_3  = models.IntegerField(editable=False)

    sophut_th_1lanc  = models.IntegerField(blank=True, null=True)

    Thoigian_yc_ca_1  = models.IntegerField(blank=True, null=True)
    Thoigian_yc_ca_2  = models.IntegerField(blank=True, null=True)
    Thoigian_yc_ca_3  = models.IntegerField(blank=True, null=True)

    Tong_phut_1namc     = models.IntegerField(blank=True, null=True)
    dinhbienca        = models.DecimalField('Định biên ca', max_digits=5, decimal_places=2,blank=True, null=True
                                            )
    def save(self):
        self.khoiluongsp_ca_1 = self.laodong_ca_1 *1
        self.khoiluongsp_ca_2 = self.laodong_ca_2 *1
        self.khoiluongsp_ca_3 = self.laodong_ca_3 *1

        self.Thoigian_yc_ca_1 = self.khoiluongsp_ca_1 * self.sophut_th_1lanc
        self.Thoigian_yc_ca_2 = self.khoiluongsp_ca_2 * self.sophut_th_1lanc
        self.Thoigian_yc_ca_3 = self.khoiluongsp_ca_3 * self.sophut_th_1lanc

        self.Tong_phut_1namc = self.Thoigian_yc_ca_1 + self.Thoigian_yc_ca_2 + self.Thoigian_yc_ca_3
        self.dinhbienca = self.Tong_phut_1namc /60/8*365/231

        return super(Dinhbien_ca, self).save()

    def __str__(self):
            return str(self.chucdanh)

