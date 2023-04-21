from django.db import models
from django.conf import settings
from datetime import date

from django.db.models.signals import post_save

from nhansu.models import trinh_do_qlnn
from nhansu.models import trinh_do_ct
from nhansu.models import Trinhdovh
from nhansu.models import Trinhdo
from nhansu.models import Thanhphan_gd
from nhansu.models import Ton_giao
from nhansu.models import Tinh_que
from nhansu.models import Tinh, Quan_huyen, Phuong_xa, Tinh_sinh
from nhansu.models import Dan_toc, Quocgia

from mota_cv.models import Mota_Cv7
from nhansu.models import Don_vi,Bo_phan,To_nhom
from django.contrib.auth.models import User



# Create your models here.



class Nhan_vien(models.Model):
    class Meta:
        ordering =["ngay_vao_dv"]

    phai = (('Nam','Nam'), ('Nữ','Nữ'))
    hthuc_dt =(('Tập trung','Tập trung'), ('Khác','Khác'))
    Loai_TN = (
         ('Giỏi', 'Giỏi'),
         ('Khá', 'Khá'),
         ('TB', 'Trung bình'),
        )

    tinhtrang_gd =(('Độc thân','Độc thân'), ('Có vợ/chồng','Có vợ/chồng'))

#Thông tin công khai
    avatar          = models.ImageField(upload_to='picture/%Y/%m', blank=True, null=True)
    user            = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)

    ho_lot_thuong_dung = models.CharField(max_length=50, blank=True, null=True)
    ten_thuong_dung = models.CharField(max_length=15, blank=True, null=True)

    vitri_CV        = models.ForeignKey(Mota_Cv7, on_delete= models.SET_NULL, blank=True, null=True)

    ma_nhan_vien    = models.CharField(max_length=5, blank=True, null=True)
    ngay_vao_nganh  = models.DateField(blank=True,null=True)
    ngay_vao_dv     = models.DateField(blank=True,null=True)
    #Nhóm 2:
    tel_dd          = models.CharField(max_length=10, blank=True, null=True)
    email           = models.EmailField(max_length=30, blank=True, null=True)
    Gioi_tinh       = models.CharField(choices=phai, max_length= 3,  null=True, blank=True)
    Nguoi_qly       = models.CharField(max_length=55, blank=True, null=True)
    Nguoi_h_dan     = models.CharField(max_length=55, blank=True, null=True)

 #Thông tin cá nhân:
    ngay_sinh       = models.DateField(blank=True,null=True)
    ma_tinh_noi_sinh= models.ForeignKey(Tinh_sinh, blank=True,null=True, on_delete= models.SET_NULL)
    so_CCCD         = models.CharField(max_length=12, blank=True, null=True)
    ngay_cap_CCCD   = models.DateField(blank=True,null=True)
    so_Hochieu      = models.CharField(max_length=12, blank=True, null=True)
    ngay_cap_hochieu = models.DateField(blank=True,null=True)

    quoctich        = models.ForeignKey(Quocgia, null=True, blank=True, on_delete= models.SET_NULL, default="Việt Nam")
    ton_giao        = models.ForeignKey(Ton_giao, null=True,blank=True, on_delete= models.SET_NULL)
    dan_toc         = models.ForeignKey(Dan_toc, null=True, blank=True, on_delete= models.SET_NULL, default="Kinh")
    Tinhtrang_gd    = models.CharField(choices=tinhtrang_gd, max_length=20, blank=True, null=True)

    thanhphan_gd    = models.ForeignKey(Thanhphan_gd, blank=True,null=True, on_delete= models.SET_NULL, default="1")
    C_danh_kiem_nhiem= models.CharField(max_length=45, blank=True, null=True)
    Nguyen_quan     = models.ForeignKey(Tinh_que, blank=True, null=True, on_delete= models.SET_NULL)

