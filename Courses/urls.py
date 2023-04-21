from django.urls import path
from .views import home_view, home_video, about_view, home_login, home_index, dashboard, employee_dashboard, \
    admin_dashboard, employees, employees_list, profile, holidays, leaves, leaves_employee, leave_settings, attendance, \
    attendance_employee, departments, designations, timesheet, shift_scheduling, overtime, shift_list, clients, \
    clients_list, client_profile, leads, estimates, create_estimate, edit_estimate, invoices, create_invoice, \
    edit_invoice, payments, expenses, provident_fund, taxes, categories, sub_category, budgets, budget_expenses, \
    budget_revenues, salary, salary_view, payroll_items, chayweb_index, chayweb_about, chayweb_course, chayweb_blog, \
    chayweb_Contac, chayweb_thu

from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'Courses'

urlpatterns = [
    path('hmis/', chayweb_index, name='chayweb_index'),
    path('habout/', chayweb_about, name='chayweb_about'),
    path('hcore/', chayweb_course, name='chayweb_course'),
     path('hblog/', chayweb_blog, name='chayweb_blog'),
     path('hcontac/', chayweb_Contac, name='chayweb_Contac'),#layouts/Contac_thu.html
    path('chayweb_thu/', chayweb_thu, name='chayweb_thu'),

    path('xem/', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('video/', home_video, name='video'),
    path('login/', home_login, name='login'),
    path('index/', home_index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/admin-dashboard', admin_dashboard, name='dashboard'),
    # - Nhân sự --
    path('dashboard/employee-dashboard', employee_dashboard, name='employee-dashboard'),
    path('dashboard/employees', employees, name='employees'),
    path('dashboard/employees-list', employees_list, name='employees-list'),


    path('dashboard/profile', profile, name='profile'),

    path('dashboard/holidays', holidays, name='holidays'),
    path('dashboard/leaves', leaves, name='leaves'),
    path('dashboard/leaves-employee', leaves_employee, name='leaves-employee'),
    path('dashboard/leave-settings', leave_settings, name='leave-settings'),
    path('dashboard/attendance', attendance, name='attendance'),
    path('dashboard/attendance-employee', attendance_employee, name='attendance-employee'),

    path('dashboard/departments', departments, name='departments'),
    path('dashboard/designations', designations, name='designations'),
    path('dashboard/timesheet', timesheet, name='timesheet'),
    path('dashboard/shift-scheduling', shift_scheduling, name='shift-scheduling'),
    path('dashboard/shift-list', shift_list, name='shift-list'),
    path('dashboard/overtime', overtime, name='overtime'),
    # -- Kết thúc nhân sự

    # -- Khách hàng
    path('dashboard/clients', clients, name='clients'),
    path('dashboard/clients-list', clients_list, name='clients-list'),
    path('dashboard/client-profile', client_profile, name='client-profile'),

    # -- Thành tích
    path('dashboard/leads', leads, name='leads'),

    # -- Bán hàng
    path('dashboard/estimates', estimates, name='estimates'),
    path('dashboard/create-estimate', create_estimate, name='create-estimate'),
    path('dashboard/edit-estimate', edit_estimate, name='edit-estimate'),
    path('dashboard/invoices', invoices, name='invoices'),
    path('dashboard/create-invoice', create_invoice, name='create-invoice'),
    path('dashboard/edit-invoice', edit_invoice, name='edit-invoice'),
    path('dashboard/payments', payments, name='payments'),
    path('dashboard/expenses', expenses, name='expenses'),
    path('dashboard/provident-fund', provident_fund, name='provident-fund'),
    path('dashboard/taxes', taxes, name='taxes'),
    
    # -- Kế toán
    path('dashboard/categories', categories, name='categories'),
    path('dashboard/sub-category', sub_category, name='sub-category'),
    path('dashboard/budgets', budgets, name='budgets'),
    path('dashboard/budget-expenses', budget_expenses, name='budget-expenses'),
    path('dashboard/budget-revenues', budget_revenues, name='budget-revenues'),

    # -- Lương
    path('dashboard/salary', salary, name='salary'),
    path('dashboard/salary-view', salary_view, name='salary-view'),
    path('dashboard/payroll-items', payroll_items, name='payroll-items'),    
    

    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)