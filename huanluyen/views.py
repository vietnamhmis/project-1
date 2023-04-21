from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *

# __________________

def bangluong_list(request):
    querysets = khach_hang.objects.all()[2:5]
    ct_tu_van2 = Loptu_van.objects.all()[2:5]
    paginate_by = 3
    context = {'querysets': querysets, 'ct_tu_van2':ct_tu_van2}
    return render(request,'huanluyen/hmis.html', context)



   
def web_index(request):
    object_list = giangvien.objects.filter()
    return render(request, 'huanluyen/hmis.html', {
        'object_list': object_list,
        'nav': 'web_index',
    })


def web_about(request):
    giangviens = giangvien.objects.all()[0:1]
    giangvien1 = giangvien.objects.all()[1:3]
    giangvien2 = giangvien.objects.all()[4:6]
    giangvien3 = giangvien.objects.all()[6:8]
    giangvien4 = giangvien.objects.all()[8:10]
    giangvien5 = giangvien.objects.all()[10:12]
    giangvien6 = giangvien.objects.all()[12:14]

    giangvienct = giangvien.objects.filter(image = "")

    context = {'giangviens':giangviens, 'giangvien1':giangvien1, 'giangvien2':giangvien2,
               'giangvien3': giangvien3,  "giangvien4":giangvien4,
               'giangvien5':giangvien5,'giangvien6': giangvien6, 'giangvienctv':giangvienct}
    return render(request,'huanluyen/base_web.html', context)


def web_course(request):
    object_list = giangvien.objects.filter()
    return render(request, 'huanluyen/course.html', {
        'object_list': object_list,
        'nav': 'web_course',
    })

def web_blog(request):
    object_list = giangvien.objects.filter()
    return render(request, 'huanluyen/Blog.html', {
        'object_list': object_list,
        'nav': 'web_blog',
    })

def web_Contac(request):
    object_list = giangvien.objects.filter()
    return render(request, 'huanluyen/Contac.html', {
        'object_list': object_list,
        'nav': 'web_Contac',
    })


#--------------------------

@login_required(login_url='/login/')
def lop_tu_van(request):
    tenlop = request.GET.get('tenlop')
    print("tenlop:", tenlop)
    if tenlop == None:
       khoa_hoc = Noidungtu_van.objects.all()
    else:
       khoa_hoc = Noidungtu_van.objects.filter(tenlop__name = tenlop)
    tenlops = Loptu_van.objects.all()
    context = {'tenlops': tenlops, 'photos': khoa_hoc}
    return render(request, 'huanluyen/tu_van.html', context)


@login_required(login_url='/login/')
def viewChuongtrinh_tu_van(request, pk):
    khoa_hoc = Noidungtu_van.objects.get(id=pk)
    return render(request, 'huanluyen/tu_van_photo.html', {'photo': khoa_hoc})


@login_required(login_url='/login/')
def add_lop_tu_van(request):
    tenlops = Loptu_van.objects.all()
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        print('data:', data)
        print('avatars:', images)
        if data['tenlop'] != 'none':
            tenlop= Loptu_van.objects.get(id=data['tenlop'])
        elif data['tenlop_new'] != '':
            tenlop, created = Loptu_van.objects.get_or_create(
                name=data['tenlop_new'])
        else:
            tenlop = None
        for image in images:
            khoa_hoc = Noidungtu_van.objects.create(
                tenlop=tenlop,
                description=data['description'],
                ngay_tu_van=data['ngay_tu_van'],
                educator=data['educator'],
                image = image,
            )
        return redirect('tu_van')
    context = {'tenlops': tenlops}
    return render(request, 'huanluyen/tu_van_add.html', context)

# print('data:', data)#print('image:', image)