#Ngân hàng và thuế #Bảo hiểm xã hội
    Masothue_cn     = models.CharField(max_length=13, blank=True, null=True)
    So_nguoi_phuthuoc = models.SmallIntegerField(blank=True, null=True, default="0")
    so_so_ld = models.CharField(max_length=12, blank=True, null=True)
    so_so_bhxh      = models.CharField(max_length=10, blank=True, null=True) #Quyết định 595, mã số BHXH, BHYT là số định danh ghi trên sổ BHXH, thẻ BHYT
    ngay_cap_sld    = models.DateField(blank=True,null=True)
    ma_phieu_kcb    = models.CharField(max_length=20, blank=True, null=True)

    Taikhoan_nh     = models.CharField(max_length=12, blank=True, null=True)
    Ten_nganhang    = models.CharField(max_length=25, blank=True, null=True)

    dc_hiennay      = models.CharField(max_length=80, blank=True, null=True)
    dc_thuong_tru   = models.CharField(max_length=120, blank=True, null=True)
    phuong_xa           = models.ForeignKey(Phuong_xa, blank=True, null=True, on_delete= models.SET_NULL)
    quan_huyen          = models.ForeignKey(Quan_huyen, blank=True, null=True, on_delete= models.SET_NULL)
    tinh_thanh          = models.ForeignKey(Tinh, blank=True, null=True, on_delete= models.SET_NULL)

#Thong tin Trình độ:
    trinhdovh       = models.ForeignKey(Trinhdovh, blank=True, null=True, on_delete= models.SET_NULL, default="12/12")
    trinhdo         = models.ForeignKey(Trinhdo, blank=True, null=True, on_delete= models.SET_NULL)
    trinh_do_ctri   = models.ForeignKey(trinh_do_ct, blank=True,null=True, on_delete= models.SET_NULL)
    trinh_do_ql     = models.ForeignKey(trinh_do_qlnn,blank=True, null=True, on_delete= models.SET_NULL)

#Thong tin y te:
    Chieu_cao       = models.IntegerField(blank=True, null=True)
    Can_nang        = models.IntegerField(blank=True, null=True)
    dd_nhan_dang    = models.CharField(max_length=55, blank=True, null=True)

    Danh_hieu_ph_tang=models.CharField(max_length=55, blank=True, null=True)#bệnh mãn tính

#Thong tin dang doan Đang_vien
    Ngay_vao_dang   = models.DateField(blank=True,null=True)
    Ngay_ct         = models.DateField(blank=True,null=True)
    Tai_chi_bo      = models.CharField(max_length=55, blank=True, null=True)
    Chuc_vu_dang    = models.CharField(max_length=55, blank=True, null=True)

    Ngay_vao_doan   = models.DateField(blank=True,null=True)
    Noi_vao_doan    = models.CharField(max_length=55, blank=True, null=True)
    Chuc_vu_doan    = models.CharField(max_length=55, blank=True, null=True)

#So thich, sở trường
    Diem_manh       = models.TextField(max_length=255, blank=True, null=True)
    Diem_yeu        = models.CharField(max_length=255, blank=True, null=True)
    Muctieu_cn      = models.CharField(max_length=255, blank=True, null=True)
    So_truong       = models.CharField(max_length=255, blank=True, null=True)

    Lsu_ban_than    = models.CharField(max_length=255, blank=True, null=True)
    Q_he_nuoc_ngoai = models.CharField(max_length=255, blank=True, null=True)
    Thannhan_nn     = models.CharField(max_length=255, blank=True, null=True)
    Nhan_xet        = models.CharField(max_length=255, blank=True, null=True)


    vitriquanly     = models.BooleanField(default=False)
    don_vi          = models.ForeignKey(Don_vi, null=True, on_delete= models.SET_NULL)
    bo_phan         = models.ForeignKey(Bo_phan, null=True, on_delete= models.SET_NULL)
    to_nhom         = models.ForeignKey(To_nhom, null=True, blank=True, on_delete=models.CASCADE)
    da_nghiviec     = models.BooleanField(default=False)

    Luong_cu      = models.IntegerField(blank=True, null=True)
    Luong_BHXH_cu = models.IntegerField(blank=True, null=True)




    def __str__(self):
       return self.ho_lot_thuong_dung
              #+ self.ten_thuong_dung
    @property
    def tuoi(self):
        today = date.today()
        tuoi =  today.year - self.ngay_sinh.year
        tuoi_stripped = str(tuoi).split(",",1)[0]
        return tuoi_stripped




