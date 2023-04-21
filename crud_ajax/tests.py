from django.test import TestCase
# Views.py

from django.views.generic import ListView
from .models import CrudUser

class CrudView(ListView):
    model = CrudUser
    template_name = 'crud_ajax/crud.html'
    context_object_name = 'users'
    paginate_by = 15

# Views.pyPost.objects.all().order_by('-date')

from .models import CrudUser
from django.views.generic import View
from django.http import JsonResponse


class CreateCrudUser(View):
    def  get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.create(
            name = name1,
            address = address1,
            age = age1
        )

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)


class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)
        obj = CrudUser.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        obj.save()
        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}
        data = {
            'user': user
        }
        return JsonResponse(data)

class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


# Create your tests here.
            <div class="modal-body">
                <input class="form-control" id="form-id" type="hidden" name="formId"/>
                <label for="kpo">KPO</label>
                <input class="form-control" id="form-user" type="text" name="formUser"/>

                <label for="chucdanh_CV">Chức danh/vị trí CV</label>
                <input class="form-control" id="form-chucdanh_CV" type="text" name="formChucdanh_CV"/>


                <label for="kpi_cv">Chức danh/vị trí CV</label>
                <input class="form-control" id="form-kpi_cv" type="text" name="formKpi_cv"/>

                <label for="ti_trong">Tuần xuất đánh giá</label>
                <input class="form-control" id="form-tan_xuat_d_gia" type="text" name="formTan_xuat_d_gia" min=10 max=100/>

                <label for="donvi_tinh">Đơn vị tính</label>
                <input class="form-control" id="form-donvi_tinh" type="text" name="formDonvi_tinh" min=10 max=100/>

                <label for="chi_tieu">Chỉ tiêu</label>
                <input class="form-control" id="form-chi_tieu" type="number" name="formChi_tieu" />

                <label for="ti_trong">Tỉ trọng</label>
                <input class="form-ti_trong" id="form-ti_trong" type="number" name="formTi_trong" min=0.01 max=1.00/>


            </div>