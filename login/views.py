from django.shortcuts import render
from .form import registerForm, loginForm
from django.views import View
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
# import decorrator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Make View tạo chương tình đăng ký
class registerUser(View):
    #Hiển thị form đăng ký
    def get(self, request):
        f_register = registerForm
        return render(request,'login/register.html', {'fff':f_register})

    # Lấy thông tin nhập từ form đăng ký  vào model hệ thống
    def post(self,request):
       # last_name= request.POST['last_name']
        #first_name= request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username,email,password)
        user.save()
        return render(request,'login/registerout.html')
        #return HttpResponse('Đăng ký thành công với %s %s' %(username, password))

# Make Chương trinh dang nhap
class loginUser(View):
    #Hiển thị form đăng nhập
    def get(self, request):
        flg = loginForm
        return render(request,'login/log.html', {'flg':flg})

    # Lấy thông tin nhập từ form đăng nhập  vào model hệ thống
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            #Dùng hàm login đăng nhập
            login(request,user)

            # return HttpResponse('Đăng nhập thành công')
           # return HttpResponseRedirect('/enroll/'+request.user.username)
            #Trả về courses/profile.html
            return render(request,'enroll/employes_profile_3.html')
        else:
             error = " Sorry! Username and Password didn't match, Please try again ! "
             return render(request, 'login/lamlai.html',{'error':error})


#Hàm thoát ra hệ thống
def logout_User(request):
    logout(request)
    return render(request,'login/log.html')
# return HttpResponse('Bạn đã thoát ra khỏi hệ thống')
#  return redirect('login:dangnhap')


#@login_required(login_url='/login/')
#def privatePage(request):
 #   return render(request,'login/private.html')

# Lớp đăng nhập vao form private.html
class privatePage(LoginRequiredMixin,View):
    login_url='/login/'
    def get(self, request):
        return render(request,'courses/profile.html')
