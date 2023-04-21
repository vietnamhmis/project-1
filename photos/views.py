from django.shortcuts import render, redirect

from .models import *

# Create your views here.

def gallery(request):
    category = request.GET.get('category')
   # print("category:", category)
    if category == None:
        photos = Photo.objects.all()
    else:
       photos = Photo.objects.filter(category__name = category)

    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})

def addPhoto(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        print('data:', data)
        print('avatars:', images)
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None
        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                ho_lot_thuong_dung=data['ho_lot_thuong_dung'],
                ten_thuong_dung=data['ten_thuong_dung'],
                ma_nhan_vien=data['ma_nhan_vien'],
                ngay_vao_nganh=data['ngay_vao_nganh'],
                image = image,
            )
        return redirect('gallery')
    context = {'categories': categories}
    return render(request, 'photos/add.html', context)

       # print('data:', data)#print('image:', image)

