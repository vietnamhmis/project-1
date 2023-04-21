from django.db import models

from mota_cv.models import Mota_Cv7
from nhansu.models import Nang_luc_2
from enroll.models import Nhan_vien, Quanly

from django.conf import settings

# Create your models here.

class Congviec_nangluc(models.Model):
    class Meta:
        unique_together = ('chucdanh_CV', 'nangluc_cv') #chức danh + năng lực không tạo trùng
        # Đổi tên table db_table = 'khung_nangluc
        ordering= ['chucdanh_CV', 'nangluc_cv__loai_nang_luc', 'stt', 'name',]

    user                  = models.ForeignKey("auth.User", blank=True, null=True, on_delete=models.SET_NULL)
    name                  = models.CharField(max_length=70, null=False, blank=False)
    chucdanh_CV           = models.ForeignKey(Mota_Cv7, default=15, null=True, on_delete=models.CASCADE)
    nangluc_cv            = models.ForeignKey(Nang_luc_2, null=True, blank=True, on_delete=models.CASCADE)
    Muc_quantrong_nluc    = models.IntegerField(default=2)
    Muc_thanhthao_nluc    = models.IntegerField(default=3)
    Diem_tieuchuan        = models.IntegerField()
    stt                   = models.IntegerField(default=2)

    def save(self, *args, **kwargs):
        self.Diem_tieuchuan = int(self.Muc_quantrong_nluc) * int(self.Muc_thanhthao_nluc)

        super(Congviec_nangluc, self).save(*args, **kwargs)



    def get_Diem_tieuchuan(self):
        return self.Muc_quantrong_nluc * self.Muc_thanhthao_nluc



    def __str__(self):
        return self.nangluc_cv.name



       #return f"{self.nangluc_cv.name} of {self.chucdanh_CV.Ten_vitri_full}"




class Danhgia_nluc(models.Model):
    class Meta:

        unique_together = ('Landanhgia_nagluc', 'Nhanvien_dg_nangluc', 'TenNangluc_congviec') #chức danh + năng lực không tạo trùng
        # Đổi tên table db_table = 'khung_nangluc
        ordering= ['Nhanvien_dg_nangluc', 'TenNangluc_congviec',]
    user                  = models.ForeignKey("auth.User", blank=True, null=True, on_delete=models.SET_NULL)
    Landanhgia_nagluc     = models.CharField(max_length=20, blank=True, null=True)
    Nhanvien_dg_nangluc   = models.ForeignKey(Nhan_vien, null=True, blank=True, on_delete=models.SET_NULL)
    TenNangluc_congviec   = models.ForeignKey(Congviec_nangluc, blank=True,  null=True, on_delete=models.CASCADE)
    Quanly_dg_nangluc     = models.ForeignKey(Quanly, null=True, blank=True, on_delete=models.SET_NULL)

    tu_danhgia_dapung     = models.IntegerField(blank=True, null=True)# Cá nhân tự đánh giá
    Quanly_danhgia        = models.IntegerField(blank=True, null=True)# Quản lý đánh giá cá nhân
    Ketqua_danhgia        = models.IntegerField(blank=True, null=True)# Điểm thống nhất cuối cùng

    Diem_tieuchuan       = models.IntegerField(blank=True, null=True) # Điểm tiêu chuẩn Thành thạo và Mức Quan trọng năng lực
    Diem_tu_danhgia      = models.IntegerField(blank= True, null=True)
    Diem_dat             = models.IntegerField(blank= True, null=True) # Điểm kết quả cuối Thành thạo và Mức Quan trọng năng lực


    Ketqua_tile         = models.CharField(max_length=220, blank=True, null=True)

    start_date            = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    Kha_nang_dapung       = models.IntegerField( blank=True, null=True)
    #---------
    def save(self, *args, **kwargs):
        self.Diem_tu_danhgia = int(self.tu_danhgia_dapung) * int(self.TenNangluc_congviec.Muc_quantrong_nluc)
        self.Diem_dat = int(self.Ketqua_danhgia) * int(self.TenNangluc_congviec.Muc_quantrong_nluc)

        super(Danhgia_nluc, self).save(*args, **kwargs)



    #------------

    def get_Diem_tu_danhgia(self):
        return self.TenNangluc_congviec.Muc_quantrong_nluc * self.tu_danhgia_dapung

    def get_Diem_ql_danhgia(self):
        return self.TenNangluc_congviec.Muc_quantrong_nluc * self.Quanly_danhgia
    def get_Diem_dat(self):
        return self.TenNangluc_congviec.Muc_quantrong_nluc * self.Ketqua_danhgia

    def get_Diem_tieuchuan(self):
        return self.TenNangluc_congviec.Muc_quantrong_nluc * self.TenNangluc_congviec.Muc_thanhthao_nluc

    def get_ketqua(self):
        return self.get_Diem_dat/ self.get_Diem_tieuchuan



#------------------







#================================================

class tong_nl(models.Model):
    user                     = models.ForeignKey("auth.User", blank=True, null=True, on_delete=models.SET_NULL)
    Nhanvien_dg_nangluc      = models.ForeignKey(Nhan_vien, null=True, blank=True, on_delete=models.SET_NULL)
    Ketqua_danhgia          = models.IntegerField(null=True, blank=True,)
    items                   = models.ForeignKey(Danhgia_nluc, null=True, blank=True, on_delete=models.CASCADE)
    ordered                 = models.BooleanField(default=False)

    #def save(self):
   #     self.Ketqua_danhgia = self.Nhanvien_dg_nangluc
    #    return super(tong_nl, self).save()

    #def save(self,*args,**kwargs):
       # self.request.user = get_current_logged_in_user() <--- Some validation or cleaning you want to do here.
  #super.save(*args,**kwargs)


    def get_tongdiemchuan(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_diem_chuan()
        return total

    def get_tong_diemdat(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_diem_dat()
        return total


##############################--------------------------https://www.youtube.com/watch?v=Qc5NnpxFbBo&t=4s
