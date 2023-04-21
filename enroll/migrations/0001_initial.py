# Generated by Django 2.2 on 2022-11-20 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nhansu', '0001_initial'),
        ('mota_cv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nhan_vien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='picture/%Y/%m')),
                ('ho_lot_thuong_dung', models.CharField(blank=True, max_length=50, null=True)),
                ('ten_thuong_dung', models.CharField(blank=True, max_length=15, null=True)),
                ('ma_nhan_vien', models.CharField(blank=True, max_length=5, null=True)),
                ('ngay_vao_nganh', models.DateField(blank=True, null=True)),
                ('ngay_vao_dv', models.DateField(blank=True, null=True)),
                ('tel_dd', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
                ('Gioi_tinh', models.CharField(blank=True, choices=[('Nam', 'Nam'), ('Nữ', 'Nữ')], max_length=3, null=True)),
                ('Nguoi_qly', models.CharField(blank=True, max_length=55, null=True)),
                ('Nguoi_h_dan', models.CharField(blank=True, max_length=55, null=True)),
                ('ngay_sinh', models.DateField(blank=True, null=True)),
                ('so_CCCD', models.CharField(blank=True, max_length=12, null=True)),
                ('ngay_cap_CCCD', models.DateField(blank=True, null=True)),
                ('so_Hochieu', models.CharField(blank=True, max_length=12, null=True)),
                ('ngay_cap_hochieu', models.DateField(blank=True, null=True)),
                ('Tinhtrang_gd', models.CharField(blank=True, choices=[('Độc thân', 'Độc thân'), ('Có vợ/chồng', 'Có vợ/chồng')], max_length=20, null=True)),
                ('C_danh_kiem_nhiem', models.CharField(blank=True, max_length=45, null=True)),
                ('Masothue_cn', models.CharField(blank=True, max_length=13, null=True)),
                ('So_nguoi_phuthuoc', models.SmallIntegerField(blank=True, default='0', null=True)),
                ('so_so_ld', models.CharField(blank=True, max_length=12, null=True)),
                ('so_so_bhxh', models.CharField(blank=True, max_length=10, null=True)),
                ('ngay_cap_sld', models.DateField(blank=True, null=True)),
                ('ma_phieu_kcb', models.CharField(blank=True, max_length=20, null=True)),
                ('Taikhoan_nh', models.CharField(blank=True, max_length=12, null=True)),
                ('Ten_nganhang', models.CharField(blank=True, max_length=25, null=True)),
                ('dc_hiennay', models.CharField(blank=True, max_length=80, null=True)),
                ('dc_thuong_tru', models.CharField(blank=True, max_length=120, null=True)),
                ('Chieu_cao', models.IntegerField(blank=True, null=True)),
                ('Can_nang', models.IntegerField(blank=True, null=True)),
                ('dd_nhan_dang', models.CharField(blank=True, max_length=55, null=True)),
                ('Danh_hieu_ph_tang', models.CharField(blank=True, max_length=55, null=True)),
                ('Ngay_vao_dang', models.DateField(blank=True, null=True)),
                ('Ngay_ct', models.DateField(blank=True, null=True)),
                ('Tai_chi_bo', models.CharField(blank=True, max_length=55, null=True)),
                ('Chuc_vu_dang', models.CharField(blank=True, max_length=55, null=True)),
                ('Ngay_vao_doan', models.DateField(blank=True, null=True)),
                ('Noi_vao_doan', models.CharField(blank=True, max_length=55, null=True)),
                ('Chuc_vu_doan', models.CharField(blank=True, max_length=55, null=True)),
                ('Diem_manh', models.TextField(blank=True, max_length=255, null=True)),
                ('Diem_yeu', models.CharField(blank=True, max_length=255, null=True)),
                ('Muctieu_cn', models.CharField(blank=True, max_length=255, null=True)),
                ('So_truong', models.CharField(blank=True, max_length=255, null=True)),
                ('Lsu_ban_than', models.CharField(blank=True, max_length=255, null=True)),
                ('Q_he_nuoc_ngoai', models.CharField(blank=True, max_length=255, null=True)),
                ('Thannhan_nn', models.CharField(blank=True, max_length=255, null=True)),
                ('Nhan_xet', models.CharField(blank=True, max_length=255, null=True)),
                ('Nguyen_quan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Tinh_que')),
                ('bo_phan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Bo_phan')),
                ('dan_toc', models.ForeignKey(blank=True, default='Kinh', null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Dan_toc')),
                ('don_vi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Don_vi')),
                ('ma_tinh_noi_sinh', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Tinh_sinh')),
                ('phuong_xa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Phuong_xa')),
                ('quan_huyen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Quan_huyen')),
                ('quoctich', models.ForeignKey(blank=True, default='Việt Nam', null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Quocgia')),
                ('thanhphan_gd', models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Thanhphan_gd')),
                ('tinh_thanh', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Tinh')),
                ('to_nhom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nhansu.To_nhom')),
                ('ton_giao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Ton_giao')),
                ('trinh_do_ctri', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.trinh_do_ct')),
                ('trinh_do_ql', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.trinh_do_qlnn')),
                ('trinhdo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Trinhdo')),
                ('trinhdovh', models.ForeignKey(blank=True, default='12/12', null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Trinhdovh')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vitri_CV', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mota_cv.Mota_Cv7')),
            ],
        ),
        migrations.CreateModel(
            name='Quanly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_thuong_dung', models.CharField(blank=True, max_length=15, null=True)),
                ('quanly', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='enroll.Nhan_vien')),
            ],
        ),
        migrations.CreateModel(
            name='khen_nhan_vien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ht_khenthuong', models.CharField(choices=[('HC', 'Huân chương lao động'), ('BKB', 'Bằng khen Bộ'), ('BKCP', 'Băng khen Chính phủ'), ('CSTĐB', 'CSTĐ Bộ, ngành'), ('CSTQ', 'CSTĐ Toàn quốc'), ('CSTĐ', 'Chiến sĩ thi đua'), ('LDXS', 'LĐ xuất sắc'), ('LDTT', 'Lao động Tiên tiến'), ('Huy chương', 'Huy chương'), ('gk', 'Giấy khen')], max_length=20, null=True)),
                ('nam_khen', models.DateField(max_length=4, null=True)),
                ('cap_khen', models.CharField(max_length=50, null=True)),
                ('Nguoi_khen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='enroll.Nhan_vien')),
            ],
        ),
        migrations.CreateModel(
            name='Gia_dinh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quan_he', models.CharField(blank=True, choices=[('cha', 'Cha'), ('me', 'Mẹ'), ('anh', 'Anh'), ('em', 'Em'), ('chú', 'Chú'), ('Bác', 'Bác'), ('Cô', 'Cô'), ('Cậu', 'Cậu'), ('Dì', 'Dì')], max_length=20, null=True)),
                ('ho_ten_quanhe', models.CharField(blank=True, max_length=50, null=True)),
                ('Nam_sinh', models.DateField(blank=True, null=True)),
                ('diachi_giadinh', models.CharField(blank=True, max_length=150, null=True)),
                ('Nghe_nghiep', models.CharField(blank=True, max_length=50, null=True)),
                ('Noi_Lamviec', models.CharField(blank=True, max_length=150, null=True)),
                ('ben_vo_chong', models.CharField(blank=True, choices=[('Bên ruột', 'Bên ruột'), ('Bên vợ/chồng', 'Bên vợ/chồng')], max_length=50, null=True)),
                ('Nguoi_khai', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='enroll.Nhan_vien')),
            ],
        ),
        migrations.CreateModel(
            name='daotao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tu_ngay', models.DateField(null=True)),
                ('Den_ngay', models.DateField(null=True)),
                ('Co_so_d_tao', models.CharField(max_length=80, null=True)),
                ('Chuyen_nganh', models.CharField(max_length=80, null=True)),
                ('Hinhthuc_dtao', models.SmallIntegerField(choices=[('Tập trung', 'Tập trung'), ('Vừa học vừa làm', 'Vừa học vừa làm')])),
                ('Loai_TN', models.CharField(choices=[('Giỏi', 'Giỏi'), ('Khá', 'Khá'), ('TB', 'Trung bình')], max_length=10, null=True)),
                ('Nguoi_daotao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='enroll.Nhan_vien')),
                ('Van_bang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nhansu.Trinhdo')),
            ],
        ),
    ]
