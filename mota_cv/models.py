from django.db import models
from ckeditor.fields import RichTextField
from nhansu.models import Don_vi,Bo_phan, To_nhom
from nhansu.models import Muc_ah_cty_11, Muc_ah_nv_12,Ycau_trinhdocm_21, Ycau_k_nghiem_22, Ycau_Ngoaingu_23, Ycau_CNTT_24
from nhansu.models import Ycau_kehoach_31, Ycau_sangtao_32, Ycau_doclap_33, Ycau_giaotiep_34, Ycau_cuongdo_35
from nhansu.models import Mt_laodong_41, Muc_rui_ro_42, Loai_laodong
from nhansu.models import Yeu_to_1_trinh_do,Yeu_to_2_Ky_nang, Yeu_to_3_Trach_nhiem, Yeu_to_4_Anh_huong,Yeu_to_5_Sangtao, Yeu_to_6_Giaotiep, Yeu_to_7_DK_lamviec, Ten_ngheDH
# Create your models here.
from nhansu.models import Yeu_to_khac



class Mota_Cv(models.Model):
    loai = (
         ('CN', 'Công nhân'),
         ('NV', 'Nhân viên'),
         ('QLCT','Quản lý Công ty'),
         ('QLĐV', 'Quản lý đơn vị'),
         ('QLBP', 'Quản lý bộ phận'),
         ('QLT01', 'Quản lý Tổ 1'),
         ('QLT01.', 'Quản lý Tổ 3'),
         ('QLT02', 'Quản lý Tổ 2'),
         ('QL', 'Quản lý 3'),
         ('SPEC', 'Khác'),
     )
    class Meta:
        ordering =["Ten_Nhom_CV"]

    Ten_Nhom_CV     = models.TextField(max_length=115, blank=True, null=True)
    don_vi          = models.ForeignKey(Don_vi, null=True, on_delete= models.SET_NULL)
    bo_phan         = models.ForeignKey(Bo_phan, null=True, on_delete= models.SET_NULL)
    to_nhom         = models.ForeignKey(To_nhom,blank=True, null=True, on_delete=models.CASCADE)

    ma_tenvitri     = models.TextField(max_length=10, blank=True, null=True)
    Ten_vitri_full  = models.TextField(max_length=110, blank=True, null=True)
    Ten_theoluong   = models.TextField(max_length=100, blank=True, null=True)
    ten_nghe_NNDH   = models.TextField(max_length=100, blank=True, null=True)
    Phan_loai       = models.CharField(default="%",max_length=20, blank=False, null=True, choices= loai)
    mota_Cong_viec  = models.FileField(upload_to='mota_CV_2022', blank=True, null=True)


    Captren         =models.CharField(max_length=300,null=True, blank=True)
    diadiem_lv      =models.CharField(max_length=300,null=True, blank=True)
    Mucdich_cv      =models.CharField(max_length=900,null=True, blank=True)
    Qhe_captren     =models.CharField(max_length=500,null=True, blank=True)
    Qhe_cungcap     =models.CharField(max_length=500,null=True, blank=True)
    Qhe_capduoi     =models.CharField(max_length=500,null=True, blank=True)
    Qhe_nn_xahoi    =models.CharField(max_length=500,null=True, blank=True)
    Qhe_khachhang   =models.CharField(max_length=500,null=True, blank=True)
   # Nh_vu_ket_qua   =models.CharField(max_length=500,null=True, blank=True)
    Nh_vu_ket_qua   = RichTextField()

    #Trach_nhiem     = RichTextField()
    Trach_nhiem     =models.CharField(max_length=1000000,null=True, blank=True)
    Mucdo_anhhuong  =models.CharField(max_length=300,null=True, blank=True)
    Ptien_laodong   =models.CharField(max_length=300,null=True, blank=True)
    Dieu_kienlaodong=models.CharField(max_length=300,null=True, blank=True, default='Máy móc, thiết bị, phương tiện để đảm bảo hoàn thành nhiệm vụ được theo theo qui định của Công ty')
