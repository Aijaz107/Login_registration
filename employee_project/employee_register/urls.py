from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.login,name='login'), # get and post req. for insert operation
    path('employee/', views.employee_form,name='employee_insert'), # get and post req. for insert operation
    path('<int:id>/', views.employee_form,name='employee_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
    path('list/',views.employee_list,name='employee_list'), # get req. to retrieve and display all records
    path('login2/',views.login2,name='login2'), # get req. to retrieve and display all records
    path('employee/list/',views.employee_list,name='employee_list'), # get req. to retrieve and display all records

]