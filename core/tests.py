from django.test import TestCase

# Create your tests here.
@admin.register(Congviec_nangluc)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'chucdanh_CV',  'Muc_quantrong_nluc', 'Muc_thanhthao_nluc', 'Diem_tieuchuan')


@admin.register(danhgia_Nangluc_nv)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id',  'Kha_nang_dapung', 'Diem_manh', 'Diem_khacphuc')
