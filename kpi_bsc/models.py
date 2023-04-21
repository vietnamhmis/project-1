from django.db import models
from mota_cv.models import Mota_Cv7
from nhansu.models import KPI_list
from enroll.models import Nhan_vien, Quanly
from django.conf import settings

class Khung_kpi(models.Model):
    class Meta:
        unique_together = ('chucdanh_CV', 'kpi_cv') #kpi_cv+ năng lực không tạo trùng
        ordering= ['chucdanh_CV', 'kpi_cv__loai_kpi', 'kpi_cv__ma_kpi', 'stt',]

    user                  = models.ForeignKey("auth.User", blank=True, null=True, on_delete=models.SET_NULL)
    name                  = models.CharField(max_length=70, null=True, blank=True,)
    chucdanh_CV           = models.ForeignKey(Mota_Cv7, null=True, blank=True, on_delete=models.CASCADE)
    kpi_cv                = models.ForeignKey(KPI_list, null=True, blank=True, on_delete=models.CASCADE)
    chi_tieu               = models.IntegerField(default=1)
    ti_trong               = models.DecimalField(max_digits=3, default=0.05, decimal_places=2, null=True, blank=True,)
    stt                   = models.IntegerField(default=2)
    def __str__(self):
        return self.kpi_cv.name


class Danhgia_KPI(models.Model):
    class Meta:
        ordering= ['Nhanvien_dg_KPI', 'Ten_kpi',]

    user                  = models.ForeignKey("auth.User", blank=True, null=True, on_delete=models.SET_NULL)
    Landanhgia_KPI          = models.CharField(max_length=20, blank=True, null=True)
    Nhanvien_dg_KPI     = models.ForeignKey(Nhan_vien, null=True, blank=True, on_delete=models.SET_NULL)
    Ten_kpi              = models.ForeignKey(Khung_kpi, blank=True,  null=True, on_delete=models.CASCADE)
    tu_danhgia_dapung     = models.IntegerField(blank=True, null=True)# Cá nhân tự đánh giá
    Quanly_danhgia        = models.IntegerField(blank=True, null=True)# Quản lý đánh giá cá nhân
    Ketqua_danhgia        = models.IntegerField(blank=True, null=True)# Điểm thống nhất cuối cùng

    Tile_hoanthanh     = models.IntegerField(blank=True, null=True) # Kết quả đánh giá / Chỉ tiêu chi_tieu

    Diem_congviec       = models.IntegerField(blank=True, null=True) # Điểm kết quả cuối Thành thạo và Mức Quan trọng năng lực

    Diem_trongso         = models.CharField(max_length=220, blank=True, null=True)
    Ketqua_tile         = models.CharField(max_length=220, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.Tile_hoanthanh = int(self.Ketqua_danhgia) / int(self.Ten_kpi.chi_tieu)
        self.Diem_congviec = int(self.Tile_hoanthanh)
        self.Diem_trongso = int(self.Diem_congviec) * int(self.Ten_kpi.ti_trong)
        super(Danhgia_KPI, self).save(*args, **kwargs)










