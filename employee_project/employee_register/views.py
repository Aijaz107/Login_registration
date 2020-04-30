from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
import psycopg2

connection = psycopg2.connect(user="postgres",
                            password="98499849",
                            host="127.0.0.1",
                            port="5432",
                            database="logindb")
cursor = connection.cursor()
postgreSQL_select_Query = "select * from employee_register_employee"

cursor.execute(postgreSQL_select_Query)
print("Selecting rows from Employeetable using cursor.fetchall")
employee_records = cursor.fetchall() 

'''print("Print each row and it's columns values")
print(employee_records)
print(employee_records[0][0])
print(employee_records[0][1])
print(employee_records[1][0])'''
print(employee_records)
pswd_list = [l[4] for l in employee_records] 
# Create your views here.

def login(request):
    return render(request,"employee_register/login.html")



def login2(request):
    #print(employee_records)
    return render(request,"employee_register/login2.html",{'pswd_list':pswd_list})

def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    print( Employee.objects.all())
    print( Employee.objects.get(fullname="ju"))
    #print(Employee._meta.get_field())
    return render(request, "employee_register/employee_list.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
