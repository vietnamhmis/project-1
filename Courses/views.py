from django import template
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic.edit import FormView

from .form import FileFieldForm
from .models import Courses

def chayweb_index(request):
    object_list = Courses.objects.filter()
    return render(request, 'layouts/hmis.html', {
        'object_list': object_list,
        'nav': 'chayweb_index',
    })

def chayweb_about(request):
    object_list = Courses.objects.filter()
    return render(request, 'layouts/base_web.html', {
        'object_list': object_list,
        'nav': 'chayweb_about',
    })

def chayweb_course(request):
    object_list = Courses.objects.filter()
    return render(request, 'layouts/course.html', {
        'object_list': object_list,
        'nav': 'chayweb_course',
    })

def chayweb_blog(request):
    object_list = Courses.objects.filter()
    return render(request, 'layouts/Blog.html', {
        'object_list': object_list,
        'nav': 'chayweb_blog',
    })

def chayweb_Contac(request):
    object_list = Courses.objects.filter()
    return render(request, 'layouts/Contac.html', {
        'object_list': object_list,
        'nav': 'chayweb_Contac',
    })

def chayweb_thu(request):
    object_list = Courses.objects.filter()
    return render(request, 'layouts/Contac_thu.html', {
        'object_list': object_list,
        'nav': 'chayweb_Contac',
    })





def home_view(request):
    object_list = Courses.objects.all()
    paginator = Paginator(object_list, 2)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Courses/home.html', {'object_list': page_obj})


def about_view(request):
    return render(request, 'Courses/taxes.html', {
        # cho biến nav thế hight light
        'nav': 'about',
    })


### them video

def home_video(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/video.html', {
        'object_list': object_list,
        'nav': 'video',
    })


def home_login(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/login.html', {
        'object_list': object_list,
        'nav': 'login',
    })

# -- Nhân sự ---
@login_required(login_url='login')
#@allowed_users(allowed_roles= ['customer'])
def dashboard(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/dashboard.html', {
        'object_list': object_list,
        'nav': 'dashboard',
    })



def home_index(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/index.html', {
        'object_list': object_list,
        'nav': 'index',
    })


def admin_dashboard(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/dashboard.html', {
        'object_list': object_list,
        'nav': 'admin-dashboard',
    })


def employee_dashboard(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/employee-dashboard.html', {
        'object_list': object_list,
        'nav': 'employee-dashboard',
    })


def employees(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/employees.html', {
        'object_list': object_list,
        'nav': 'employees',
    })

def employees_list(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/employees-list.html', {
        'object_list': object_list,
        'nav': 'employees-list',
    })

def profile(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/profile.html', {
        'object_list': object_list,
        'nav': 'profile',
    })

def holidays(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/holidays.html', {
        'object_list': object_list,
        'nav': 'holidays',
    })

def leaves(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/leaves.html', {
        'object_list': object_list,
        'nav': 'leaves',
    })

def leaves_employee(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/leaves-employee.html', {
        'object_list': object_list,
        'nav': 'leaves-employee',
    })

def leave_settings(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/leave-settings.html', {
        'object_list': object_list,
        'nav': 'leave-settings',
    })

def attendance(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/attendance.html', {
        'object_list': object_list,
        'nav': 'attendance',
    })

def attendance_employee(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/attendance-employee.html', {
        'object_list': object_list,
        'nav': 'attendance-employee',
    })

def departments(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/departments.html', {
        'object_list': object_list,
        'nav': 'departments',
    })

def designations(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/designations.html', {
        'object_list': object_list,
        'nav': 'designations',
    })

def timesheet(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/timesheet.html', {
        'object_list': object_list,
        'nav': 'timesheet',
    })

def shift_scheduling(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/shift-scheduling.html', {
        'object_list': object_list,
        'nav': 'shift-scheduling',
    })

def shift_list(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/shift-list.html', {
        'object_list': object_list,
        'nav': 'shift-list',
    })

def overtime(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/overtime.html', {
        'object_list': object_list,
        'nav': 'overtime',
    })
# -- Kết thúc nhân sự

# -- Khách hàng
def clients(request):
    object_list = Courses.objects.all()
    return render(request, 'Courses/clients.html', {
        'object_list': object_list,
        'nav': 'clients',
    })

def clients_list(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/clients-list.html', {
        'object_list': object_list,
        'nav': 'clients-list',
    })

def client_profile(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/client-profile.html', {
        'object_list': object_list,
        'nav': 'client-profile',
    })
# Thành tích
def leads(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/leads.html', {
        'object_list': object_list,
        'nav': 'leads',
    })

# Bán hàng
def estimates(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/estimates.html', {
        'object_list': object_list,
        'nav': 'estimates',
    })

def create_estimate(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/create-estimate.html', {
        'object_list': object_list,
        'nav': 'create-estimate',
    })

def edit_estimate(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/edit-estimate.html', {
        'object_list': object_list,
        'nav': 'edit-estimate',
    })

def invoices(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/invoices.html', {
        'object_list': object_list,
        'nav': 'invoices',
    })

def create_invoice(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/create-invoice.html', {
        'object_list': object_list,
        'nav': 'create-invoice',
    })

def edit_invoice(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/edit-invoice.html', {
        'object_list': object_list,
        'nav': 'edit-invoice',
    })

def payments(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/payments.html', {
        'object_list': object_list,
        'nav': 'payments',
    })

def expenses(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/expenses.html', {
        'object_list': object_list,
        'nav': 'expenses',
    })

def provident_fund(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/provident-fund.html', {
        'object_list': object_list,
        'nav': 'provident-fund',
    })

def taxes(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/taxes.html', {
        'object_list': object_list,
        'nav': 'taxes',
    })

# Bán hàng
def categories(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/categories.html', {
        'object_list': object_list,
        'nav': 'categories',
    })

def sub_category(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/sub-category.html', {
        'object_list': object_list,
        'nav': 'sub-category',
    })

def budgets(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/budgets.html', {
        'object_list': object_list,
        'nav': 'budgets',
    })

def budget_expenses(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/budget-expenses.html', {
        'object_list': object_list,
        'nav': 'budget-expenses',
    })

def budget_revenues(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/budget-revenues.html', {
        'object_list': object_list,
        'nav': 'budget-revenues',
    })

# Lương
def salary(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/salary.html', {
        'object_list': object_list,
        'nav': 'salary',
    })

def salary_view(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/salary-view.html', {
        'object_list': object_list,
        'nav': 'salary-view',
    })

def payroll_items(request):
    object_list = Courses.objects.filter()
    return render(request, 'Courses/payroll-items.html', {
        'object_list': object_list,
        'nav': 'payroll-items',
    })
## chương trình up nhiều hình ảnh cùng lúc............................


class FileFieldFormView(FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = '...'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                ...  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