#__________________________Đinh giá 4 yêu tố
    muc_ah_cty_11       = models.ForeignKey(Muc_ah_cty_11, null=True, on_delete= models.SET_NULL)
    muc_ah_nv_12        = models.ForeignKey(Muc_ah_nv_12, null=True, on_delete= models.SET_NULL)
    ycau_trinhdocm_21   = models.ForeignKey(Ycau_trinhdocm_21, null=True, on_delete= models.SET_NULL)
    ycau_k_nghiem_22    = models.ForeignKey(Ycau_k_nghiem_22, null=True, on_delete= models.SET_NULL)
    ycau_Ngoaingu_23    = models.ForeignKey(Ycau_Ngoaingu_23, null=True, on_delete= models.SET_NULL)
    ycau_CNTT_24        = models.ForeignKey(Ycau_CNTT_24, null=True, on_delete= models.SET_NULL)
    ycau_kehoach_31     = models.ForeignKey(Ycau_kehoach_31, null=True, on_delete= models.SET_NULL)
    ycau_sangtao_32     = models.ForeignKey(Ycau_sangtao_32, null=True, on_delete= models.SET_NULL)
    ycau_doclap_33      = models.ForeignKey(Ycau_doclap_33, null=True, on_delete= models.SET_NULL)
    ycau_giaotiep_34    = models.ForeignKey(Ycau_giaotiep_34, null=True, on_delete= models.SET_NULL)
    ycau_cuongdo_35     = models.ForeignKey(Ycau_cuongdo_35, null=True, on_delete= models.SET_NULL)
    mt_laodong_41      = models.ForeignKey(Mt_laodong_41, null=True, on_delete= models.SET_NULL)
    muc_rui_ro_42       = models.ForeignKey(Muc_rui_ro_42, null=True, on_delete= models.SET_NULL)
    #------------------------
    #------------------------
    ycau_kynang_khac    = models.CharField(max_length=300,null=True, blank=True)
    tong_diem           = models.IntegerField()

    #__________________________
    def save(self):
        self.tong_diem = self.muc_ah_cty_11.diem + self.muc_ah_nv_12.diem + self.ycau_trinhdocm_21.diem + self.ycau_k_nghiem_22.diem + self.ycau_Ngoaingu_23.diem + self.ycau_CNTT_24.diem +  self.ycau_kehoach_31.diem + self.ycau_sangtao_32.diem + self.ycau_doclap_33.diem + self.ycau_giaotiep_34.diem +self.ycau_cuongdo_35.diem +self.mt_laodong_41.diem + self.muc_rui_ro_42.diem
        return super(Mota_Cv, self).save()
    def __str__(self):
        return self.Ten_Nhom_CV

class Chuc_danh(models.Model):
    Ten             = models.TextField(max_length=115, blank=True, null=True)
    Chuc_trach      = models.TextField(max_length=10000, blank=True, null=True)
    TC_daotao       = models.TextField(max_length=7000, blank=True, null=True)
    TC_kthuc_kn     = models.TextField(max_length=7000, blank=True, null=True)
    TC_khac         = models.TextField(max_length=10000, blank=True, null=True)
    def __str__(self):
        return self.Ten

class Mota_Cv_base(models.Model):
    class Meta:
        ordering =["Ten_Nhom_CV"]
    class Meta:
       abstract = True

    Ten_Nhom_CV     = models.TextField(max_length=115, blank=True, null=True)
    don_vi          = models.ForeignKey(Don_vi, null=True, on_delete= models.SET_NULL)
    bo_phan         = models.ForeignKey(Bo_phan, null=True, on_delete= models.SET_NULL)
    to_nhom         = models.ForeignKey(To_nhom,blank=True, null=True, on_delete=models.CASCADE)
    chuc_danh       = models.ForeignKey(Chuc_danh,blank=True, null=True, on_delete=models.CASCADE)

    ma_tenvitri     = models.TextField(max_length=10, blank=True, null=True)
    Ten_vitri_full  = models.TextField(max_length=110, blank=True, null=True)
    Ten_theoluong   = models.TextField(max_length=100, blank=True, null=True)
    Loai_laodong    = models.ForeignKey(Loai_laodong, blank=True, null=True, on_delete=models.CASCADE)

    mota_Cong_viec  = models.FileField(upload_to='mota_CV_2022', blank=True, null=True)
    Captren         =models.CharField(max_length=200,null=True, blank=True)
    Donvi_Captren   =models.CharField(max_length=100,null=True, blank=True)

    Mucdich_cv      =models.CharField(max_length=900,null=True, blank=True)
    Qhe_captren     =models.CharField(max_length=900,null=True, blank=True)
    Qhe_cungcap     =models.CharField(max_length=900,null=True, blank=True)
    Qhe_capduoi     =models.CharField(max_length=900,null=True, blank=True)
    Qhe_nn_xahoi    =models.CharField(max_length=900,null=True, blank=True)
    Qhe_khachhang   =models.CharField(max_length=900,null=True, blank=True)
    Nh_vu_ket_qua   = models.CharField(max_length=10000000,null=True, blank=True)
    Trach_nhiem     =models.CharField(max_length=50000,null=True, blank=True)
    Mucdo_anhhuong  =models.CharField(max_length=300,null=True, blank=True)
    Ptien_laodong   =models.CharField(max_length=300,null=True, blank=True, default='Máy móc, thiết bị, phương tiện để đảm bảo hoàn thành nhiệm vụ được theo theo qui định của Công ty')

