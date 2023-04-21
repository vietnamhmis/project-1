from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

from nhansu.models import Ton_giao
from nhansu.models import Tinh_que
from nhansu.models import Tinh, Quan_huyen, Phuong_xa, Tinh_sinh
from nhansu.models import Dan_toc, Quocgia,coso_KCB


# Create your models here.
from nhansu.models import Tinh_HK, Quan_huyen_HK, Phuong_xa_HK




class BHXHTN(models.Model):
    phai = (('Nam','Nam'), ('Nữ','Nữ'))
    doituongbh = (('Cận nghèo','Cận nghèo'),
                  ('Người có công','Người có công'),
                  ('Hộ gia đình ', 'Hộ gia đình'))


#Thông tin công khai

    #user      = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    HOTEN         = models.CharField(max_length=150, blank=True, null=True)
    SOBHXH        = models.CharField(max_length=10, blank=True, null=True) #Quyết định 595, mã số BHXH, BHYT là số định danh ghi trên sổ BHXH, thẻ BHYT
    SOKCB      = models.CharField(max_length=10, blank=True, null=True) #Quyết định 595, mã số BHXH, BHYT là số định danh
    NGAYSINH      = models.DateField(blank=True, null=True)
    NAMSINH    = models.IntegerField( blank=True, null=True)
    #email           = models.EmailField(max_length=30, blank=True, null=True)
    GIOITINH      = models.CharField(choices=phai, max_length= 3,  null=True, blank=True)

    NOIKHAI    = models.CharField(max_length=120, blank=True, null=True)
    tinh_thanh   = models.ForeignKey(Tinh, blank=True, null=True, on_delete= models.SET_NULL)
    quan_huyen   = models.ForeignKey(Quan_huyen, blank=True, null=True, on_delete= models.SET_NULL)
    phuong_xa      = models.ForeignKey(Phuong_xa, blank=True, null=True, on_delete= models.SET_NULL)

    NOICAP     = models.CharField(max_length=12, blank=True, null=True)
    NGAYCMND   = models.DateTimeField(blank=True, null=True)
    MA_TINHCMT = models.ForeignKey(Tinh_que, blank=True, null=True, on_delete= models.SET_NULL)

    QUOCTICH   = models.ForeignKey(Quocgia, null=True, blank=True, on_delete= models.SET_NULL, default="Việt Nam")
    DANTOC     = models.ForeignKey(Dan_toc, null=True, blank=True, on_delete= models.SET_NULL, default="Kinh")

    DIACHI          = models.CharField(max_length=120, blank=True, null=True)
    TINH_LH    = models.IntegerField(blank=True, null=True)
    HUYEN_LH   = models.IntegerField(blank=True, null=True)
    XA_LH      = models.IntegerField(blank=True, null=True)

    DIACHIHK    = models.CharField(max_length=120, blank=True, null=True)
   # TINH_HK     = models.ForeignKey(Tinh_HK, blank=True, null=True, on_delete= models.SET_NULL)
   # HUYEN_HK    = models.ForeignKey(Quan_huyen_HK, blank=True, null=True, on_delete= models.SET_NULL)
   # XA_HK       = models.ForeignKey(Phuong_xa_HK, blank=True, null=True, on_delete= models.SET_NULL)

    MAPB        = models.CharField(max_length=20, blank=True, null=True)
    MADT        = models.CharField(choices=doituongbh, max_length= 30,  null=True, blank=True)
    TUNGAY      = models.DateTimeField(blank=True, null=True)
    DENNGAY     = models.DateTimeField(blank=True, null=True)
    SOTHANG     = models.CharField(max_length=20, blank=True, null=True)
    TUTHANG     = models.CharField(max_length=2, blank=True, null=True)
    DENTHANG    = models.CharField(max_length=2, blank=True, null=True)

    TYLE        = models.DecimalField(default=4.5,max_digits = 5, decimal_places=2, null=True, blank=True)
    TYLE_NSNN   = models.DecimalField(default=0,max_digits = 5, decimal_places=2, null=True, blank=True)
    TYLEDONG    = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)

    ML_DK        = models.IntegerField(blank=True, null=True)
    HSL_DK       = models.IntegerField(blank=True, null=True)
    ML_dong      = models.IntegerField(blank=True, null=True)

    HSL             = models.DecimalField(default=1,max_digits = 5, decimal_places=2, null=True, blank=True)
    PA              = models.IntegerField(blank=True, null=True)
    ML              = models.IntegerField(default=1490000, blank=True, null=True)
    MA_BV               = models.CharField(max_length=4, blank=True, null=True)
    MA_TINH         = models.CharField(max_length=5, blank=True, null=True)
    MAVUNGSS        = models.CharField(max_length=40, blank=True, null=True)
    TAMTRU          = models.CharField(max_length=120, blank=True, null=True)

    SOBL            = models.IntegerField( blank=True, null=True)
    NGAYBL              =  models.DateTimeField(auto_now_add=True,blank=True, null=True)
    SDT             = models.IntegerField( blank=True, null=True)
    MA_CA           = models.CharField(max_length=120, blank=True, null=True)
    GHICHU          = models.CharField(max_length=120, blank=True, null=True)
    GIAM_DO_CHET    = models.BooleanField(default=False)



    def __str__(self):
       return self.HOTEN

#    def get_sotien_phaidong_BHXH(self): #ghi số tiền phải đóng BHXH tự nguyện
     #   return self.get_diem_congviec_kpi() * self.quantity

  #  def get_sotien_nn_hotro_BHXH(self): #ghi số tiền ngân sách nhà nước hỗ trợ đóng:tỉ lệ NNhỗ trơ x mức chuẩn nghèo nông thôn x 22%).
 #       return self.TYLE_NSNN() * 22/100 *1









