    Luong_BHXH     = models.IntegerField(blank=True, null=True)
    Bang_luong_cu  = models.CharField(max_length=5, blank=True, null=True)
    Heso_cu         = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    Bac_cu          = models.IntegerField(blank=True, null=True)
    Ngay_giu_lg_cu = models.DateField(null=True,blank=True)

    Luong_cb         = models.IntegerField(blank=True, null=True)
    Nang_luc       = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
    So_ngayphep    = models.IntegerField(blank=True, null=True)


##-----

def dashboard(request):
    form = Form_Nhanvien(request.POST or None)
    object_list = Nhan_vien.objects.all()
    pro = Don_vi.objects.all()

    context = { 'object_list': object_list, 'form': form, "productss": pro,}

    if request.method == 'POST':
        bo_phan = form['bo_phan'].value()
        thang = form['thang'].value()

        if (bo_phan == '' or form['thang'].value() == ''):
            object_list = object_list.filter()

        elif(bo_phan != '' or form['thang'].value() == ''):
            object_list = object_list.filter(
                bo_phan_id = bo_phan
            )

        context =  {'bo_phan': bo_phan, 'object_list': object_list, 'form': form, "productss": pro,}
        Tong_NV = (object_list.aggregate(total=Count('id', field="id"))['total'])
        NV_nghi = object_list.aggregate(total=Count('id', field="id"))['total']
        NV_moi = object_list.aggregate(total=Count('id', field="id"))['total']
        NV_thu_viec = object_list.aggregate(total=Count('id', field="id"))['total']

        Ti_le_NV_moi = round((NV_moi/Tong_NV)*100,2)

        context= {
                'object_list': object_list, "productss": pro,
                'form': form, 'bo_phan': bo_phan,
                'nav': 'dashboard',
                'Tong_NV':Tong_NV, 'NV_nghi':NV_nghi, 'NV_moi':NV_moi, 'NV_thu_viec':NV_thu_viec, 'Ti_le_NV_moi':Ti_le_NV_moi}


    return render(request, 'enroll/dashboard_nv.html', context)

#---------
	data: [{{DV_1}},{{DV_2}},{{DV_3},{{DV_4}},{{DV_5}},{{DV_6}},{{DV_7}},{{DV_8}},{{DV_9}},{{DV_10}},{{DV_11}},{{DV_12}},{{DV_13}},{{DV_14}},{{DV_15}},{{DV_16}},{{DV_17}}, {{DV_18}},{{DV_19}},{{DV_20}} ],
    [{% for product in queryset %}  '{{ product.don_vi.Ten_DV|truncatewords:2 }}', {% endfor %}]

class luongcs(models.Model):
    hsluong = models.IntegerField(default=0)
    phucap = models.IntegerField(default=0)
    tongluongcs = models.IntegerField(...)

    #def save(self):
       # self.tongluongcb = self.hsluong + self.phucap
       # return super(luongcs, self).save()
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import luongcs


@admin.register(luongcs)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'hsluong','phucap', 'tongluongcs', )
    list_filter = [ 'id', 'hsluong',]



def dashboard(request):
    form = Form_Nhanvien(request.POST or None)
    object_list = Nhan_vien.objects.all()
    context=    { 'object_list': object_list}
    Tong_NV = (object_list.aggregate(total=Count('id', field="id"))['total'])
    NV_nghi = object_list.aggregate(total=Count('id', field="id"))['total']
    NV_moi = object_list.aggregate(total=Count('id', field="id"))['total']
    NV_thu_viec = object_list.aggregate(total=Count('id', field="id"))['total']
    context= {
        'object_list': object_list,
        'nav': 'dashboard',
        'Tong_NV':Tong_NV, 'NV_nghi':NV_nghi, 'NV_moi':NV_moi, 'NV_thu_viec':NV_thu_viec,}

    return render(request, 'enroll/dashboard_nv.html', context)
