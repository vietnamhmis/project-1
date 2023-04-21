from django.db.models.signals import post_save
from django.conf import settings
from datetime import date, timedelta
from django.db import models
from enroll.models import Nhan_vien
from nhansu.models import Don_vi,Bo_phan, To_nhom, TK_ngach
from dbview.models import DbView
from mota_cv.models import Mota_Cv7

from django.db.models import Avg, Max, Min

#--------------------------------------------------------
class nhanvientest(models.Model):
    ten_danhmuc = models.CharField(max_length=60, blank=True, null=True)
    kyhieu_cc = models.CharField(max_length=6, blank=True, null=True)
    def __str__(self):
        return self.kyhieu_cc

class DmChamcong(models.Model):
    ten_danhmuc = models.CharField(max_length=60, blank=True, null=True)
    kyhieu_cc = models.CharField(max_length=6, blank=True, null=True)
    nhanvien      = models.ForeignKey(nhanvientest,blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.kyhieu_cc

class bangluong_chinh(models.Model):
    Nhom_luong      =models.ForeignKey(TK_ngach, null=True, blank=True, on_delete=models.SET_NULL)
    diem            =models.ForeignKey(Mota_Cv7, null=True, blank=True, on_delete=models.SET_NULL)
    Bac_1           = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    Bac_2           = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    Bac_3           = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    Bac_4           = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    Bac_5           = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    Boiso           = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    tong_diem       = models.IntegerField(blank=False, null=True)
    luong_toi_thieu = models.IntegerField(blank=False, null=True)
    start_date      = models.DateTimeField(auto_now_add=True)
    ordered         = models.BooleanField(default=False)
    Luong_bac_1     = models.IntegerField(blank=False, null=True)

    def save(self, *args, **kwargs):
        if self.Bac_1 and self.luong_toi_thieu:
            self.Luong_bac_1 = int(self.Bac_1) * int(self.luong_toi_thieu)
        else:
            self.Luong_bac_1 =0
        super(bangluong_chinh, self).save(*args, **kwargs)

    def get_luong_bac(self):
        if self.Bac_1:
            return round(self.Bac_1 * self.luong_toi_thieu)
        else:
            return 1

    def get_luong_bac1(self):
        if self.Bac_1:
            return format(round(self.Bac_1 * self.luong_toi_thieu), ",")
        else:
            return 1

    def get_luong_bac2(self):
        if self.Bac_2:
            return format(round(self.Bac_2 * self.luong_toi_thieu), ",")
        else:
            return 1

    def get_luong_bac3(self):
        if self.Bac_5:
            return format(round(self.Bac_5 * self.luong_toi_thieu), ",")
        else:
            return 1

    def get_luong_bac4(self):
        if self.Bac_5:
            return format(round(self.Bac_5 * self.luong_toi_thieu), ",")
        else:
            return 1


    def get_luong_bac5(self):
        if self.Bac_5:
            return format(round(self.Bac_5 * self.luong_toi_thieu), ",")
        else:
            return 1


    def __str__(self):
       return str(self.Nhom_luong)



class bangluong_BHXH(models.Model):
    Nhom_luong      =models.ForeignKey(TK_ngach, null=True, blank=True, on_delete=models.SET_NULL)
    diem            =models.ForeignKey(Mota_Cv7, null=True, blank=True, on_delete=models.SET_NULL)
    Bac_1           = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    Bac_2           = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    Bac_3           = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    Bac_4           = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    Bac_5           = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    Boiso           = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    tong_diem       = models.IntegerField(blank=False, null=True)
    luong_toi_thieu = models.IntegerField(blank=False, null=True)
    start_date      = models.DateTimeField(auto_now_add=True)
    ordered         = models.BooleanField(default=False)
    Luong_bac_1     = models.IntegerField(blank=False, null=True)

    def save(self, *args, **kwargs):
        if self.Bac_1 and self.luong_toi_thieu:
            self.Luong_bac_1 = int(self.Bac_1) * int(self.luong_toi_thieu)
        else:
            self.Luong_bac_1 =0
        super(bangluong_BHXH, self).save(*args, **kwargs)

    def get_luong_bac(self):
        if self.Bac_1:
            return round(self.Bac_1 * self.luong_toi_thieu)
        else:
            return 1

    def get_luong_bac1(self):
        if self.Bac_1:
            return format(round(self.Bac_1 * self.luong_toi_thieu), ",")
        else:
            return 1

    def get_luong_bac2(self):
        if self.Bac_2:
            return format(round(self.Bac_2 * self.luong_toi_thieu), ",")
        else:
            return 1

    def get_luong_bac3(self):
        if self.Bac_5:
            return format(round(self.Bac_5 * self.luong_toi_thieu), ",")
        else:
            return 1

    def get_luong_bac4(self):
        if self.Bac_5:
            return format(round(self.Bac_5 * self.luong_toi_thieu), ",")
        else:
            return 1


    def get_luong_bac5(self):
        if self.Bac_5:
            return format(round(self.Bac_5 * self.luong_toi_thieu), ",")
        else:
            return 1

    def __str__(self):
       return str(self.Nhom_luong)





class Phuongan_luong(models.Model):
    Nhom_luong      =models.ForeignKey(bangluong_chinh, null=True, blank=True, on_delete=models.SET_NULL)
    Nhanvien        =models.ForeignKey(Nhan_vien, null=True, blank=True, on_delete=models.SET_NULL)
    Luong_BHXH_cu   = models.IntegerField(blank=False, null=True)
    Luong_cu        = models.IntegerField(blank=False, null=True)

    Bac_1           = models.IntegerField(blank=False, null=True)
    Bac_2           = models.IntegerField(blank=False, null=True)
    Bac_3           = models.IntegerField(blank=False, null=True)
    Bac_4           = models.IntegerField(blank=False, null=True)
    Bac_5           = models.IntegerField(blank=False, null=True)

    Luong_BHXH_moi   = models.IntegerField(blank=False, null=True)
    Luong_moi        = models.IntegerField(blank=False, null=True)
    CL_Luong_BHXH_PA_1   = models.IntegerField(blank=False, null=True)
    CL_Luong_moi_PA_1        = models.IntegerField(blank=False, null=True)
    luong_toi_thieu = models.IntegerField(blank=False, null=True)
    start_date      = models.DateTimeField(auto_now_add=True)
    ordered         = models.BooleanField(default=False)


class Phuongan_luongbhxh(models.Model):
    Nhom_luong      =models.ForeignKey(bangluong_chinh, null=True, blank=True, on_delete=models.SET_NULL)
    Nhom_luongBH    =models.ForeignKey(bangluong_BHXH, null=True, blank=True, on_delete=models.SET_NULL)
    Nhanvien        =models.ForeignKey(Nhan_vien, null=True, blank=True, on_delete=models.SET_NULL)
    Luong_BHXH_cu   = models.IntegerField(blank=False, null=True)
    Luong_cu        = models.IntegerField(blank=False, null=True)
    Bac_1           = models.IntegerField(blank=False, null=True)
    Bac_2           = models.IntegerField(blank=False, null=True)
    Bac_3           = models.IntegerField(blank=False, null=True)
    Bac_4           = models.IntegerField(blank=False, null=True)
    Bac_5           = models.IntegerField(blank=False, null=True)
    Luong_BHXH_moi   = models.IntegerField(blank=False, null=True)
    Luong_moi        = models.IntegerField(blank=False, null=True)
    CL_Luong_BHXH_PA_1   = models.IntegerField(blank=False, null=True)
    CL_Luong_moi_PA_1        = models.IntegerField(blank=False, null=True)
    luong_toi_thieu = models.IntegerField(blank=False, null=True)

    ordered         = models.BooleanField(default=False)

    def get_Luong_BHXH_moi(self):
        if  self.Nhom_luongBH.Bac_2 and self.Nhom_luong.luong_toi_thieu :
            return  int(self.Nhom_luong.luong_toi_thieu) * int(self.Nhom_luongBH.Bac_2)




    def save(self, *args, **kwargs):
        if  self.Nhom_luongBH.Bac_2:
            self.Luong_BHXH_moi = int(self.Nhom_luongBH.Bac_2) * int(self.Nhom_luongBH.luong_toi_thieu)
        else:
            self.Luong_BHXH_moi =0
        super(Phuongan_luongbhxh, self).save(*args, **kwargs)



    def save(self, *args, **kwargs):
        if self.Luong_BHXH_cu and self.Luong_BHXH_moi:
            self.CL_Luong_BHXH_PA_1 = self.Luong_BHXH_moi - self.Luong_BHXH_cu
        else:
            self.CL_Luong_BHXH_PA_1 =0
        super(Phuongan_luongbhxh, self).save(*args, **kwargs)

class bangluong(models.Model):
    bac = (
         ('Bậc 1', 'Bậc 1'),
         ('Bậc 2', 'Bậc 2'),
         ('Bậc 3', 'Bậc 3'),
         ('Bậc 4', 'Bậc 4'),
         ('Bậc 5', 'Bậc 5'),
         ('Bậc 6', 'Bậc 6'),
         ('Bậc 7', 'Bậc 7'),

         ('Bậc 8', 'Bậc 8'),
         ('Bậc 9', 'Bậc 9'),
         ('Bậc 10', 'Bậc 10'),
        )

    Nhom_luong      = models.CharField(max_length=20, blank=False, null=True)
    Heso            = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    Bac             = models.CharField(max_length=20, blank=False, null=True, choices=bac)
    Boiso           = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    Muc_luong       = models.IntegerField(blank=False, null=True)

    def save(self):
        self.Muc_luong = self.Heso * 4900000
        return super(bangluong, self).save()
    def __str__(self):
       return self.Nhom_luong  +' '+ self.Bac

class hd_laodong(models.Model):
    class Meta:
        ordering =["Tu_ngay", "id"]
    Loai_hd = (
         ('Có thời hạn', 'Có thời hạn'),
         ('Không thời hạn', 'Không thời hạn'),
         ('Thử việc', 'Thử việc'),
        )
    ht_traluong = (
        ('Khoán', 'Khoán'),
        ('Thời gian', 'Thời gian'),
        ('Sản phẩm', 'Sản phẩm'),
    )
    So_hopdong      = models.CharField(max_length=20, blank=False, null=True)
    Ho_ten          = models.ForeignKey(Nhan_vien,  blank=True, null=True,  on_delete= models.SET_NULL)
    Hoten_nhanvien  = models.CharField(max_length=150, blank=True, null=True, default="Họ tên")
    Loai_hd         = models.CharField(max_length=20, blank=False, null=True, choices = Loai_hd, default='Không thời hạn')
    Tu_ngay         = models.DateField(null=True, blank=True)
    Den_ngay        = models.DateField(null=True, blank=True)
    start_date      = models.DateTimeField(auto_now_add=True)

    Ht_traluong     = models.CharField(max_length=20,  blank=True, null=True, choices = ht_traluong, default='Khoán')
    bangluong       = models.ForeignKey(bangluong,  blank=True, null=True, on_delete= models.SET_NULL)
    Heso            = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    Bac             = models.CharField(max_length=10,  blank=True, null=True,)
    Muc_luong       = models.IntegerField( blank=True, null=True,)

    Loai_hd_kth     =  models.BooleanField(blank=True, null=True, default=True)
    Loai_hd_coth    = models.BooleanField(blank=True, null=True,default=False)
    Loai_hd_thu_viec = models.BooleanField(blank=True, null=True, default=False)

    Nang_luong      = models.BooleanField(blank=True, null=True, default=False)
    Dieudong        = models.BooleanField(blank=True, null=True, default=False)
    Bo_nhiem        = models.BooleanField(blank=True, null=True, default=False)
    Ly_do           = models.CharField(max_length=10, blank=True, null=True)
    Ngay_nangluong_sau  = models.DateField(auto_now_add=True, blank=True, null=True)
    Thu_nhap        = models.IntegerField(blank=True, null=True)
    Hieuluc         = models.BooleanField(blank=True, null=True, default=True)

  #  def save(self):
       # self.Heso = self.bangluong.Heso
       # self.Bac = self.bangluong.Bac
        #self.Hoten_nhanvien = self.Ho_ten.ho_lot_thuong_dung
      #  self.Muc_luong = self.bangluong.Muc_luong
        #self.Thu_nhap = self.Muc_luong + self.Phucap_kn +self.Phucap_khac +self.Tien_an + self.Boiduong_dochai
       # return super(hd_laodong, self).save()

    @property
    def Day_still(self):
        if  self.Den_ngay != None:
            today = date.today()
            days_still = self.Den_ngay - today
            days_still_splited = str(days_still).split(",",1)[0]
            return days_still_splited
    @property
    def Day_nangluong(self):
        if  self.Ngay_nangluong_sau != None and self.Hieuluc != None and self.Heso > 12:
            nangluong = self.Ngay_nangluong_sau
        else:
            nangluong = self.Ngay_nangluong_sau

            return nangluong

    @property
    def Day_past(self):
        if  self.Den_ngay != None:
            today = date.today()
            if self.Den_ngay >= today:
                thing ='Ngày đến hạn'
            else:
                thing ='Quá hạn'
            return thing

class hd_laodong_thu(models.Model):
    Loai_hd = (
         ('Có thời hạn', 'Có thời hạn'),
         ('Không thời hạn', 'Không thời hạn'),
         ('Thử việc', 'Thử việc'),
        )
    ht_traluong = (
        ('Khoán', 'Khoán'),
        ('Thời gian', 'Thời gian'),
        ('Sản phẩm', 'Sản phẩm'),
    )
    So_hopdong      = models.CharField(max_length=20, blank=False, null=True)
    Ho_ten          = models.ForeignKey(Nhan_vien,  blank=True, null=True,  on_delete= models.SET_NULL)
    Hoten_nhanvien  = models.CharField(max_length=150, blank=True, null=True, default="Họ tên")
    Loai_hd         = models.CharField(max_length=20, blank=False, null=True, choices = Loai_hd, default='Không thời hạn')
    Tu_ngay         = models.DateField(null=True, blank=True)
    Den_ngay        = models.DateField(null=True, blank=True)
    start_date      = models.DateTimeField(auto_now_add=True)

    Ht_traluong     = models.CharField(max_length=20,  blank=True, null=True, choices = ht_traluong, default='Khoán')
    bangluong       = models.ForeignKey(bangluong,  blank=True, null=True, on_delete= models.SET_NULL)
    Heso            = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    Bac             = models.CharField(max_length=10,  blank=True, null=True,)
    Muc_luong       = models.IntegerField( blank=True, null=True,)

    Loai_hd_kth     =  models.BooleanField(blank=True, null=True, default=True)
    Loai_hd_coth    = models.BooleanField(blank=True, null=True,default=False)
    Loai_hd_thu_viec = models.BooleanField(blank=True, null=True, default=False)

    Nang_luong      = models.BooleanField(blank=True, null=True, default=False)
    Dieudong        = models.BooleanField(blank=True, null=True, default=False)
    Bo_nhiem        = models.BooleanField(blank=True, null=True, default=False)
    Ly_do           = models.CharField(max_length=10, blank=True, null=True)

    Ngay_nangluong_sau  = models.DateField(auto_now_add=True, blank=True, null=True)

    Thu_nhap        = models.IntegerField(blank=True, null=True)
    Hieuluc         = models.BooleanField(blank=True, null=True, default=True)


class Chamcong(models.Model):
    user      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    kyhieu_cc = models.CharField(max_length=6, blank=True, null=True)
    Ngay_1    = models.CharField( max_length=3, blank=True, null=True,  default ="X")
    Ngay_2    = models.CharField( max_length=3, blank=True, null=True, default ="X")
    def __str__(self):
        return self.user.username


class Chamcongchitiet(models.Model):
   nam = (

          ('2021', '2021'),
          ('2022', '2022'),
          ('2023', '2023'),
          ('2024', '2024'),
          ('2025', '2025'),
        )
   truc = (
          ('T', 'Trực'),
          ('N', 'Nghỉ'),

        )
   thang = (
          ('1', '1'),
          ('2', '2'),
          ('3', '3'),
          ('4', '4'),
          ('5', '5'),
          ('6', '6'),
          ('7', '7'),
          ('8', '8'),
          ('9', '9'),
          ('10', '10'),
          ('11', '11'),
          ('12', '12'),
        )
   ngay = (

          ('Ô', 'Ốm, điều dưỡng'),
          ('X', 'làm việc'),

        )
   Nhan_vien    = models.ForeignKey(Nhan_vien, blank=True, null=True, on_delete=  models.SET_NULL)

   don_vi       = models.ForeignKey(Don_vi, blank=True, null=True, on_delete= models.SET_NULL)
   bo_phan      = models.ForeignKey(Bo_phan,  blank=True, null=True, on_delete= models.SET_NULL)
   to_nhom      = models.ForeignKey(To_nhom,blank=True, null=True, on_delete=models.CASCADE)

   thang        =  models.CharField(max_length=2, blank=True, null=True, choices = thang, default='4')
   Nam          = models.CharField(max_length=4, blank=True, null=True, choices=nam, default='2022')
   Ngay_1    = models.CharField( max_length=3, blank=True,null= True, choices= ngay, default ="X")
   Ngay_2    = models.CharField( max_length=3,blank=True, null= True, choices= ngay, default ="X")
   Ngay_3   = models.CharField( max_length=3,blank=True, null= True, choices= ngay, default ="X")
   Ngay_4   = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_5    = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_6    = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_7    = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_8    = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_9   = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_10   = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_11    = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_12    = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_13    = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_14    = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_15   = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_16   = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_17   = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_18    = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_19    = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_20    = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")

   Ngay_21   = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_22   = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_23    = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_24    = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")

   Ngay_25   = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_26   = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_27   = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_28   = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_29   = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_30   = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_31   = models.CharField( max_length=3, blank=True, null=True, choices= ngay, default ="X")
   Ngay_truc24 = models.CharField(max_length=6, blank=False, null=True, choices = truc, default='Trực')
   Ngay_cong = models.IntegerField(blank=True, null=True)
   #Ngay_BHXH = models.IntegerField(blank=True, null=True)
   Ngaycham    = models.DateField( null=True, blank=True)





class luongthang(models.Model):
    nam = (
          ('2021', '2021'),
          ('2022', '2022'),
          ('2023', '2023'),
          ('2024', '2024'),
          ('2025', '2025'),
        )
    thang = (
          ('1', '1'),
          ('2', '2'),
          ('3', '3'),
          ('4', '4'),
          ('5', '5'),
          ('6', '6'),
          ('7', '7'),
          ('8', '8'),
          ('9', '9'),
          ('10', '10'),
          ('11', '11'),
          ('12', '12'),
   )


    Thang_tra_luong =  models.CharField(max_length=2, blank=True, null=True, choices = thang, default='2')
    Nam             = models.CharField(max_length=4, blank=True, null=True, choices=nam, default='2022')
    hoten_nhanvien  = models.ForeignKey(Nhan_vien, on_delete= models.SET_NULL,blank=True, null=True)

    don_vi          = models.ForeignKey(Don_vi, blank=True, null=True, on_delete= models.SET_NULL)
    bo_phan          = models.ForeignKey(Bo_phan,  blank=True, null=True, on_delete= models.SET_NULL)
    to_nhom          = models.ForeignKey(To_nhom,blank=True, null=True, on_delete=models.CASCADE)

    Heso            = models.ForeignKey(hd_laodong, null=True, on_delete= models.SET_NULL)
    Muc_luongBHXH   = models.IntegerField(blank=True, null=True)
    Tam_ung         = models.IntegerField(blank=True, null=True)
    Muc_luong       = models.IntegerField(blank=True, null=True)

    luong_p2        = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    luong_p3        = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    Gio_lam_them    = models.DecimalField(max_digits = 4, decimal_places=1, null=True, blank=True)
    Gio_lam_them_CT = models.DecimalField(max_digits = 4, decimal_places=1, null=True, blank=True)
    Gio_lam_them_le = models.DecimalField(max_digits = 4, decimal_places=1, null=True, blank=True)


    phucap_knhiem       = models.IntegerField(blank=True, null=True)
    phucap_khac     = models.IntegerField(blank=True, null=True)
    Tien_an        = models.IntegerField(blank=True, null=True)
    Luong_thang     = models.IntegerField(blank=True, null=True)

    Ngay_cong       = models.IntegerField(blank=True, null=True)
    cham_cong       = models.OneToOneField(Chamcongchitiet, blank=True, null=True, on_delete= models.SET_NULL)

    Boiduong_dochai = models.IntegerField(blank=True, null=True)
    Thu_nhap        = models.IntegerField(blank=True, null=True)
    kn_thuetncn     = models.IntegerField(blank=True, null=True)
    kn_BHXH_BYTT    = models.IntegerField(blank=True, null=True)
    kn_KPCĐ         = models.IntegerField(blank=True, null=True)
    kn_khac         = models.IntegerField(blank=True, null=True)
    luong_themgio   = models.IntegerField(blank=True, null=True)
    Luong_lamthemT7 = models.IntegerField(blank=True, null=True)
    Luong_lamthemle = models.IntegerField(blank=True, null=True)

    Thu_nhapthuclinh = models.IntegerField(blank=True, null=True)

    @classmethod
    def view(klass):
        qs = (hd_laodong.objects.filter().values('hoten_nhanvien_ID', 'Heso', ))
        return str(qs.query)

def save(self):
     def save(self):
        self.don_vi = self.Nhan_vien.don_vi
        self.bo_phan = self.Nhan_vien.bo_phan
        self.to_nhom = self.Nhan_vien.to_nhom
        self.Ngay_cong = self.Chamcongchitiet.Ngay_cong

        ngaycong_chedo= 22
        Luong_TT= 4680000

        self.Luong_thang = (self.Heso * Luong_TT) / self.Ngay_cong /ngaycong_chedo
        self.Tien_an = self.Ngay_cong * 22000

        self.luong_themgio = (self.Heso * Luong_TT)/ngaycong_chedo * self.Gio_lam_them * 150/100
        self.Luong_lamthemT7 = (self.Heso * Luong_TT)/ngaycong_chedo * self.Gio_lam_them_CT * 200/100
        self.Luong_lamthemle = (self.Heso * Luong_TT)/ngaycong_chedo * self.Gio_lam_them_le * 300/100

        self.Thu_nhap = self.Luong_thang + self.Phucap_kn +self.Phucap_khac +self.Tien_an + self.Boiduong_dochai + self.Luong_lamthem + self.Luong_lamthemT7 + self.Luong_lamthemle

        self.kn_thuetncn = self.Muc_luong * 10/100
        self.kn_BHXH_BYTT = self.Muc_luongBHXH * 11.5/100
        self.kn_KPCĐ = self.Muc_luongBHXH * 1/100
        self.Thu_nhapthuclinh = self.Thu_nhap - self.kn_thuetncn - self.kn_BHXH_BYTT -  self.kn_KPCĐ - self.Tam_ung
        return super(luongthang, self).save()


def file_re(sender, instance, created, *args, **kwargs):
    if created:
        userfile = Chamcong.objects.create(user=instance)
post_save.connect(file_re, sender=settings.AUTH_USER_MODEL)





def nhanvien_cham_cong(sender, instance, created, **kwargs):
    if created:
        userfile = hd_laodong.objects.create(nhanvien=instance)
post_save.connect(nhanvien_cham_cong, sender=nhanvientest)

