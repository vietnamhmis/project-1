#Tìm kiếm đa bảng
#Các bảng trong CSDL có quan hệ với nhau nhờ vào các khóa ngoại, khi truy vấn dữ liệu, SQL cho phép bạn truy vấn các bản ghi có liên quan với nhau bằng cách nối các bảng lại bằng câu lệnh JOIN, Django cũng cho phép bạn làm điều đó, bạn chỉ cần đưa vào biểu thức tìm kiếm cú pháp <tên khóa ngoại>__<tên thuộc tính của bảng khác>=<giá trị>. Ví dụ:


#>>> Entry.objects.filter(blog__name='Beatles Blog')
#Câu lệnh trên sẽ tìm các bản ghi Entry có quan hệ với bảng Blog với name là “Beatles Blog”.


from django.db import models
from nhansu.models import Don_vi,Bo_phan,To_nhom
from enroll.models import Cong_viec
from django.db.models import Aggregate, Sum

# Create your models here.


class Dinhbien_base(models.Model):
    Tan_xuat = (
         ('Ngày', 'Ngày'),
         ('Tuần', 'Tuần'),
         ('Tháng', 'Tháng'),
         ('Quý', 'Quý'),
         ('Năm', 'Năm'),
          )
    donvitinh = (
         ('Ngày', 'Ngày'),
         ('Lần', 'Lần'),
         ('Hồ sơ', 'Hồ sơ'),
             )
    class Meta:
        abstract = True
    don_vi          = models.ForeignKey(Don_vi, null=True, on_delete= models.SET_NULL)
    bo_phan         = models.ForeignKey(Bo_phan, null=True, on_delete= models.SET_NULL)
    to_nhom         = models.ForeignKey(To_nhom,on_delete=models.CASCADE)
    chuc_vu         = models.ForeignKey(Cong_viec,on_delete=models.CASCADE)
    donvi_tinh      = models.CharField(max_length=20, blank=False, null=True, choices= donvitinh)
    tan_xuat_lviec  = models.CharField(max_length=20, blank=False, null=True, choices= Tan_xuat)


class dinhbien(Dinhbien_base):
    chucdanh_dinhbien = models.CharField(max_length=60, blank=True, null=True)
    dinhbien_hienco     = models.IntegerField(blank=True, null=True)
    laodong_hc_hienco   = models.IntegerField(blank=True, null=True)
    laodong_ca_hienco   = models.IntegerField(blank=True, null=True)

    Lao_dong_ngoaids    = models.IntegerField(blank=True, null=True)
    laodong_hc_dinhbien = models.IntegerField(blank=True, null=True)
    laodong_ca_dinhbien = models.IntegerField(blank=True, null=True)
    tong_dinhbien       = models.IntegerField(blank=True, null=True)

    chenhlech_dbien     = models.IntegerField(blank=True, null=True)
    Tong_phut_1nam      = models.IntegerField()
    ghichu              = models.CharField(max_length=500, blank=True, null=True)

    def save(self):
        self.dinhbien_hienco = self.laodong_hc_hienco + self.laodong_ca_hienco
        self.tong_dinhbien = self.laodong_hc_dinhbien + self.laodong_ca_dinhbien
        self.chenhlech_dbien = self.tong_dinhbien - self.dinhbien_hienco
        #self.Tong_phut_1nam = dinhbien.objects.filter().

        return super(dinhbien, self).save()


class Dinhbien_HC(Dinhbien_base):
    chucdanh        = models.ForeignKey(dinhbien, null=True, on_delete= models.SET_NULL)

    Noi_dung_cviec  = models.TextField(max_length=1000, blank=False, null=False)
    khoiluong_nam   = models.IntegerField()
    sophut_th_1lan  = models.IntegerField()
    Tong_phut_1nam  = models.IntegerField()
    Ngaytao         = models.DateTimeField(auto_now_add=True)
    Ngay_update     = models.DateTimeField(auto_now=True)

    def save(self):
        self.Tong_phut_1nam = self.sophut_th_1lan * self.khoiluong_nam
        return super(Dinhbien_HC, self).save()


class Dinhbien_ca(Dinhbien_base):
    chucdanh        = models.ForeignKey(dinhbien, null=True, on_delete= models.SET_NULL)
    Noi_dung_cviecca  = models.TextField(max_length=1000, blank=False, null=False)
    laodong_ca_1    = models.IntegerField()
    laodong_ca_2    = models.IntegerField()
    laodong_ca_3    = models.IntegerField()

    khoiluongsp_ca_1  = models.IntegerField(editable=False)
    khoiluongsp_ca_2  = models.IntegerField(editable=False)
    khoiluongsp_ca_3  = models.IntegerField(editable=False)

    sophut_th_1lanc  = models.IntegerField()

    Thoigian_yc_ca_1  = models.IntegerField()
    Thoigian_yc_ca_2  = models.IntegerField()
    Thoigian_yc_ca_3  = models.IntegerField()

    Tong_phut_1namc  = models.IntegerField()

    def save(self):
        self.khoiluongsp_ca_1 = self.laodong_ca_1 *1
        self.khoiluongsp_ca_2 = self.laodong_ca_2 *1
        self.khoiluongsp_ca_3 = self.laodong_ca_3 *1

        self.Thoigian_yc_ca_1 = self.khoiluongsp_ca_1 * self.sophut_th_1lanc
        self.Thoigian_yc_ca_2 = self.khoiluongsp_ca_2 * self.sophut_th_1lanc
        self.Thoigian_yc_ca_3 = self.khoiluongsp_ca_3 * self.sophut_th_1lanc

        self.Tong_phut_1namc = self.Thoigian_yc_ca_1 + self.Thoigian_yc_ca_2 + self.Thoigian_yc_ca_3
        return super(Dinhbien_ca, self).save()