class Mota_Cv7(Mota_Cv_base):

    Yeu_to_1_trinh_do    = models.ForeignKey(Yeu_to_1_trinh_do, null=True, on_delete= models.SET_NULL)
    Yeu_to_2_Ky_nang     = models.ForeignKey(Yeu_to_2_Ky_nang, null=True, on_delete= models.SET_NULL)
    Yeu_to_3_Trach_nhiem = models.ForeignKey(Yeu_to_3_Trach_nhiem, null=True, on_delete= models.SET_NULL)
    Yeu_to_4_Anh_huong   = models.ForeignKey(Yeu_to_4_Anh_huong, null=True, on_delete= models.SET_NULL)
    Yeu_to_5_Sangtao     = models.ForeignKey(Yeu_to_5_Sangtao, null=True, on_delete= models.SET_NULL)
    Yeu_to_6_Giaotiep    = models.ForeignKey(Yeu_to_6_Giaotiep, null=True, on_delete= models.SET_NULL)
    Yeu_to_7_DK_lamviec  = models.ForeignKey(Yeu_to_7_DK_lamviec, null=True, on_delete= models.SET_NULL)
    Ycau_Ngoaingu_23     =  models.ForeignKey(Ycau_Ngoaingu_23, null=True, on_delete= models.SET_NULL)
    Ycau_CNTT_24         = models.ForeignKey(Ycau_CNTT_24, null=True, on_delete= models.SET_NULL)

    ten_nghe_NNDH        = models.ForeignKey(Ten_ngheDH, null=True, on_delete= models.SET_NULL)

    Yeu_to_khac         = models.ForeignKey(Yeu_to_khac, null=True, on_delete= models.SET_NULL)
    tong_diem7           = models.IntegerField(null=True, blank=True)
    Nhom_luong           = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.Ten_Nhom_CV

    def save(self, *args, **kwargs):
        self.tong_diem7 = self.Yeu_to_1_trinh_do.diem + self.Yeu_to_2_Ky_nang.diem + self.Yeu_to_3_Trach_nhiem.diem + self.Yeu_to_4_Anh_huong.diem + self.Yeu_to_5_Sangtao.diem + self.Yeu_to_6_Giaotiep.diem +  self.Yeu_to_7_DK_lamviec.diem

        di =49
        max1 = 950
        max2 = max1 - di +1
        self.Nhom_luong =1

        max3 = max2 - di +1
        max4 = max3 - di +1
        max5 = max4 - di +1
        print(max1,max2, max3, max4, max5)
        max6 = max5 - di +1
        max7 = max6 -di +1
        max8 = max7 - di +1
        max9 = max8 - di +1
        max10 = max9 - di +1
        print(max6,max7, max8, max9, max10)
        max11 = max10 - di +1
        max12 = max11  - di +1
        max13 = max12 - di +1
        max14 = max13  - di +1
        max15 = max14 - di +1
        max16 = max15 - di +1
        print(max11,max12, max13, max14, max15)

        max17 = max16 - di +1
        max18 = max17 - di +1
        max19 = max18 - di +1
        max20 = max19 - di +1
      

        if self.tong_diem7 > max1:
             self.Nhom_luong = 1

        if self.tong_diem7  > max2 and self.tong_diem7 < max2+ di :
             self.Nhom_luong = 2

        if self.tong_diem7  > max3 and self.tong_diem7 < max3+ di :
             self.Nhom_luong = 3

        if self.tong_diem7  > max4 and self.tong_diem7 < max4+ di :
             self.Nhom_luong = 4

        if self.tong_diem7  > max5 and self.tong_diem7 < max5+ di :
             self.Nhom_luong = 5

        if self.tong_diem7  > max6 and self.tong_diem7 < max6+ di :
             self.Nhom_luong = 6

        if self.tong_diem7  > max7 and self.tong_diem7 < max7+ di :
             self.Nhom_luong = 7

        if self.tong_diem7  > max8 and self.tong_diem7 < max8+ di :
             self.Nhom_luong = 8

        if self.tong_diem7  > max9 and self.tong_diem7 < max9+ di :
             self.Nhom_luong = 9


        if self.tong_diem7  > max10 and self.tong_diem7 < max10+ di :
             self.Nhom_luong = 10

        if self.tong_diem7  > max11 and self.tong_diem7 < max11+ di :
             self.Nhom_luong = 11

        if self.tong_diem7  > max12 and self.tong_diem7 < max12+ di :
             self.Nhom_luong = 12

        if self.tong_diem7  > max13 and self.tong_diem7 < max13+ di :
             self.Nhom_luong = 13

        if self.tong_diem7  > max14 and self.tong_diem7 < max14+ di :
             self.Nhom_luong = 14

        if self.tong_diem7  > max15 and self.tong_diem7 < max15+ di :
             self.Nhom_luong = 15

        if self.tong_diem7  > max16 and self.tong_diem7 < max16+ di :
             self.Nhom_luong = 16

        if self.tong_diem7  > max17 and self.tong_diem7 < max17+ di :
             self.Nhom_luong = 17

        if self.tong_diem7  > max18 and self.tong_diem7 < max18+ di :
             self.Nhom_luong = 8

        if self.tong_diem7  > max19 and self.tong_diem7 < max19+ di :
             self.Nhom_luong = 19


        if self.tong_diem7  > max20 and self.tong_diem7 < max20+ di :
             self.Nhom_luong = 20


        super(Mota_Cv7, self).save(*args, **kwargs)



