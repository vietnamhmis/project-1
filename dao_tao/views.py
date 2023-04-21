from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def lop_daotao(request):
    tenlop = request.GET.get('tenlop')
    print("tenlop:", tenlop)
    if tenlop == None:
       khoa_hoc = Noidungdaotao.objects.all()
    else:
       khoa_hoc = Noidungdaotao.objects.filter(tenlop__name = tenlop)

    tenlops = Lopdaotao.objects.all()
    context = {'tenlops': tenlops, 'photos': khoa_hoc}
    return render(request, 'daotao/gallery.html', context)


def viewChuongtrinh_daotao(request, pk):
    khoa_hoc = Noidungdaotao.objects.get(id=pk)
    return render(request, 'daotao/photo.html', {'photo': khoa_hoc})


def add_lop_daotao(request):
    tenlop = Lopdaotao.objects.all()
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        print('data:', data)
        print('avatars:', images)
        if data['tenlop'] != 'none':
            tenlop= Lopdaotao.objects.get(id=data['tenlop'])

        elif data['tenlop_new'] != '':
            tenlop, created = Lopdaotao.objects.get_or_create(
                name=data['tenlop_new'])
        else:
            tenlop = None
        for image in images:
            kha_hoc = Noidungdaotao.objects.create(
                tenlop=tenlop,
                description=data['description'],
                ngay_daotao=data['ngay_daotao'],
                educator=data['educator'],
                image = image,
            )
        return redirect('gallery')
    context = {'tenlops': tenlop}
    return render(request, 'daotao/add.html', context)

# print('data:', data)#print('image:', image)


# This functions will delete/xóa
#def del_daotao(request, id):
 #   if request.method == 'POST':
  #      pi = Noidungdaotao.objects.get(pk=id)
    #    pi.delete()
     #   return HttpResponseRedirect('/')
        #return redirect('/')

def del_daotao(request, id):
    del_dt = Noidungdaotao.objects.get(pk=id)
    if request.method == 'POST':
        del_dt.delete()
        return HttpResponseRedirect('/daotao/')
    return render(request, 'daotao/daotao_delete.html')