class Quanly(models.Model):
    quanly             = models.ForeignKey(Nhan_vien, null=True, on_delete=models.SET_NULL)
    ten_thuong_dung    = models.CharField(max_length=15, blank=True, null=True)
    def __str__(self):
        return self.ten_thuong_dung




class daotao(models.Model):
    hthuc_dt = (
         ('Tập trung', 'Tập trung'),
         ('Vừa học vừa làm', 'Vừa học vừa làm')
    )
    Loai_TN = (
         ('Giỏi', 'Giỏi'),
         ('Khá', 'Khá'),
         ('TB', 'Trung bình'),
        )
    Nguoi_daotao      = models.ForeignKey(Nhan_vien, null=True, on_delete=models.SET_NULL)
    Van_bang    = models.ForeignKey(Trinhdo, null=True, on_delete= models.SET_NULL)
    Tu_ngay     = models.DateField(null=True)
    Den_ngay    = models.DateField(null=True)
    Co_so_d_tao = models.CharField(max_length=80, blank=False, null=True)
    Chuyen_nganh    = models.CharField(max_length=80, blank=False, null=True)
    Hinhthuc_dtao   = models.SmallIntegerField(choices= hthuc_dt)
    Loai_TN         = models.CharField(max_length=10, blank=False, null=True, choices=Loai_TN)

    def __str__(self):
       return self.Nguoi_daotao

class khen_nhan_vien(models.Model):
    ht_khenthuong = (
         ('HC', 'Huân chương lao động'),
         ('BKB', 'Bằng khen Bộ'),
         ('BKCP', 'Băng khen Chính phủ'),
         ('CSTĐB', 'CSTĐ Bộ, ngành'),
         ('CSTQ', 'CSTĐ Toàn quốc'),
         ('CSTĐ', 'Chiến sĩ thi đua'),
         ('LDXS', 'LĐ xuất sắc'),
         ('LDTT', 'Lao động Tiên tiến'),
         ('Huy chương', 'Huy chương'),
         ('gk', 'Giấy khen'),
          )

    Nguoi_khen      = models.ForeignKey(Nhan_vien, null=True, on_delete=models.SET_NULL)
    ht_khenthuong   = models.CharField(max_length=20, blank=False, null=True, choices = ht_khenthuong)
    nam_khen        = models.DateField(max_length=4, blank=False, null=True)
    cap_khen        = models.CharField(max_length=50, blank=False, null=True)
def __str__(self):
       return self.Nguoi_khen


class Gia_dinh(models.Model):
    benquanhe = (
        ('Bên ruột','Bên ruột'),
        ('Bên vợ/chồng' ,'Bên vợ/chồng')
    )
    Quanhe = (
         ('cha', 'Cha'),
         ('me', 'Mẹ'),
         ('anh', 'Anh'),
         ('em', 'Em'),
         ('chú', 'Chú'),
         ('Bác', 'Bác'),
         ('Cô', 'Cô'),
         ('Cậu', 'Cậu'),
         ('Dì', 'Dì')
          )

    Nguoi_khai      = models.ForeignKey(Nhan_vien, null=True, on_delete=models.SET_NULL)
    Quan_he         = models.CharField(max_length=20, blank=True, null=True, choices = Quanhe)
    ho_ten_quanhe   = models.CharField(max_length=50, blank=True, null=True)
    Nam_sinh        = models.DateField(blank=True, null=True)
    diachi_giadinh  = models.CharField(max_length=150, blank=True, null=True)
    Nghe_nghiep     = models.CharField(max_length=50, blank=True, null=True)
    Noi_Lamviec     = models.CharField(max_length=150, blank=True, null=True)
    ben_vo_chong    = models.CharField(max_length=50, blank=True, null=True, choices= benquanhe)


