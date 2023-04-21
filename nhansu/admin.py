from django.contrib import admin


from import_export.admin import ImportExportModelAdmin

from .models import *

from .models import Trinhdo, Thanhphan_gd, Tinh, Dan_toc, Quocgia, Don_vi, Bo_phan, To_nhom, \
    Trinhdovh, Ton_giao, Tinh_que, trinh_do_ct, trinh_do_qlnn, Phuong_xa, Quan_huyen,  Nang_luc_2, Loai_nangluc


#--------
# Register your models here.
@admin.register(Product)
class PersonAdmin(ImportExportModelAdmin):
     list_display = ('id', 'category',)
#------


@admin.register(Thanhphan_gd)
class PersonAdmin(ImportExportModelAdmin):
     list_display = ('id', 'THANH_PHAN',)

@admin.register(Tinh)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'TEN_TINH',)
    search_fields = ('TEN_TINH',)

@admin.register(Quan_huyen)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'Ten_quan',)
    search_fields = ('Ten_quan',)

@admin.register(Phuong_xa)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'Ten_xa',)
    search_fields = ('Ten_xa',)

@admin.register(Tinh_que)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'TEN_TINH',)
    search_fields = ('TEN_TINH',)

@admin.register(Tinh_sinh)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'TEN_TINH',)
    search_fields = ('TEN_TINH',)

@admin.register(Quocgia)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'TEN_QUOC_GIA',)
    search_fields = ('TEN_QUOC_GIA',)


@admin.register(Ton_giao)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'TEN_TON_GIAO',)


@admin.register(Dan_toc)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'TEN_DAN_TOC',)
    search_fields = ('TEN_DAN_TOC',)

@admin.register(Don_vi)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'ma_DV', 'Ten_DV','diachi',  'so_nhanvien')
    search_fields = ('Ten_DV',)


@admin.register(Bo_phan)
class PersonAdmin(ImportExportModelAdmin):
  list_display = ('id', 'ma_bp', 'ten_bp', 'don_vi', 'nv_bp')
  search_fields = ('ten_bp',)

@admin.register(To_nhom)
class PersonAdmin(ImportExportModelAdmin):
  list_display = ('id', 'ma_to', 'ten_to', 'bo_phan', 'nv_tn')
  search_fields = ('ten_to',)

#--------------------CHƯƠNG TRÌNH HIỂN THỊ LÝ LỊCH............................................

@admin.register(trinh_do_ct)
class PersonAdmin(ImportExportModelAdmin):
  list_display = ('id', 'TEN_TRINH_DO',)

@admin.register(trinh_do_qlnn)
class PersonAdmin(ImportExportModelAdmin):
  list_display = ('id', 'TEN_TRINH_DO',)

@admin.register(Trinhdovh)
class PersonAdmin(ImportExportModelAdmin):
  list_display = ('id','TEN_TRINH_DO',)

@admin.register(Trinhdo)
class PersonAdmin(ImportExportModelAdmin):
  list_display = ('id', 'TEN_TRINH_DO',)



@admin.register(Ten_ngheDH)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name','dacdiem_nghe','loai_dh', 'ma_nghe']
   search_fields = ('ten_nghe',)

@admin.register(Loai_laodong)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'ma_loai_laodong']


@admin.register(Muc_ah_cty_11)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'titrong', 'diem']


@admin.register(Muc_ah_nv_12)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'titrong', 'diem']


@admin.register(Ycau_trinhdocm_21)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'titrong', 'diem']

@admin.register(Ycau_k_nghiem_22)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'titrong', 'diem']


@admin.register(Ycau_Ngoaingu_23)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'titrong', 'diem']


@admin.register(Ycau_CNTT_24)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'titrong', 'diem']

@admin.register(Ycau_kehoach_31)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'titrong', 'diem']

@admin.register(Ycau_sangtao_32)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'titrong', 'diem']

@admin.register(Ycau_doclap_33)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'titrong', 'diem']

@admin.register(Ycau_giaotiep_34)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'titrong', 'diem']

@admin.register(Ycau_cuongdo_35)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'titrong', 'diem']


@admin.register(Mt_laodong_41)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'titrong', 'diem']

@admin.register(Muc_rui_ro_42)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'titrong', 'diem']

   #--------------
@admin.register(Yeu_to_1_trinh_do)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'titrong', 'diem']


@admin.register(Yeu_to_2_Ky_nang)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'titrong', 'diem']


@admin.register(Yeu_to_3_Trach_nhiem)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'titrong', 'diem']

@admin.register(Yeu_to_4_Anh_huong)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'titrong', 'diem']


@admin.register(Yeu_to_5_Sangtao)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'titrong', 'diem']


@admin.register(Yeu_to_6_Giaotiep)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'titrong', 'diem']

@admin.register(Yeu_to_7_DK_lamviec)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'titrong', 'diem']

@admin.register(TK_ngach)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'nhom',  'diem']

@admin.register(Yeu_to_khac)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name', 'titrong', 'diem']

@admin.register(Loai_nangluc)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'name',]

@admin.register(Loai_kpi)
class PersonAdmin(ImportExportModelAdmin):
   list_display =  ['id', 'name', ]

@admin.register(KPI_list)
class PersonAdmin(ImportExportModelAdmin):
   list_display =  ['id', 'loai_kpi','name', ]

@admin.register(Donvi_tinh)
class PersonAdmin(ImportExportModelAdmin):
   list_display =  ['id', 'name', ]

@admin.register(Tochuc_Sudung_KPI_NL)
class PersonAdmin(ImportExportModelAdmin):
   list_display =  ['id', 'name', ]

@admin.register(Nang_luc_2)
class PersonAdmin(ImportExportModelAdmin):
   list_display =  ['id','ho_congviec', 'name', ]

@admin.register(Ho_congviec)
class PersonAdmin(ImportExportModelAdmin):
   list_display =  ['id', 'name', 'ma_ho_cv' ]

@admin.register(Loai_vanban)
class PersonAdmin(ImportExportModelAdmin):
   list_display =  ['id', 'name', ]


@admin.register(Vanban)
class PersonAdmin(ImportExportModelAdmin):
   list_display =  ['id','loai_vanban', 'name', ]
